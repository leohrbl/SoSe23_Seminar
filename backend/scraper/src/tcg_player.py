import time

from djangoapp.models import Card, Result
from typing import List
from bs4 import BeautifulSoup
import seleniumwire.undetected_chromedriver.v2 as uc


def scrape_tcg_player(card: Card, driver: uc) -> List[Result]:
    scape_url = f'https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&q=' \
                f'{card.name}&view=grid&CardType=Pokemon&page=1'
    base_url = "https://www.tcgplayer.com"
    results = []

    driver.get(scape_url)
    time.sleep(25)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    last_page = get_last_page(soup)
    for i in range(1, last_page + 1):
        if i != 1:
            driver.get(f'https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&q='
                       f'{card.name}&view=grid&CardType=Pokemon&page={i}')
            time.sleep(25)
            soup = BeautifulSoup(driver.page_source, "html.parser")
        if i == 5:
            break
        items = soup.find_all("div", class_="search-result")
        for item in items:
            name = item.find('span', class_='search-result__title').text
            edition = item.find('h4', class_='search-result__subtitle').text
            rarity_number_string = item.find('section', class_='search-result__rarity').text.replace('·', '').strip()
            rarity_number_arr = rarity_number_string.rsplit(" ", 1)
            rarity = rarity_number_arr[0]
            card_number = rarity_number_arr[1]
            if item.find('section', class_='search-result__market-price--unavailable') is None:
                market_price = item.find('span', class_='search-result__market-price--value').text
            else:
                market_price = 'unavailable'
            shop = 'TCGPlayer'
            product_link = base_url + item.find('a')['href']
            picture_url = item.find('img')['src']

            results.append(Result(
                name=name,
                edition=edition,
                rarity=rarity,
                card_number=card_number,
                market_price=market_price,
                shop=shop,
                product_link=product_link,
                picture_url=picture_url
            ))
    return results


def get_last_page(soup: BeautifulSoup) -> int:
    page_container = soup.find("div", class_="tcg-pagination__pages")
    pages = page_container.find_all("span", class_="tcg-standard-button__content")
    return int(pages[-1].text)
