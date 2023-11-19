# Generated by Django 4.2.6 on 2023-11-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_carts', '0004_alter_shopping_cart_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]