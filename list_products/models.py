from django.db import models
from products.models import Product

# Create your models here.


class List_product(models.Model):
    products = models.ManyToManyField(Product)
    quantity_products = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

    class Meta:
        db_table = "list_products"
