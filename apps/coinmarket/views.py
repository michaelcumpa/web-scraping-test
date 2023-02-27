from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Cryptocurrency, Rate


class CryptocurrencyListView(ListView):
    model = Cryptocurrency
    template_name = "pages/home.html"


class CryptocurrencyRateView(DetailView):
    model = Cryptocurrency
    template_name = "pages/crytocurrency_rates.html"

    def get_context_data(self, **kwargs):
        current_rate = Rate.fetch_rate(self.object)
        context_data = super().get_context_data(**kwargs)
        context_data["current_rate"] = current_rate
        return context_data


class CryptocurrencyRateDataListView(ListView):
    model = Rate

    response_class = JsonResponse

    def get_queryset(self):
        cryptocurrency = get_object_or_404(Cryptocurrency, slug=self.kwargs.get("slug"))
        # TODO: should to implemment it with celery
        queryset = Rate.objects.filter(cryptocurrency=cryptocurrency)[:10]
        data = {
            "labels": list(map(lambda obj: obj.rate_date.strftime("%H:%M"), queryset)),
            "datasets": [
                {
                    "label": "Precio $",
                    "data": list(map(lambda obj: obj.price, queryset)),
                }
            ],
        }
        return data

    def render_to_response(self, context, **response_kwargs):
        return self.response_class(self.object_list, safe=False)
