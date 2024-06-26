from django.db import models
from customer.models import Order


class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class DeliveryAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tel_number = models.CharField(max_length=20)
    acceptance = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]
