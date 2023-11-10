from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "categories"
