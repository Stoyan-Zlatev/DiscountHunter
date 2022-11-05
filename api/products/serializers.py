from .models import Product
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return str(obj)

    class Meta:
        model = Product
        fields = ['id', 'name', 'new_price', 'image_url']


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'sub_title', 'old_price', 'new_price', 'base_price', 'quantity', 'discount_phrase',
                  'description', 'image_url']
