import string
from typing import List
from .src.driver import get_driver

from djangoapp.models import Card, Result
from .src.tcg_player import scrape_tcg_player


def run_scraper(card: Card) -> List[Result]:
    return scrape_tcg_player(card, get_driver(get_proxy()))


def get_proxy() -> string:
    return ('http://customer-%s:%s@pr.oxylabs.io:7777' %
    ('leohrbl', 'Test123!'))
