from django.db import models


# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)

    class Meta:
        managed = False


class Result(models.Model):
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    market_price = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=255)

    class Meta:
        managed = False


