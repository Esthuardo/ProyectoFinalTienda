from django.db import models

from django.contrib.auth.models import AbstractUser, Permission, Group
from shopping_carts.models import Shopping_cart


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=18)
    direction = models.TextField(default="")
    status = models.BooleanField(default=True)
    id_shopping_cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)

    class Meta:
        db_table = "clients"

    def create_user(self, **kwargs):
        record = self.model(**kwargs)
        record.set_password(kwargs["password"])
        record.save()
        return record
