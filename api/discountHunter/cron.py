import datetime
from stores.models import Store
from .scraper import kaufland, billa, lidl


def get_data():
    for store in Store.objects.all():
        # if store.promotions.filter(expire_date=datetime.datetime.now()).count() or store.promotions.count() == 0:
        if store.name == "Billa":
            billa(store)
        if store.name == "Kaufland":
            kaufland(store)
        if store.name == "Lidl":
            lidl(store)
