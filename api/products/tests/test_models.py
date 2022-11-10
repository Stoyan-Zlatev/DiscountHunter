from django.test import TestCase
from products.models import Product, Promotion
from stores.models import Store
from datetime import datetime as dt


class TestModels(TestCase):
    def setUp(self):
        self.store1 = Store.objects.create(name="Test Store")
        self.promotion1 = Promotion.objects.create(
            store=self.store1,
            start_date=dt.now(),
            expire_date=dt.now()
        )

        self.product1 = Product.objects.create(
            promotion=self.promotion1,
            title='Product Title 1',
            sub_title='Product Sub Title 1',
        )

        self.product2 = Product.objects.create(
            promotion=self.promotion1,
            title='Product Title 2'
        )

        self.product3 = Product.objects.create(
            promotion=self.promotion1,
            sub_title='Product Sub Title 3'
        )

    def test_promotion_str(self):
        self.assertEqual(str(self.promotion1),
                         f"Test Store {self.promotion1.start_date} - {self.promotion1.expire_date}")

    def test_0_product_str(self):
        self.assertEqual(str(self.product1), 'Product Title 1, Product Sub Title 1')

    def test_1_product_str(self):
        self.assertEqual(str(self.product2), 'Product Title 2')

    def test_2_product_str(self):
        self.assertEqual(str(self.product3), 'Product Sub Title 3')

    def test_product_get_promotion_start(self):
        self.assertEqual(self.product1.get_promotion_start(), self.promotion1.start_date)

    def test_product_get_promotion_expire(self):
        self.assertEqual(self.product1.get_promotion_expire(), self.promotion1.expire_date)

    def test_product_get_store(self):
        self.assertEqual(self.product1.get_store(), str(self.store1))

