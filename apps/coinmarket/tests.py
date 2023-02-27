from django.test import TestCase
from django.urls import reverse

from .models import Cryptocurrency


class CryptocurrencyModelTests(TestCase):
    fixtures = [
        "cryptocurrencies.json",
    ]

    def test_was_load_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class ModelTests(TestCase):
    fixtures = [
        "cryptocurrencies.json",
    ]

    def test_was_fetch_rate(self):
        btc = Cryptocurrency.objects.get(slug="bitcoin")
        response = self.client.get(reverse("currency_detail", args=(btc.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_was_fetch_rate_data(self):
        btc = Cryptocurrency.objects.get(slug="bitcoin")
        response = self.client.get(reverse("currency_rates", args=(btc.slug,)))
        self.assertEqual(response.status_code, 200)
