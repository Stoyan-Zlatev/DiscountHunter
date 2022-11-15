from django.test import TestCase
from datetime import datetime as dt
from discountHunter.scraper import *
from stores.models import Store
from products.models import Product, Promotion

test_billa_promotion_dates_html = '<div class="date"><p class="dateSpan">Цените са валидни от 10.11.2022 г. до 16.11.2022 г.</p></div>'
test_billa_product_html = '<div class="product"> ' \
                          '<div class="actualProduct" style="float:left; width:25%; margin-right:2%;">Газирана напитка Pepsi</div>' \
                          '<div class="priceText" style="float:left; width:10%;">СТАРА<br>ЦЕНА</div>' \
                          '<div style="float:left; width:22%"><span class="price">2.59</span><span class="currency">лв.</span></div>' \
                          '<div class="priceText" style="float:left; width:10%;">НОВА<br>ЦЕНА</div><div class ="discount" style="float:left; width:10%;" > - 38 % </div>' \
                          '<div style = "float:left; width:15%" ><spanclass ="price" > 1.59 < / span > < span class ="currency" > лв.< / span > < / div ></div>'


class TestScraper(TestCase):
    def setUp(self):
        with open("discountHunter/tests/billa_test_html.txt", "r") as billa_source_html:
            self.billa_test_html = "\n".join(billa_source_html.readlines())
        self.billa_promotion_start_date_test = dt.strptime('10.11.2022', '%d.%m.%Y')
        self.billa_promotion_expire_date_test = dt.strptime('16.11.2022', '%d.%m.%Y')
        self.billa_product_title_test = 'Газирана напитка Pepsi'
        self.billa_product_old_price_test = 2.59
        self.billa_product_new_price_test = 1.59
        self.billa_product_discount_phrase_test = '- 34%'
        self.billa_test_store = Store.objects.create(name="Billa")
        self.billa_test_promotion = Promotion.objects.create(
            store=self.billa_test_store,
            start_date=self.billa_promotion_start_date_test,
            expire_date=self.billa_promotion_expire_date_test
        )
        self.billa_test_product = Product.objects.create(
            promotion=self.billa_test_promotion, title=self.billa_product_title_test,
            old_price=self.billa_product_old_price_test, new_price=self.billa_product_new_price_test,
            discount_phrase=self.billa_product_discount_phrase_test,
            image_url=BILLA_LOGO
        )
        self.billa_test_soup = BeautifulSoup(self.billa_test_html, "html.parser")
        self.billa_test_product_soup = self.billa_test_soup.find("div", 'product')

    def test_find_billa_promotion_start_date(self):
        promotion_starts = get_billa_promotion_start_date(self.billa_test_soup)
        self.assertEqual(promotion_starts, self.billa_promotion_start_date_test)

    def test_find_billa_promotion_expire_date(self):
        promotion_expires = get_billa_promotion_expire_date(self.billa_test_soup)
        self.assertEqual(promotion_expires, self.billa_promotion_expire_date_test)

    def test_find_billa_product_title(self):
        product_title = get_billa_product_title(self.billa_test_product_soup, ".actualProduct")
        self.assertEqual(product_title, self.billa_product_title_test)

    def test_find_billa_product_old_price(self):
        product_old_price = get_billa_product_old_price(self.billa_test_product_soup, ".price")
        self.assertEqual(product_old_price, self.billa_product_old_price_test)

    def test_find_billa_product_new_price(self):
        product_new_price = get_billa_product_new_price(self.billa_test_product_soup, ".price")
        self.assertEqual(product_new_price, self.billa_product_new_price_test)

    def test_find_billa_product_discount_phrase(self):
        product_discount_phrase = get_billa_product_discount_phrase(self.billa_test_product_soup, ".discount")
        self.assertEqual(product_discount_phrase, self.billa_product_discount_phrase_test)


def get_soup(category):
    products = get_kaufland_category_products_url(category)
    for product in products:
        response = requests.get(product)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        return soup
