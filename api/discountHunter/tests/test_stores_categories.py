from django.test import TestCase
from discountHunter.categories import *
from discountHunter.scraper import get_kaufland_category_products_url, get_lidl_category_products_url


class TestCategories(TestCase):
    def test_find_new_lidl_promotions_url(self):
        self.assertEqual(get_lidl_promotions_url().startswith(lidl_url), True)

    def test_find_new_lidl_promotions_categories(self):
        self.assertEqual(len(get_lidl_categories()) > 0, True)

    def test_find_new_lidl_categories_products_urls(self):
        self.assertEqual(len(get_lidl_category_products_url(get_lidl_categories()[0])) > 0, True)

    def test_find_new_kaufland_promotions_url(self):
        self.assertEqual(get_kaufland_promotions_main().startswith(kaufland_url), True)

    def test_find_new_kaufland_promotions_urls(self):
        self.assertEqual(len(get_kaufland_promotions_urls()) > 0, True)

    def test_find_new_kaufland_categories_urls(self):
        self.assertEqual(len(kaufland_categories_url()) > 0, True)

    def test_find_new_kaufland_categories_products_urls(self):
        self.assertEqual(len(get_kaufland_category_products_url(kaufland_categories_url()[0])) > 0, True)
