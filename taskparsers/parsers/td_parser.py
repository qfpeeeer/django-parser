from .models import Parser
from selenium import webdriver
import pyderman as dr
from selenium.webdriver import ActionChains

import urllib.parse as urlparse
from urllib.parse import parse_qs
from bs4 import BeautifulSoup
from urllib.parse import urlencode


class TD(Parser):
    def __init__(self, category, URL):
        self.path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False,
                               version=None, filename=None, return_info=False)
        self.category = category
        self.URL = URL

    def add_params(self, URL, params=None):
        if params is None:
            return URL

        url_parts = list(urlparse.urlparse(URL))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)
        return urlparse.urlunparse(url_parts)

    def get_driver(self, URL):
        driver = webdriver.Chrome(self.path)
        driver.get(URL)
        return driver

    def close_welcome_modal(self, driver):
        modal_window = driver.find_element_by_class_name('VerifyCityModal__Actions')
        if modal_window:
            yes_button = modal_window.find_element_by_class_name('ButtonNext')
            ActionChains(driver).click(yes_button).perform()
        else:
            print("ERROR!!!")

    def get_html(self, driver):
        self.close_welcome_modal(driver)
        html_source = driver.page_source
        return html_source

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='ProductCard-Content')
        products = []
        for item in items:
            products.append(
                {
                    'category': self.category,
                    'title': item.find('h4').get_text(strip=True),
                    'link': self.HOST + item.get('href'),
                    'price': item.find('data').get_text(strip=True),
                }
            )
        return products

    def get_pages_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        url = soup.find('a', class_='CategoryPagination-Arrow_direction_last').get('href')
        parsed = urlparse.urlparse(url)
        return int(parse_qs(parsed.query)['page'][0])

    def parse(self):
        cur_driver = self.get_driver(self.URL)
        html = self.get_html(cur_driver)
        items = []
        pages_count = self.get_pages_count(html)
        for page in range(1, pages_count + 1):
            cur_driver.close()
            cur_driver = self.get_driver(self.add_params(self.URL, params={'page': page}))
            html = self.get_html(cur_driver)
            items.extend(self.get_content(html))
        return items
