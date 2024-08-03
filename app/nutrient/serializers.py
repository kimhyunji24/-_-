from rest_framework import serializers
from core.models import Nutrient

class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['name', 'description', 'health_impact', 'Daily_Recommended_Intake', 'Considerations']