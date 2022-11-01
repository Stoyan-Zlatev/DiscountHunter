from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from products.models import Product
from products.serializers import ProductsSerializer, ProductDetailSerializer


class ProductsView(ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductDetailView(RetrieveAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
