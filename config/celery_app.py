import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("apps")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
app.conf.beat_schedule = {
    "add-every-30-seconds": {
        "task": "apps.coinmarket.tasks.get_coinmarketcap_cryptocurrencies",
        "schedule": crontab(hour=0, minute=0),
    },
}
