from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Order(models.Model):
    marketplace = models.CharField(max_length=35)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=35)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.lastname
