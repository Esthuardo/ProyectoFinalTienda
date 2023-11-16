from django.db import models


# Create your models here.
class PaymentMethod(models.Model):
    name = models.CharField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "PaymenMethod"

    def __str__(self):
        return self.name
