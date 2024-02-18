from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    product_id = models.IntegerField()
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=12, default="00:00")


    def __str__(self):
        return self.name
