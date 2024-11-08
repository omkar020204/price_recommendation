# pricechecker/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cheapest_site = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
