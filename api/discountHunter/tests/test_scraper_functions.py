from django.test import TestCase
from discountHunter.categories import *
from discountHunter.scraper import *


class TestScraper(TestCase):
    def setUp(self):
        self.kaufland_soup = get_soup(kaufland_cats[0])
        self.lidl_soup = get_soup(lidl_cats[0])
        self.billa_soup = get_soup(billa_cats[0])

    def test_find_kaufland_product_sub_title(self):
        self.assertEqual(get_product_title(self.kaufland_soup, ".t-offer-detail__subtitle"), True)


def get_soup(category):
    products = get_kaufland_category_products_url(category)
    for product in products:
        response = requests.get(product)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        return soup
