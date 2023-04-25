from django.db import models


# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)

    class Meta:
        managed = False


class Result(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField
    origin = models.URLField

    class Meta:
        managed = False
