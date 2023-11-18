from django.db import models

from itemsShopCart.models import ItemShopCart
from clients.models import Client
from datetime import datetime
from payment_method.models import PaymentMethod

# Create your models here.


class Shopping_cart(models.Model):
    # id_list_product = models.ForeignKey(List_product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(ItemShopCart)
    date = models.DateTimeField(default=datetime.now)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, null=True
    )
    direction = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = "shopping_carts"
