from rest_framework import serializers
from . models import Product


class Productserializer(serializers.Serializer):
    product_name = serializers.CharField(required=False)
    product_brand=serializers.CharField(required=False)

    image = serializers.ImageField(required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)