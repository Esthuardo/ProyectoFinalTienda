from django.db import models
from products.models import Product


# Create your models here.
class ItemShopCart(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        db_table = "ItemShopCart"
