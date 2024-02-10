from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField()
    picname = models.TextField(default="-")
    picurl = models.TextField(default="-")

    def __str__(self):
        return self.name