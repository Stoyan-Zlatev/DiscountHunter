import requests
from bs4 import BeautifulSoup

billa_cats = ["https://ssbbilla.site/weekly"]

kaufland_url = "https://www.kaufland.bg/"

lidl_url = "https://www.lidl.bg/"


def lidl_promotions_url():
    '''
    Searches for the new url where lidl presents it promotions each week
    :return: Promotions url
    '''
    response = requests.get(lidl_url)
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    main_urls = soup.select(".nuc-m-header-main-nav-item__anchor-text")
    for url in main_urls:
        if url.get_text() == "Нови предложения":
            return f"{lidl_url}{url.parent['href']}"


def get_lidl_categories():
    response = requests.get(lidl_promotions_url())
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    categories = soup.find_all("a", "theme__item")
    categories_url = [f"https://www.lidl.bg/{category['href']}" for category in categories]
    return categories_url


def kaufland_get_promotions_main():
    '''
    Searches for the main promotions page
    :return: main promotion page url
    '''
    response = requests.get(kaufland_url)
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    navigation_url = soup.select(".m-accordion__link")
    promotions_page = None
    for url in navigation_url:
        if url.find("span").get_text().startswith("Предложения"):
            return f"https://www.kaufland.bg/{url['href']}"


def kaufland_get_promotions_urls():
    '''
    Searches for the promotions that start from monday and from thursday
    :return: promotions from monday and thursday urls
    '''
    response = requests.get(kaufland_get_promotions_main())
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    promotions = []
    for component in soup.select(".textimageteaser"):
        url = component.find("a")["href"]
        if not url.startswith("https:"):
            url = "https://www.kaufland.bg" + url
        promotions.append(url)

    return promotions


def kaufland_categories_url():
    '''
    Gets categories for monday promotions, the url with thursday promotions is equal to a category
    '''
    categories = []
    promotions_urls = kaufland_get_promotions_urls()
    response = requests.get(promotions_urls[0])
    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    buttons = soup.select(".a-button--primary")
    for button in buttons:
        if button.find("a") and button.find("a").get_text().startswith("Разгледай всички предложения"):
            categories.append(button.find("a")['href'])
    # Append category with promotions from thursday
    categories.append(promotions_urls[1])
    return categories


lidl_cats = get_lidl_categories()
kaufland_cats = kaufland_categories_url()
