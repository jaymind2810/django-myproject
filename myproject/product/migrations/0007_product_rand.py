# Generated by Django 3.1.7 on 2024-02-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_create_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]