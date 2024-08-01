"""
Serializers for product APIs
"""
from rest_framework import serializers

from core.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_kind', 'manufacture', 'allergy', 'nutrient', 'product_img', 'meta_img']

class ProductDetailSerializer(ProductSerializer):

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['nutrient']