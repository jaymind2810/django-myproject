# Generated by Django 3.1.7 on 2024-02-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_manager_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='country',
            field=models.CharField(default='UnKnown', max_length=128),
        ),
    ]
