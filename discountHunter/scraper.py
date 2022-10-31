import re
import requests
from bs4 import BeautifulSoup
from .categories import kaufland_cats, billa_cats, lidl_cats
from datetime import datetime as dt
from products.models import Promotion, Product

# TODO migrate and check if scraper is working

def convert_to_date(date_text):
    if int(date_text.split('.')[1]) < dt.now().month:
        year = dt.now().year + 1
    else:
        year = dt.now().year

    date_text = dt.strptime(f"{date_text}{year} 00:00:00", "%d.%m.%Y %H:%M:%S")
    return date_text


def billa(store):
    response = requests.get(billa_cats[0])
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", 'product')
    promotion_text = soup.find("div", 'date').get_text().split(" ")
    promotion_starts = dt.strptime(promotion_text[-5], '%d.%m.%Y')
    promotion_expires = dt.strptime(promotion_text[-2], '%d.%m.%Y')
    promotion, _ = Promotion.objects.get_or_create(store=store, expire_date=promotion_expires,
                                                   start_date=promotion_starts)

    print(f"{promotion_starts} - {promotion_expires}")
    for product in products:
        product_title = product.select_one(".actualProduct").text.strip()

        product_prices = product.select(".price")
        if len(product_prices) == 2:
            product_new_price = float(product_prices[1].text.strip())
            product_old_price = float(product_prices[0].text.strip())
        elif len(product_prices) == 1:
            product_new_price = float(product_prices[0].text.strip())
            product_old_price = None

        try:
            product_discount = product.select_one(".discount").text.strip()
        except AttributeError:
            product_discount = None

        if product_prices:
            print(product_title, product_old_price, product_new_price, product_discount, sep='\n')

        product, _ = Product.objects.get_or_create(promotion=promotion, title=product_title, sub_title=None,
                                                   old_price=product_old_price, new_price=product_new_price,
                                                   base_price=None, quantity=None, discount_phrase=product_discount,
                                                   image_url=None
                                                   )
    return True


def kaufland(store):
    for category in kaufland_cats[:]:
        response = requests.get(category)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("a", 'm-offer-tile__link u-button--hover-children')
        promotion_text = soup.find("div",
                                   "a-icon-tile-headline__subheadline").find("h2").text.strip()
        promotion_starts = dt.strptime(promotion_text.split()[-3], '%d.%m.%Y')
        promotion_expires = dt.strptime(promotion_text.split()[-1], '%d.%m.%Y')
        promotion, _ = Promotion.objects.get_or_create(store=store, expire_date=promotion_expires,
                                                       start_date=promotion_starts)

        print(f"{promotion_starts} - {promotion_expires}")
        for product in products:
            product_image = product.select_one(".a-image-responsive")['data-src']
            product_subtitle = product.select_one(".m-offer-tile__subtitle").text.strip()
            try:
                product_title = product.select_one(".m-offer-tile__title").text.strip()
            except AttributeError:
                product_title = None

            try:
                product_discount_phrase = product.select_one(".a-pricetag__discount").text.strip()
            except AttributeError:
                product_discount_phrase = None

            # It could be old_price and 'само' as well
            try:
                product_old_price = float(product.select_one(".a-pricetag__old-price").text.strip().replace(",", "."))
            except ValueError:
                product_old_price = None
                product_discount_phrase = product.select_one(".a-pricetag__old-price").text.strip()

            product_new_price = float(product.select_one(".a-pricetag__price").text.strip().replace(",", "."))

            try:
                product_base_price = product.select_one(".m-offer-tile__basic-price").text.strip()
            except AttributeError:
                product_base_price = None

            try:
                product_quantity = product.select_one(".m-offer-tile__quantity").text.strip()
            except AttributeError:
                product_quantity = None

            print(product_image, product_subtitle, product_title, product_old_price, product_discount_phrase,
                  product_new_price, product_base_price, product_quantity, sep='\n')

            product, _ = Product.objects.get_or_create(promotion=promotion, title=product_title,
                                                       sub_title=product_subtitle,
                                                       old_price=product_old_price, new_price=product_new_price,
                                                       base_price=product_base_price, quantity=product_quantity,
                                                       discount_phrase=product_discount_phrase,
                                                       image_url=product_image
                                                       )
    return True


def lidl(store):
    for category in lidl_cats[:]:
        response = requests.get(category)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("a", 'ret-o-card__link nuc-a-anchor')
        for product in products:
            product_image = product.find("img")["src"]
            product_title = " ".join(
                re.sub('\n', '', product.select_one(".ret-o-card__head").find("h3").text).strip().split())

            # Shows discount % as well as other type of promotion 'СПЕСТИ 20 ЛВ. САМО НА 05.11.'
            try:
                product_discount_phrase = product.select_one(".lidl-m-pricebox__highlight").text.strip()
            except AttributeError:
                product_discount_phrase = None

            try:
                product_old_price = product.select_one(".lidl-m-pricebox__discount-wrapper").text.strip()
            except AttributeError:
                product_old_price = None
            else:
                try:
                    product_old_price = float(product_old_price.replace(",", "."))
                except ValueError:
                    product_old_price = None

            product_new_price = float(product.select_one(".lidl-m-pricebox__price").text.strip().replace(",", "."))
            product_quantity = product.select_one(".lidl-m-pricebox__basic-quantity").text.strip()

            # Promotion could be interval date-date, but could be 'само на date', 'от date'
            # if promotion_starts is None - 'само на date'
            # if promotion_expires is None - 'от date'
            try:
                promotion_interval = product.select_one(".lidl-m-ribbon-item__text").text.strip()
                promotion_starts = promotion_interval.split()[-3]
                if promotion_starts == 'само':
                    promotion_starts = None
                promotion_expires = promotion_interval.split()[-1]
            except AttributeError:
                promotion_starts = None
                promotion_expires = None
            except IndexError:
                promotion_starts = promotion_interval.split()[-1]
                promotion_expires = None

            if promotion_starts:
                promotion_starts = convert_to_date(promotion_starts)
            if promotion_expires:
                promotion_expires = convert_to_date(promotion_expires)

            print(product_image, product_title, product_discount_phrase, product_old_price, product_new_price,
                  product_quantity, f"{promotion_starts} - {promotion_expires}", sep='\n')

            promotion, _ = Promotion.objects.get_or_create(store=store, expire_date=promotion_expires,
                                                           start_date=promotion_starts)

            product, _ = Product.objects.get_or_create(promotion=promotion, title=product_title,
                                                       sub_title=None,
                                                       old_price=product_old_price, new_price=product_new_price,
                                                       base_price=None, quantity=product_quantity,
                                                       discount_phrase=product_discount_phrase,
                                                       image_url=product_image
                                                       )
    return True
