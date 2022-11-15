from stores.models import Store
from .scraper import kaufland, billa, lidl


def get_data():
    for store in Store.objects.all():
        # if store.name == "Kaufland":
        #     kaufland(store)
        if store.name == "Lidl":
            lidl(store)
        # if store.name == "Billa":
        #     billa(store)
