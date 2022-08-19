from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class ProductPrice(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    price = models.FloatField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()


