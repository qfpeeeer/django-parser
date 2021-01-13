#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv
from db import insert

URL = 'https://www.sulpak.kz/f/smartfoniy'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://www.sulpak.kz'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='tile-container')
    phones = []
    for item in items:
        availability = item.find('span', class_='availability').get_text(strip=True)
        if availability != 'Нет в наличии':
            phones.append({
                'title': item.find('h3', class_='title').get_text(strip=True),
                'link': HOST + item.find('a').get('href'),
                'price': item.find('div', class_='price').get_text(strip=True),
            })
        else:
            phones.append({
                'title': item.find('h3', class_='title').get_text(strip=True),
                'link': HOST + item.find('a').get('href'),
                'price': 'null',
            })

    return phones


def get_pages_count(html):
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


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count+1):
            print(f'Parsing from {HOST} page {page} of {pages_count}...')
            html = get_html(URL, params={'page': page})
            if html.status_code == 200:
                items.extend(get_content(html.text))
        # save_items_to_db (items)
        print(items)
        print(f'Parsed {len(items)} items')
    else:
        print('ERROR')