# Generated by Django 5.0.2 on 2024-02-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20240220_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
