from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=128)
    short_text = models.CharField(max_length=128)
    description = models.TextField()
    amount = models.CharField(default="1", max_length=10)
    picname = models.TextField(default="-")
    picurl = models.TextField(default="-")
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=12, default="00:00")

    def __str__(self):
        return self.name