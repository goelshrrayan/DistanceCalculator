from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"