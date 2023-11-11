from django.db import models
from categories.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=20, unique=True)
    customs_code = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.TextField()
    number_order = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "productos"

    def __str__(self):
        return self.name
