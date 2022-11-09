import django_filters
import requests
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from products.models import Product
from products.serializers import ProductsSerializer, ProductDetailSerializer
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MyEndpointFilter


class ProductsView(generics.ListAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    filter_backends = {filters.SearchFilter, DjangoFilterBackend}
    # $ means Regex search
    search_fields = ['title', 'sub_title']
    filterset_class = MyEndpointFilter
    filterset_fields = ['promotion_start', 'promotion_expire_lte', 'promotion_expire_gte', 'store']


class ProductDetailView(RetrieveAPIView):
    """
    API endpoint that allows product details to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
