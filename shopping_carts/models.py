from django.db import models

from itemsShopCart.models import ItemShopCart
from clients.models import Client
from datetime import datetime

# Create your models here.


class Shopping_cart(models.Model):
    # id_list_product = models.ForeignKey(List_product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(ItemShopCart)
    date = models.DateTimeField(default=datetime.now)
    payment_method = models.CharField(max_length=25, unique=True)
    direction = models.TextField(default="")

    class Meta:
        db_table = "shopping_carts"
