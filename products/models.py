from django.db import models


class Promotion(models.Model):
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name='promotions')
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()

    def __str__(self):
        return f"{self.store} {self.expire_date}"


class Product(models.Model):
    promotion = models.ForeignKey(Promotion, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    new_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    base_price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    discount_phrase = models.CharField(max_length=255)
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
