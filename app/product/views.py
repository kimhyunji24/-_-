import requests, json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
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

    # GET 요청 시 외부 API에서 데이터를 가져와서 업데이트
    def list(self, request, *args, **kwargs):
        url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3?ServiceKey=j60V6KWnaSxrnblnCkKEEooTQdW9Jx4Ayh%2FmxhV46yPIDI5Lmk6mPKbVKPcTz757jswtGniYg%2BAH%2FgZPCnglUA%3D%3D&returnType=json'
        params = {
            'ServiceKey': settings.API_KEY,
            'type': 'json',
            'numOfRows': '20',
            'pageNo': '4',
            'format': 'json',
        }

        try:
            # API 요청
            response = requests.get(url, params=params)
            response.raise_for_status() # 응답 상태 코드 확인
            data = response.json() # JSON 데이터로 변환

            # 응답 상태 코드 및 내용 확인
            # print("응답 상태 코드:", response.status_code)
            # print("응답 내용:", json.dumps(data, indent=2)) # JSON 데이터 형식으로 출력
            # print("응답 내용 전체:", response.text)

            # 'body'와 'items' 키가 존재하는지 확인
            body = data.get('body', {})
            items = body.get('items', [])

            if not items:
                return Response({"error": "No items found in the response."}, status=500)

            # 데이터 처리 및 저장
            for item in items:
                item_data = item.get('item', {})
                # Product.objects.update_or_create(
                #     defaults={
                product_name = item_data.get('prdlstNm', 'N/A')
                product_kind = item_data.get('prdkind', 'N/A')
                manufacture = item_data.get('manufacture', 'N/A')
                allergy = item_data.get('allergy', 'N/A')
                nutrient = item_data.get('nutrient', 'N/A')
                ingredient = item_data.get('rawmtrl', 'N/A')  # 예를 들어 rawmtrl을 nutrient로 사용
                product_img = item_data.get('imgurl1', 'N/A')
                meta_img = item_data.get('imgurl2', 'N/A')
                #     }
                # )

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
                return self.get_paginated_response(serializer.data)
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            # 요청 예외 처리
            return Response({"error": str(e)}, status=502)
        except json.JSONDecodeError as e:
            # JSON 디코드 오류 처리
            return Response({"error": "JSON 디코드 오류", "details": str(e)}, status=500)