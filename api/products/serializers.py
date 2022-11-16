from django_filters import IsoDateTimeFilter, CharFilter
from .models import Product
from rest_framework import serializers
import django_filters


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    promotion_starts = serializers.SerializerMethodField()
    promotion_expires = serializers.SerializerMethodField()
    store = serializers.SerializerMethodField()

    def get_name(self, obj):
        return str(obj)

    def get_promotion_starts(self, obj):
        return obj.get_promotion_start()

    def get_promotion_expires(self, obj):
        return obj.get_promotion_expire()

    def get_store(self, obj):
        return obj.get_store()

    class Meta:
        model = Product
        fields = ['id', 'name', 'new_price', 'image_url', 'promotion_starts', 'promotion_expires', 'store']


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    promotion_starts = serializers.SerializerMethodField()
    promotion_expires = serializers.SerializerMethodField()
    store = serializers.SerializerMethodField()

    def get_promotion_starts(self, obj):
        return obj.get_promotion_start()

    def get_promotion_expires(self, obj):
        return obj.get_promotion_expire()

    def get_store(self, obj):
        return obj.get_store()

    class Meta:
        model = Product
        fields = ['id', 'title', 'sub_title', 'old_price', 'new_price', 'base_price', 'quantity', 'discount_phrase',
                  'description', 'image_url', 'promotion_starts', 'promotion_expires', 'store', 'promo_message']


class MyEndpointFilter(django_filters.FilterSet):
    promotion_start = IsoDateTimeFilter(field_name="promotion__start_date", lookup_expr='gte')
    promotion_expire_gte = IsoDateTimeFilter(field_name='promotion__expire_date', lookup_expr='gte')
    promotion_expire_lte = IsoDateTimeFilter(field_name='promotion__expire_date', lookup_expr='lte')
    store = CharFilter(field_name='promotion__store__name')

    class Meta:
        model = Product
        fields = '__all__'
