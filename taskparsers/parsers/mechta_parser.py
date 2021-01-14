import json
import requests
from .models import Parser


class Mechta(Parser):
    def __init__(self, category, URL):
        self.category = category
        self.URL = URL

    def get_json(self, params):
        response = requests.get(self.URL, params)
        json_data = response.json()
        return json_data

    def get_element_count(self):
        params = dict(
            section=self.category,
            catalog='true',
            page_element_count=0
        )
        json_data = self.get_json(params)
        item_count = json_data['data']['ALL_ITEMS']
        return item_count

    def get_content(self):
        params = dict(
            section=self.category,
            catalog='true',
            page_element_count=self.get_element_count()
        )
        json_data = self.get_json(params)
        products = []
        for item in json_data['data']['ITEMS']:
            products.append({
                'title': item['NAME'],
                'link': self.HOST + item['CODE'],
                'price': item['PRICE']['PRICE']
            })
        return products

    def parse(self):
        items = self.get_content()
        return json.dumps(items)