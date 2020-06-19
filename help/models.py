from django.db import models

# Create your models here.


class information(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=256, default="")
