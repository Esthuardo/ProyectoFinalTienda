from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    REQUIRED_FIELDS = ["email", "password"]

    def create_user(self, **kwargs):
        record = self.model(**kwargs)
        record.set_password(kwargs["password"])
        record.save()
        return record
