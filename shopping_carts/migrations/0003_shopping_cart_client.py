# Generated by Django 4.2.6 on 2023-11-13 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_id_shopping_cart'),
        ('shopping_carts', '0002_remove_shopping_cart_id_list_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]