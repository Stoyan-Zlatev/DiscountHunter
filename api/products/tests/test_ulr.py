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

#     class PromotionTestCase(TestCase):
#
#         def promotion_items(self):
#             for promotion in Promotion.objects.all():
#                 self.assertNotEqual(promotion.items.all().count(), 0,
#                                     f"The promotion with id {promotion.pk} is  without products in it")
#
#     class ProductTestCase(TestCase):
#
#         def product_price(self):
#             self.assertNotEqual(Product.objects.filter(price__lte=0), 0, "The price of a product  is negative")
