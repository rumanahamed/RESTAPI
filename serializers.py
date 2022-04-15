from rest_framework import serializers
from .models import Product


class Product_Serializers(serializers.ModelSerializer):
    class Meta:
        model  = Product  #key value pair
        fields = '__all__'

class Serializer_Serializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=200)

