# Generated by Django 5.0 on 2024-02-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pic',
        ),
        migrations.AddField(
            model_name='product',
            name='picname',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='product',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]
