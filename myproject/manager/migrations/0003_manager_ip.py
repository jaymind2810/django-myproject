# Generated by Django 3.1.7 on 2024-02-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20240217_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.CharField(default='-', max_length=128),
        ),
    ]
