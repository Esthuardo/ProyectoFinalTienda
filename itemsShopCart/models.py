from django.db import models
from products.models import Product


# Create your models here.
class ItemShopCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "ItemShopCart"

    def __str__(self):
        return f"{self.product.name} - {self.quantity} unidades"
