from django.contrib import admin
from .models import Product, BasketItem

# Register your models here.

admin.site.register(Product)
admin.site.register(BasketItem)
