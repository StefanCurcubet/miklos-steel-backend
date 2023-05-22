from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(null=True, blank=True)
    inventory = models.IntegerField()

    def __str__(self):
        return self.name + ' | ' + str(self.inventory)


class BasketItem(models.Model):
    product_name = models.TextField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name) + str(self.quantity) + str(self.created)

