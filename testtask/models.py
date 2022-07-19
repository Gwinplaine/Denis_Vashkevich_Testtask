from django.db import models

class Product(models.Model):
    #producttype_choices = (('DVD', 'DVD'), ('Book', 'Book'),('Furniture', 'Furniture'))
    
    #producttype = models.CharField(max_length=30, choices=producttype_choices)
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField(default=None, blank=True, null=True)
    weight = models.PositiveIntegerField(default=None, blank=True, null=True)
    height = models.PositiveIntegerField(default=None, blank=True, null=True)
    width = models.PositiveIntegerField(default=None, blank=True, null=True)
    length = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


