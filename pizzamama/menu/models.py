from django.db import models


# Create your models here.


class Pizza(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    Vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.name
