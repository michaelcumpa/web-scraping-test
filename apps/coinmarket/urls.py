from django.urls import path

from .views import (
    CryptocurrencyListView,
    CryptocurrencyRateDataListView,
    CryptocurrencyRateView,
)

urlpatterns = [
    path("", CryptocurrencyListView.as_view(), name="home"),
    path("<slug:slug>/", CryptocurrencyRateView.as_view(), name="currency_detail"),
    path(
        "<slug:slug>/rates/",
        CryptocurrencyRateDataListView.as_view(),
        name="currency_rates",
    ),
]
