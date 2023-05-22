from rest_framework.serializers import ModelSerializer

from api.models import Product, BasketItem


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketItemSerializer(ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'

