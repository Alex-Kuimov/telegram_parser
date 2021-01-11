from bs4 import BeautifulSoup
import requests
import re


class Finder:

    def __init__(self, name, q, url, el, el_type):
        self.name = name
        self.q = q
        self.url = url
        self.el = el
        self.el_type = el_type

    def find(self):
        site = requests.get(self.url + '' + self.q)
        content = BeautifulSoup(site.text, 'html.parser')
        ads = content.find_all(self.el_type, {'class': self.el})

        prices = list()

        for ad in ads:
            _price = int(re.sub('[^0-9]', '', ad.text))
            prices.append(_price)

        average = sum(prices) / len(prices)
        average_round = round(average)

        result = 'Средняя стоимость ' + self.q + ' на ' + self.name + ' составит: ' + str(average_round) + ' руб.'

        return result
