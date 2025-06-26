from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=10_000)
    expire_date = models.DateTimeField(auto_now=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"
    
