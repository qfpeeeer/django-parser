import requests


class Parser:
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'accept': '*/*'}

    def __init__(self, URL, HOST):
        self.URL = URL
        self.HOST = HOST

    def get_html(self, params=None):
        response = requests.get(self.URL, headers=self.HEADERS, params=params)
        return response

    def get_content(self, html):
        pass

    def get_pages_count(self, html):
        pass

    def parse(self):
        pass