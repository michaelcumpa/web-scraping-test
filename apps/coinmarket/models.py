from django.db import models

from .scraper import fetch_cryptocurrencies, get_cryptocurrency_rate


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    logo = models.URLField(blank=True)
    symbol = models.CharField(max_length=5, blank=True)
    path = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

    @classmethod
    def save_cryptocurrencies(cls):
        cryptocurrencies = map(lambda data: cls(**data), fetch_cryptocurrencies())
        return cls.objects.bulk_create(cryptocurrencies)


class Rate(models.Model):
    cryptocurrency = models.ForeignKey(
        Cryptocurrency, null=True, blank=True, on_delete=models.SET_NULL
    )
    rate_date = models.DateTimeField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    price_change = models.CharField(max_length=100)
    price_low_high = models.CharField(max_length=500)
    trading_volume = models.CharField(max_length=500)
    volume_market_cap = models.CharField(max_length=50)
    market_dominance = models.CharField(max_length=50)
    market_rank = models.CharField(max_length=5)
    circulating_supply = models.CharField(max_length=100)
    total_supply = models.CharField(max_length=100)
    max_supply = models.CharField(max_length=100)

    class Meta:
        ordering = ["-rate_date"]

    @classmethod
    def fetch_rate(cls, cryptocurrency):
        crytocurrency_rate = get_cryptocurrency_rate(cryptocurrency=cryptocurrency)
        rate = cls.objects.create(**crytocurrency_rate)
        return rate

    @property
    def rate_price(self):
        return f"${self.price}"

    @property
    def price_changed(self):
        return f'{self.price_change.split("|")[0]}'

    @property
    def price_changed_percentaje(self):
        return f'{self.price_change.split("|")[1]}'
