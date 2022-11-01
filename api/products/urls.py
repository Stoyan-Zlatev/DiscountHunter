from django.urls import path

from products.views import ProductsView, ProductDetailView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]
