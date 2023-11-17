from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=18)
    direction = models.TextField(default="")
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "clients"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Cifra la contraseña antes de guardarla
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Comprueba la contraseña proporcionada contra la versión cifrada
        return check_password(raw_password, self.password)

    # def create_user(self, **kwargs):
    #     record = self.model(**kwargs)
    #     record.set_password(kwargs["password"])
    #     record.save()
    #     return record
