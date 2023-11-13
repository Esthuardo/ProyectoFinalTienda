from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=18)
    direction = models.TextField(default="")
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "clients"

    # def create_user(self, **kwargs):
    #     record = self.model(**kwargs)
    #     record.set_password(kwargs["password"])
    #     record.save()
    #     return record
