from rest_framework import serializers

from ProductApp.models import Product, ProductPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',
                  'sku',
                  'description')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('productName',
                  'price',
                  'startDate',
                  'endDate')
