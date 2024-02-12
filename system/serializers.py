from rest_framework import serializers

from .models import Product, Part, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    part_in_order = OrderSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Part
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_in_part = PartSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

