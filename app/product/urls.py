from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', views.products),
]