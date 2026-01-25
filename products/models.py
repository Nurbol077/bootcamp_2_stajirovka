from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
