import logging

from config import celery_app

from .models import Cryptocurrency

logger = logging.getLogger(__name__)


@celery_app.task()
def get_coinmarketcap_cryptocurrencies():
    try:
        if Cryptocurrency.objects.all().count() == 0:
            Cryptocurrency.save_cryptocurrencies()
    except Exception as e:
        logger.warning(e)
