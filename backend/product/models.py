from django.db import models


class Product(models.Model:)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2, default=99.99)
