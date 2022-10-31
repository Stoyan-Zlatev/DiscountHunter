from django.db import models
from django.utils import timezone


class Promotion(models.Model):
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name='promotions')
    start_date = models.DateTimeField(null=True)
    expire_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.store} {self.start_date} - {self.expire_date}"


class Product(models.Model):
    promotion = models.ForeignKey(Promotion, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    sub_title = models.CharField(max_length=255, null=True)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
    new_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
    base_price = models.CharField(max_length=255, null=True)
    quantity = models.CharField(max_length=255, null=True)
    discount_phrase = models.CharField(max_length=255, null=True)
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.title and self.sub_title:
            return f"{self.title}, {self.sub_title}"
        elif not self.sub_title:
            return self.title
        else:
            return self.sub_title

