import requests, json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema, action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from django.conf import settings
from core.models import Product
from .serializers import ProductSerializer
from json.decoder import JSONDecodeError



API_KEY = settings.API_KEY

# Create your views here.

# 점수 계산 및 등급 결정 로직
def calculate_score(nutrient):
    # 영양 성분 정보가 "알수없음" 또는 "N/A"일 경우
    if nutrient.strip().lower() in ['알수없음', 'N/A']:
        return 0, 'Z'
    
    nutrients = nutrient.split('\n')
    scores = {
        'calories': 0,
        'sodium': 0,
        'carbohydrate': 0,
        'sugar': 0,
        'fat': 0,
        'trans_fat': 0,
        'satured_fat': 0,
        'cholesterol': 0,
        'protein': 0,
    }
    for line in nutrients:
        # 영양 성분 데이터만 포함된 라인인지 확인
        if 'mg' in line or 'g' in line or 'kcal' in line:
            parts = line.split(',')
            for part in parts:
                part = part.strip()
                nutrient_info = part.split()
                if len(nutrient_info) >= 2:
                    try:
                        # 영양 성분 이름과 값을 분리
                        name = nutrient_info[0]
                    # 비율(%) 정보 제거
                        value_str = ''.join(filter(lambda x: x.isdigit() or x == '.', nutrient_info[1]))
                    # 숫자 추출
                        value = float(value_str) if value_str else 0

                        if '열량' in name or 'kcal' in name:
                            scores['calories'] = 10 - min(value / 500, 10)
                        elif '나트륨' in name:
                            scores['sodium'] = 10 - min(value / 300, 10)
                        elif '탄수화물' in name:
                            scores['carbohydrate'] = 10 - min(value/ 150, 10)
                        elif '당류' in name:
                            scores['sugar'] = 10 - min(value / 60, 10)
                        elif '지방' in name:
                            scores['fat'] = 10 - min(value / 60, 10)
                        elif '트랜스지방' in name:
                            scores['trans_fat'] = 10 if value == 0 else 0
                        elif '포화지방' in name:
                            scores['saturated_fat'] = 10 - min(value / 15, 10)
                        elif '콜레스테롤' in name:
                            scores['cholesterol'] = 10 - min(value / 400, 10)
                        elif '단백질' in name:
                            scores['protein'] = min(value / 20, 10)
                    except (ValueError, IndexError):
                        continue

    total_score = sum(scores.values())

    if total_score >= 55:
        grade = 'A'
    elif total_score >= 48:
        grade = 'B'
    elif total_score > 0:
        grade = 'C'
    else:
        grade = 'Z'

    return total_score, grade

class ProductPagination(PageNumberPagination):
    page_size = 6 # 페이지당 항목 수
    page_size_query_param = 'page_size'
    max_page_size = 100 # 최대 페이지 크기

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination # 페이지네이션 클래스 설정
    # 검색 기능
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name']

    def list(self, request, *args, **kwargs):
        url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3?ServiceKey=j60V6KWnaSxrnblnCkKEEooTQdW9Jx4Ayh%2FmxhV46yPIDI5Lmk6mPKbVKPcTz757jswtGniYg%2BAH%2FgZPCnglUA%3D%3D&returnType=json'
        params = {
            'ServiceKey': settings.API_KEY,
            'type': 'json',
            'numOfRows': '100',
            'pageNo': '5',
            'format': 'json',
        }
        try:
            # API 요청
            response = requests.get(url, params=params)
            response.raise_for_status() # 응답 상태 코드 확인
            data = response.json() # JSON 데이터로 변환

            # 'body'와 'items' 키가 존재하는지 확인
            body = data.get('body', {})
            items = body.get('items', [])

            if not items:
                return Response({"error": "No items found in the response."}, status=500)

            # 데이터 처리 및 저장
            for item in items:
                item_data = item.get('item', {})
                product_name = item_data.get('prdlstNm', 'N/A')
                product_kind = item_data.get('prdkind', 'N/A')
                manufacture = item_data.get('manufacture', 'N/A')
                allergy = item_data.get('allergy', 'N/A')
                nutrient = item_data.get('nutrient', 'N/A')
                ingredient = item_data.get('rawmtrl', 'N/A')  # 예를 들어 rawmtrl을 nutrient로 사용
                product_img = item_data.get('imgurl1', 'N/A')
                meta_img = item_data.get('imgurl2', 'N/A')

                # 업데이트 또는 생성
                Product.objects.update_or_create(
                    product_name=product_name,
                    defaults={
                        'product_kind': product_kind,
                        'manufacture': manufacture,
                        'allergy': allergy,
                        'nutrient': nutrient,
                        'ingredient': ingredient,
                        'product_img': product_img,
                        'meta_img': meta_img,
                    }
                )
            
            # 모든 데이터를 반환
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
        
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                products = serializer.data
                for product in products:
                    nutrient_info = product.get('nutrient', '')
                    total_score, grade = calculate_score(nutrient_info)
                    product['total_score'] = total_score
                    product['grade'] = grade
                return self.get_paginated_response(products)

            serializer = self.get_serializer(queryset, many=True)
            products = serializer.data
            for product in products:
                nutrient_info = product.get('nutrient', '')
                total_score, grade = calculate_score(nutrient_info)
                product['total_score'] = total_score
                product['grade'] = grade
            return Response(products)

        except requests.exceptions.RequestException as e:
            # 요청 예외 처리
            return Response({"error": str(e)}, status=502)
        except json.JSONDecodeError as e:
            # JSON 디코드 오류 처리
            return Response({"error": "JSON 디코드 오류", "details": str(e)}, status=500)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        product_data = serializer.data

        nutrient_info = product_data.get('nutrient', '')
        total_score, grade = calculate_score(nutrient_info)

        product_data['total_score'] = total_score
        product_data['grade'] = grade

        return Response(product_data)

    @action(detail=True, methods=['get'])
    def recommend(self, request, pk=None):
        # 현재 선택된 상품 가져오기
        product = self.get_object()
        nutrient_info = product.nutrient
        # selected_score = product.total_score
        total_score, _ = calculate_score(nutrient_info)
        # prdkind = product.product_kind

        # 같은 종류의 상품들 중 선택된 상품보다 점수가 높은 상품들을 필터링
        product_kind = product.product_kind
        similar_products = Product.objects.filter(
            product_kind = product_kind
            # total_score__gt = selected_score
        ).exclude(pk=product.pk) # 본인 제외

        # 점수가 높은 순으로 정렬 후 상위 2-3개 상품 선택
        # recommended_products = similar_products.order_by('-total_score')[:3]
        recommendations = []
        for p in similar_products:
            p_score, _ = calculate_score(p.nutrient)
            if p_score > total_score:
                recommendations.append({
                    'id': p.id,
                    'product_name': p.product_name,
                    'total_score': p_score
                })
        # 상위 3개만 추출
        recommendations.sort(key=lambda x: x['total_score'], reverse=True)
        top_recommendations = recommendations[:3]

        return Response(top_recommendations)