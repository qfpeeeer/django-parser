from bs4 import BeautifulSoup
from .models import Parser


class Sulpak(Parser):
    def __init__(self, category, URL):
        self.category = category
        self.URL = URL

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('li', class_='tile-container')

        products = []
        for item in items:
            price = item.find('div', class_='price').get_text(strip=True)
            if price:
                products.append({
                    'category': self.category,
                    'title': item.find('h3', class_='title').get_text(strip=True),
                    'link': self.HOST + item.find('a').get('href'),
                    'price': item.find('div', class_='price').get_text(strip=True),
                })

        return products

    def get_pages_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find('div', class_='pages-list')
        if pagination:
            pages = pagination.find_all('a')
            if pages:
                return int(pages[-1].get_text(strip=True))
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
                html = self.get_html(params={'page': page})
                if html.status_code == 200:
                    items.extend(self.get_content(html.text))
            return items
        else:
            Exception('_Sulpak_ No this kind of page')