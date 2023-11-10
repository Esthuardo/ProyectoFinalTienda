from django.db import models
from list_products.models import List_product

# Create your models here.


class Shopping_cart(models.Model):
    id_list_product = models.ForeignKey(List_product, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=25, unique=True)
    direction = models.TextField(default="")

    class Meta:
        db_table = "shopping_carts"
