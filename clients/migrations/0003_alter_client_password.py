# Generated by Django 4.2.6 on 2023-11-17 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_id_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
