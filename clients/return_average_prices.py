import re
import requests
from bs4 import BeautifulSoup as b

class ReturnAveragePrices:

    def return_average_price(self, sector):
        r = requests.get('https://www.storia.ro/vanzare/apartament/bucuresti/?search%5Bdistrict_id%5D=' + str(sector))
        soup = b(r.text, "html.parser")
        prices = soup.find_all("li", class_="hidden-xs offer-item-price-per-m")
        clean_prices = []
        for price in prices[2:]:
            raw_price = price.text
            clean_price = raw_price[:raw_price.find(",")]
            clean_prices.append(int(''.join(re.findall(r'\d+', clean_price))))
        return sum(clean_prices) / len(clean_prices)
