from django.urls import path, include

from rest_framework.routers import DefaultRouter

#from product.views import ProductViewSet
from . import views
# from .views import fetch_product_data
"""
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

app_name = 'product'


urlpatterns = [
    path('', include(router.urls)),
]
"""
urlpatterns = [
    path('products/', views.products),
]