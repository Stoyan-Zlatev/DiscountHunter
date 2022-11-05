from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from products.models import Product
from products.serializers import ProductsSerializer, ProductDetailSerializer
from rest_framework import filters

class ProductsView(ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = {filters.SearchFilter}
    # $ means Regex search
    search_fields = ['$title', '$sub_title']

class ProductDetailView(RetrieveAPIView):
    """
    API endpoint that allows product details to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
