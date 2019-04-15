from rest_framework import serializers
from .models import Order, Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'title', 'price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'url', 'marketplace', 'lastname', 'city', 'products')