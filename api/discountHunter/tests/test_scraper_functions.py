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

        with open("discountHunter/tests/kaufland_test_html.txt", "r") as kaufland_source_html:
            self.kaufland_test_html = "\n".join(kaufland_source_html.readlines())
        self.kaufland_test_soup = BeautifulSoup(self.kaufland_test_html, "html.parser")
        self.kaufland_promotion_text_test = '14.11. - 20.11.'
        self.kaufland_image_url_test = "https://webassets.kaufland.com/images/PPIM/KMO/BG2708_00094522_P.jpg?MYRAVRESIZE=150"
        self.kaufland_product_sub_title_test = "MAGGI"
        self.kaufland_product_title = "Нудели с вкус на зеленчуци"
        self.kaufland_product_discount_phrase = "- 25%"
        self.kaufland_product_old_price = 0.75
        self.kaufland_product_new_price = 0.56
        self.kaufland_product_base_price = "(1 кг = 9,50)"
        self.kaufland_product_quantity = "59,2 г"
        self.kaufland_product_description = "\n25% отстъпка\nза всички продукти\nс марка Maggi\n"
        self.kaufland_product_promotion_message = "Отстъпка за марка!"

        with open("discountHunter/tests/lidl_test_html.txt", "r") as lidl_source_html:
            self.lidl_test_html = "\n".join(lidl_source_html.readlines())
        self.lidl_test_soup = BeautifulSoup(self.lidl_test_html, "html.parser")
        self.lidl_test_product_component_soup = self.lidl_test_soup.select_one(".attributebox")
        self.lidl_product_image_url = "https://bg.cat-ret.assets.lidl/catalog5media/bg/article/7205616/gallery/zoom/7205616_0.jpg"
        self.lidl_product_title = "Шпеков салам Бургас"
        self.lidl_product_discount_phrase = "Двойно повече"
        self.lidl_product_old_price = 11.98
        self.lidl_product_new_price = 5.99
        self.lidl_product_quantity = "2 х 250 бр./опаковка"
        self.lidl_product_description = "В асортимента и 250 g за 5,99 лв.\nДо 5 промопакета на клиент\nВ промоцията участват само показаните продукти, обозначени с промоционалния символ „1 + 1“"
        self.lidl_product_promotion_start_date = dt.strptime("14.11.2022", '%d.%m.%Y')
        self.lidl_product_promotion_expire_date = dt.strptime("20.11.2022", '%d.%m.%Y')

    def test_find_billa_promotion_start_date(self):
        promotion_starts = get_billa_promotion_start_date(self.billa_test_soup)
        self.assertEqual(promotion_starts, self.billa_promotion_start_date_test)

    def test_find_billa_promotion_expire_date(self):
        promotion_expires = get_billa_promotion_expire_date(self.billa_test_soup)
        self.assertEqual(promotion_expires, self.billa_promotion_expire_date_test)

    def test_find_billa_product_title(self):
        product_title = get_product_title(self.billa_test_product_soup, ".actualProduct")
        self.assertEqual(product_title, self.billa_product_title_test)

    def test_find_billa_product_old_price(self):
        product_old_price = get_billa_product_old_price(self.billa_test_product_soup, ".price")
        self.assertEqual(product_old_price, self.billa_product_old_price_test)

    def test_find_billa_product_new_price(self):
        product_new_price = get_billa_product_new_price(self.billa_test_product_soup, ".price")
        self.assertEqual(product_new_price, self.billa_product_new_price_test)

    def test_find_billa_product_discount_phrase(self):
        product_discount_phrase = get_product_discount_phrase(self.billa_test_product_soup, ".discount")
        self.assertEqual(product_discount_phrase, self.billa_product_discount_phrase_test)

    def test_convert_to_date_function(self):
        date_to_convert_to = datetime(day=22, month=12, year=2022)
        self.assertEqual(convert_to_date("22.12."), date_to_convert_to)

    def test_find_kaufland_promotion_text(self):
        promotion_text = get_kaufland_promotion_text(self.kaufland_test_soup,
                                                     ["a-eye-catcher", "a-eye-catcher--secondary"])
        self.assertEqual(promotion_text, self.kaufland_promotion_text_test)

    def test_find_kaufland_product_image_url(self):
        product_image_url = get_kaufland_product_image(self.kaufland_test_soup, ["a-image-responsive",
                                                                                 "a-image-responsive--preview-knockout"])
        self.assertEqual(product_image_url, self.kaufland_image_url_test)

    def test_find_kaufland_product_sub_title(self):
        product_sub_title = get_kaufland_product_sub_title(self.kaufland_test_soup, ".t-offer-detail__subtitle")
        self.assertEqual(product_sub_title, self.kaufland_product_sub_title_test)

    def test_find_kaufland_product_title(self):
        product_title = get_product_title(self.kaufland_test_soup, ".t-offer-detail__title")
        self.assertEqual(product_title, self.kaufland_product_title)

    def test_find_kaufland_product_discount_phrase(self):
        product_discount_phrase = get_kaufland_product_discount_phrase(self.kaufland_test_soup, ".a-pricetag__discount",
                                                                       ".a-pricetag__old-price")
        self.assertEqual(product_discount_phrase, self.kaufland_product_discount_phrase)

    def test_find_kaufland_product_old_price(self):
        product_old_price = get_product_old_price(self.kaufland_test_soup, ".a-pricetag__old-price")
        self.assertEqual(product_old_price, self.kaufland_product_old_price)

    def test_find_kaufland_product_new_price(self):
        product_new_price = get_product_new_price(self.kaufland_test_soup, ".a-pricetag__price")
        self.assertEqual(product_new_price, self.kaufland_product_new_price)

    def test_find_kaufland_product_base_price(self):
        product_base_price = get_product_base_price(self.kaufland_test_soup, ".t-offer-detail__basic-price")
        self.assertEqual(product_base_price, self.kaufland_product_base_price)

    def test_find_kaufland_product_quantity(self):
        product_quantity = get_product_quantity(self.kaufland_test_soup, ".t-offer-detail__quantity")
        self.assertEqual(product_quantity, self.kaufland_product_quantity)

    def test_find_kaufland_product_description(self):
        product_description = get_kaufland_product_description(self.kaufland_test_soup, ".t-offer-detail__description")
        self.assertEqual(product_description, self.kaufland_product_description)

    def test_find_kaufland_product_promotion_message(self):
        product_promotion_message = get_product_promotion_message(self.kaufland_test_soup, ".t-offer-detail__mpa",
                                                          ".t-offer-detail__promo-message")
        self.assertEqual(product_promotion_message, self.kaufland_product_promotion_message)

    def test_find_lidl_product_image_url(self):
        product_image_url = get_lidl_product_image(self.lidl_test_soup, "multimediabox__preview-link")
        self.assertEqual(product_image_url, self.lidl_product_image_url)

    def test_find_lidl_product_title(self):
        product_title = " ".join(
            re.sub('\n', '', get_product_title(self.lidl_test_product_component_soup, ".attributebox__headline--h1")).split())
        self.assertEqual(product_title, self.lidl_product_title)

    def test_find_lidl_product_discount_phrase(self):
        product_discount_phrase = get_product_discount_phrase(self.lidl_test_product_component_soup, ".pricebox__highlight")
        self.assertEqual(product_discount_phrase, self.lidl_product_discount_phrase)

    def test_find_lidl_product_old_price(self):
        product_old_price = get_lidl_product_old_price(self.lidl_test_product_component_soup, ".pricebox__recommended-retail-price")
        self.assertEqual(product_old_price, self.lidl_product_old_price)

    def test_find_lidl_product_new_price(self):
        product_new_price = get_product_new_price(self.lidl_test_product_component_soup, ".pricebox__price")
        self.assertEqual(product_new_price, self.lidl_product_new_price)

    def test_find_lidl_product_quantity(self):
        product_quantity = get_product_quantity(self.lidl_test_product_component_soup, ".pricebox__basic-quantity")
        self.assertEqual(product_quantity, self.lidl_product_quantity)

    def test_find_lidl_product_description(self):
        product_description = get_lidl_product_description(self.lidl_test_product_component_soup, ".textbody")
        self.assertEqual(product_description, self.lidl_product_description)

    def test_find_lidl_product_promotion_start_date(self):
        product_promotion_starts = get_lidl_product_promotion_interval(self.lidl_test_product_component_soup,
                                                                                  ".ribbon__text")[0]
        self.assertEqual(product_promotion_starts, self.lidl_product_promotion_start_date)

    def test_find_lidl_product_promotion_expire_date(self):
        product_promotion_expires = get_lidl_product_promotion_interval(self.lidl_test_product_component_soup,
                                                                                  ".ribbon__text")[1]
        self.assertEqual(product_promotion_expires, self.lidl_product_promotion_expire_date)




