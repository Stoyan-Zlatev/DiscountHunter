from django.contrib import admin

from .models import Product, Promotion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title', 'sub_title')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['start_date']
