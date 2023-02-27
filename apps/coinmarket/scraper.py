# Python dependencies
import datetime
import logging

import cloudscraper
from bs4 import BeautifulSoup as beauty
from slugify import slugify

from .constants import HOME_URL

logger = logging.getLogger(__name__)

Scraper = lambda: cloudscraper.create_scraper(delay=10, browser="chrome")  # noqa


def fetch_cryptocurrencies():
    cryptocurrencies = list()
    scraper = Scraper()
    response = scraper.get(HOME_URL)
    html = beauty(response.text, "lxml")
    table = html.find("table")
    rows = table.select("tbody tr")
    for row in rows:
        td = row.select_one("td:nth-child(3)")
        a = td.find("a")
        img = td.find("img")
        name = ""
        logo = ""
        symbol = ""
        path = ""
        if img:
            ps = td.select("p")
            name = ps[0].text
            symbol = ps[1].text
        else:
            spans = td.select("span")
            name = spans[1].text
            symbol = spans[2].text
        path = a["href"]
        logo = img["src"] if img else ""
        cryptocurrencies.append(
            dict(name=name, slug=slugify(name), logo=logo, symbol=symbol, path=path)
        )
    return cryptocurrencies


def process_home_page():
    scraper = Scraper()
    response = scraper.get(HOME_URL)

    try:
        if response.status_code == 200:
            logger.info("Got successfull coinmarketcap home page")
            return beauty(response.text, "lxml")
        else:
            logger.warning(
                f"Error get coinmarketcap home page, response status: {response.status_code}"
            )
    except ValueError as ve:
        logger.error(ve)


def get_cryptocurrency_rate(cryptocurrency):
    scraper = Scraper()
    response = scraper.get(f"{HOME_URL}{cryptocurrency.path}")
    try:
        if response.status_code == 200:
            logger.info(f"Got successfull {cryptocurrency.name} page")
            html = beauty(response.text, "lxml")
            div = html.select_one(".czILqM")
            tables = div.find_all("table")
            price = (
                tables[0]
                .select_one("tr:nth-child(1) > td")
                .text.replace("$", "")
                .replace(",", "")
            )
            price_change = f'{tables[0].select_one("tr:nth-child(2) > td > span > span").text}|{tables[0].select_one("tr:nth-child(2) > td > div > span").text}'  # noqa
            price_low_high = f'{tables[0].select_one("tr:nth-child(3) > td > div:nth-child(1)").text} {tables[0].select_one("tr:nth-child(3) > td > div:nth-child(2)").text}'  # noqa
            trading_volume = tables[0].select_one("tr:nth-child(4) > td > span").text
            volume_market_cap = tables[0].select_one("tr:nth-child(5) > td").text
            market_dominance = tables[0].select_one("tr:nth-child(6) > td").text
            market_rank = tables[0].select_one("tr:nth-child(7) > td").text
            circulating_supply = tables[4].select_one("tr:nth-child(1) > td").text
            total_supply = tables[4].select_one("tr:nth-child(2) > td").text
            max_supply = tables[4].select_one("tr:nth-child(3) > td").text
            data = dict(
                cryptocurrency=cryptocurrency,
                rate_date=datetime.datetime.now(),
                price=price,
                price_change=price_change,
                price_low_high=price_low_high,
                trading_volume=trading_volume,
                volume_market_cap=volume_market_cap,
                market_dominance=market_dominance,
                market_rank=market_rank,
                circulating_supply=circulating_supply,
                total_supply=total_supply,
                max_supply=max_supply,
            )
            return data
        else:
            logger.warning(
                f"Can't got {cryptocurrency.name} rate, response status: {response.status_code}"
            )
    except ValueError as ve:
        logger.error(ve)
