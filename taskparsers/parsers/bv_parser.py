from bs4 import BeautifulSoup
from .models import Parser


class BV(Parser):
    def __init__(self, category, URL):
        self.category = category
        self.URL = URL

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='bx_catalog_item')
        products = []
        for item in items:
            products.append({
                'category': self.category,
                'title': item.find('div', class_='bx_catalog_item_title').find('a').get_text(strip=True),
                'link': self.HOST + item.find('div', class_='bx_catalog_item_title').find('a').get('href'),
                'price': item.find('span', class_='bx-more-price-text').get_text(strip=True),
            })
        return products

    def get_pages_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find('div', class_='bx-pagination-container')
        if pagination:
            pages = pagination.find_all('li')
            if pages:
                return int(pages[-2].find('span').get_text(strip=True))
            else:
                return 1
        else:
            return 1

    def parse(self):
        html = self.get_html()
        if html.status_code == 200:
            items = []
            pages_count = self.get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                html = self.get_html(params={'PAGEN_1': page})
                if html.status_code == 200:
                    items.extend(self.get_content(html.text))
            return items
        else:
            Exception('BV No this kind of page')