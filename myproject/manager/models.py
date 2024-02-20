from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Manager(models.Model):

    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    ip = models.CharField(max_length=128, default="-")
    country = models.CharField(max_length=128, default="UnKnown")
    
    def __str__(self):
        return self.name