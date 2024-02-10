from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):

    name = models.CharField(default="My Site", max_length=128)
    about = models.TextField(default="-")
    tell = models.CharField(default="+91 ", max_length=255)
    link = models.CharField(default="-", max_length=255)
    email = models.CharField(default="-", max_length=255)
    location = models.CharField(default="Ahmedabad, India", max_length=255)

    fb = models.CharField(default="fb", max_length=128)
    tw = models.CharField(default="tw", max_length=128)
    google = models.CharField(default="gg", max_length=128)
    pt = models.CharField(default="pt", max_length=128)

    picname = models.TextField(default="-")
    picurl = models.TextField(default="-")

    set_name = models.CharField(default="Site Settings", max_length=128)

    def __str__(self):
        return self.set_name + " | "+ str(self.pk)