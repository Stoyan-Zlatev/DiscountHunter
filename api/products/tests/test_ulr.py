from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import ProductsView, ProductDetailView


class TestUrls(SimpleTestCase):
    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductsView)

    def test_product_url_is_resolved(self):
        url = reverse('product', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)