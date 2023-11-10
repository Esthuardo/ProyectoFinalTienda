from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=18)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "users"

    def create_user(self, **kwargs):
        record = self.model(**kwargs)
        record.set_password(kwargs["password"])
        record.save()
        return record
