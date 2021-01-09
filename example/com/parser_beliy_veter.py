#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

URL = 'https://shop.kz/smartfony'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://shop.kz'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='bx_catalog_item')
    phones = []
    for item in items:
        phones.append({
            'title': item.find('div', class_='bx_catalog_item_title').find('a').get_text(strip=True),
            'link': HOST + item.find('div', class_='bx_catalog_item_title').find('a').get('href'),
            'price': item.find('span', class_='bx-more-price-text').get_text(strip=True),
        })
    print(phones)
    return phones


def get_pages_count(html):
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


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Parsing from {HOST} page {page} of {pages_count}...')
            html = get_html(URL, params={'PAGEN_1': page})
            if html.status_code == 200:
                items.extend(get_content(html.text))
        # save_items_to_db (items)
        print(items)
        print(f'Parsed {len(items)} items')
    else:
        print('ERROR')
