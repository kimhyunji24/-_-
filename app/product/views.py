
import requests

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from django.conf import settings
# from django.shortcuts import HttpResponse
from product.models import Product
# from product.serializers import ProductSerializer
from json.decoder import JSONDecodeError

API_KEY = settings.API_KEY

# Create your views here.
"""
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def fetch_data(self, request):
        API_KEY = settings.API_KEY
        API_URL = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3'

        params = {
            'ServiceKey': API_KEY,
            'type': 'json',
            'numOfRows': '6',
            'pageNo': '1',
        }

        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

            # 데이터 처리 및 저장
        for item in data.get('items', []):
            Product.objects.update_or_create(
                prdlst_report_no=item.get('prdlstReportNo'),
                defaults={
                    'product_name': item.get('prdlstNm'), # 제품명
                    'product_kind': item.get('prdkind'), # 유형명
                    'manufacture': item.get('manufacture'), # 제조원
                    'allergy': item.get('allergy'), # 알레르기 유발 물질
                    'nutrient': item.get('nutrient'), # 영양 성분
                    'product_img': item.get('productImageURL'), # 제품 이미지
                    'meta_img': item.get('metaImageURL'), #메타 이미지
                }
            )
    
        return HttpResponse({"status": "Product data updated successfully!"})
"""
"""
def fetch_product_data():
    API_KEY = settings.API_KEY
    API_URL = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3'

    params = {
        'ServiceKey': API_KEY,
        'type': 'json',
        'numOfRows': '6',
        'pageNo': '1',
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status() # HTTP 오류 발생 시 예외를 발생시킴
    data = response.json()
    
    # 데이터 처리 및 저장
    for item in data.get('items', []):
        Product.objects.update_or_create(
            prdlst_report_no=item.get('prdlstReportNo'),
            defaults={
                'product_name': item.get('prdlstNm'), # 제품명
                'product_kind': item.get('prdkind'), # 유형명
                'manufacture': item.get('manufacture'), # 제조원
                'allergy': item.get('allergy'), # 알레르기 유발 물질
                'nutrient': item.get('nutrient'), # 영양 성분
                'product_img': item.get('productImageURL'), # 제품 이미지
                'meta_img': item.get('metaImageURL'), #메타 이미지
            }
        )
    
    return HttpResponse("Product data updated successfully!")
"""
"""
@api_view(['GET'])
def products(request):
    url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3'
    params = {
        'ServiceKey': API_KEY,
        'type': 'json',
        'numOfRows': '6',
        'pageNo': '1',
        'format': 'json', # 응답 형식을 JSON으로 명시
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        # 응답 내용 로그 남기기
        print("Response Content:", response.content.decode('utf-8'))

        #JSON 응답 파싱
        try:
            data = response.json()
        except JSONDecodeError:
            return Response({"error": "Failed to parse JSON response"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # response = requests.get(url, params=params)
        products_data = data.get('result', {}).get('baseList', [])
        return Response(products_data, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
"""

# 외부 API로부터 JSON 데이터 가져오기
# response = requests.get('https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3?ServiceKey=YOUR_SERVICE_KEY&prdlstReportNo=123456&returnType=JSON')
# data = response.json()
"""
# JSON 데이터에서 아이템 추출 및 저장
for item in data['item']:
    product_data = item['item']

    # Product 객체 생성 및 저장
    product = Product(
        product_name = product_data.get('prdlstNm', 'N/A'),
        product_kind = product_data.get('prdkind', 'N/A'),
        manufacture = product_data.get('manufacture', 'N/A'),
        allergy = product_data.get('allergy', 'N/A'),
        nutrient = product_data.get('nutrient', 'N/A'),
        product_img = product_data.get('imgurl1', 'N/A'),
        meta_img = product_data.get('imgurl2', 'N/A'),
    )
    product.save()
"""
"""
def fetch_product_data(request):
    url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3'
    params = {
        'ServiceKey': API_KEY,
        'type': 'json',
        'numOfRows': '6',
        'pageNo': '1',
        'format': 'json',
    }

    try:
        # API 요청
        response = requests.get(url, params=params)

        # 응답 상태 코드 확인
        print("응답 상태 코드:", response.status_code)
        
        # 응답 내용 로그
        print("응답 내용:", response.text)
        
        # JSON 데이터로 변환
        data = response.json()
        
        # JSON 데이터 반환
        return JsonResponse(data, safe=False)
    
    except JSONDecodeError as e:
        # JSON 디코드 오류 처리
        return JsonResponse({"error": "JSON 디코드 오류", "details": str(e)}, status=500)
    
    except requests.exceptions.RequestException as e:
        # 요청 예외 처리
        return JsonResponse({"error": str(e)}, status=502)
"""
def products(request):
    url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3?ServiceKey=j60V6KWnaSxrnblnCkKEEooTQdW9Jx4Ayh%2FmxhV46yPIDI5Lmk6mPKbVKPcTz757jswtGniYg%2BAH%2FgZPCnglUA%3D%3D&returnType=json'
    params = {
        'ServiceKey': settings.API_KEY,
        'type': 'json',
        'numOfRows': '6',
        'pageNo': '1',
        'format': 'json',
    }

    try:
        # API 요청
        response = requests.get(url, params=params)

        # 응답 상태 코드 및 내용 확인
        print("응답 상태 코드:", response.status_code)
        print("응답 내용:", response.text)
        
        # 응답이 비어있는지 확인
        if not response.text.strip():
            return JsonResponse({"error": "API 응답이 비어 있습니다."}, status=500)

        # JSON 데이터로 변환
        try:
            data = response.json()
        except JSONDecodeError as e:
            return JsonResponse({"error": "JSON 디코드 오류", "details": str(e)}, status=500)

        # 데이터 처리 및 저장
        items = data.get('result', {}).get('baseList', [])
        for item in items:
            Product.objects.update_or_create(
                prdlst_report_no=item.get('prdlstReportNo'),
                defaults={
                    'product_name': item.get('prdlstNm', 'N/A'),
                    'product_kind': item.get('prdkind', 'N/A'),
                    'manufacture': item.get('manufacture', 'N/A'),
                    'allergy': item.get('allergy', 'N/A'),
                    'nutrient': item.get('nutrient', 'N/A'),
                    'product_img': item.get('productImageURL', 'N/A'),
                    'meta_img': item.get('metaImageURL', 'N/A'),
                }
            )

        return JsonResponse({"status": "Product data updated successfully!"})

    except requests.exceptions.RequestException as e:
        # 요청 예외 처리
        return JsonResponse({"error": str(e)}, status=502)