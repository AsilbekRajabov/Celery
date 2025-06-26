from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=500)




