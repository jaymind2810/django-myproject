# Generated by Django 3.1.7 on 2024-02-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_remove_category_date_remove_category_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
