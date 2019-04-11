from django.db import models

class Order(models.Model):
    marketplace = models.CharField(max_length=35)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=35)
    product = models.CharField(max_length=50)
    price = models.FloatField()