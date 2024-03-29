# Generated by Django 5.0 on 2024-01-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_text', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('amount', models.IntegerField(default='1', max_length=10)),
                ('date', models.CharField(max_length=15)),
                ('pic', models.TextField()),
            ],
        ),
    ]
