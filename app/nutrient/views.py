from rest_framework import viewsets
from core.models import Nutrient
from .serializers import NutrientSerializer

# Create your views here.
class NutrientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer
