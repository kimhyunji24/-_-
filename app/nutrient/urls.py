from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nutrient', views.NutrientViewSet)

app_name = 'nutrient'

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', views.products),
]