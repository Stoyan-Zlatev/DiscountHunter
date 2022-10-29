import requests
from bs4 import BeautifulSoup

billa_cats = ["https://ssbbilla.site/weekly"]

kaufland_cats = [
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=01_%D0%9C%D0%B5%D1%81%D0%BE__%D0%BF%D1%82%D0%B8%D1%87%D0%B5_%D0%BC%D0%B5%D1%81%D0%BE__%D0%BA%D0%BE%D0%BB%D0%B1%D0%B0%D1%81%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=01a_%D0%9F%D1%80%D1%8F%D1%81%D0%BD%D0%B0_%D1%80%D0%B8%D0%B1%D0%B0.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=02_%D0%9F%D0%BB%D0%BE%D0%B4%D0%BE%D0%B2%D0%B5_%D0%B8_%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D1%87%D1%83%D1%86%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=03_%D0%9C%D0%BB%D0%B5%D1%87%D0%BD%D0%B8_%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=04_%D0%97%D0%B0%D0%BC%D1%80%D0%B0%D0%B7%D0%B5%D0%BD%D0%B8_%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=05_%D0%9A%D0%BE%D0%BD%D1%81%D0%B5%D1%80%D0%B2%D0%B8__%D0%B4%D0%B5%D0%BB%D0%B8%D0%BA%D0%B0%D1%82%D0%B5%D1%81%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=06_%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%B8_%D1%85%D1%80%D0%B0%D0%BD%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=07_%D0%9A%D0%B0%D1%84%D0%B5__%D1%87%D0%B0%D0%B9__%D0%B7%D0%B0%D1%85%D0%B0%D1%80%D0%BD%D0%B8_%D0%B8%D0%B7%D0%B4%D0%B5%D0%BB%D0%B8%D1%8F__%D1%81%D0%BD%D0%B0%D0%BA%D1%81.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=08_%D0%90%D0%BB%D0%BA%D0%BE%D1%85%D0%BE%D0%BB%D0%BD%D0%B8_%D0%B8_%D0%B1%D0%B5%D0%B7%D0%B0%D0%BB%D0%BA%D0%BE%D1%85%D0%BE%D0%BB%D0%BD%D0%B8_%D0%BD%D0%B0%D0%BF%D0%B8%D1%82%D0%BA%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=09_%D0%94%D1%80%D0%BE%D0%B3%D0%B5%D1%80%D0%B8%D1%8F__%D1%85%D1%80%D0%B0%D0%BD%D0%B0_%D0%B7%D0%B0_%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B8_%D0%BB%D1%8E%D0%B1%D0%B8%D0%BC%D1%86%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=10_%D0%95%D0%BB__%D1%83%D1%80%D0%B5%D0%B4%D0%B8__%D0%BE%D1%84%D0%B8%D1%81__%D0%BC%D0%B5%D0%B4%D0%B8%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=11_%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B8_%D0%BF%D0%BE%D1%82%D1%80%D0%B5%D0%B1%D0%B8.html',
    'https://www.kaufland.bg/aktualni-predlozheniya/ot-ponedelnik/obsht-pregled.category=12_%D0%A2%D0%B5%D0%BA%D1%81%D1%82%D0%B8%D0%BB__%D0%B8%D0%B3%D1%80%D0%B0%D1%87%D0%BA%D0%B8__%D0%B0%D0%B2%D1%82%D0%BE__%D1%83%D0%B8%D0%BA%D0%B5%D0%BD%D0%B4.html'
]

lidl_url = "https://www.lidl.bg/c/novo/c2738/w2"


def get_lidl_categories():
    response = requests.get(lidl_url)
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    categories = soup.find_all("a", "theme__item")
    categories_urls = [f"https://www.lidl.bg/{category['href']}" for category in categories]
    return categories_urls


lidl_cats = get_lidl_categories()
