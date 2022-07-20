from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    size = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name



