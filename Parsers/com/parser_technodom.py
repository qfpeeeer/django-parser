from selenium import webdriver
from selenium.webdriver import ActionChains
import urllib.parse as urlparse
from urllib.parse import parse_qs
from bs4 import BeautifulSoup
from urllib.parse import urlencode

URL = 'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony/smartfony'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://www.technodom.kz'
CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\87.0.4280.141\\chromedriver.exe'


def add_params(url, params=None):
    if params is None:
        return url

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def get_driver(url):
    driver = webdriver.Chrome(CHROME_PATH)
    driver.get(url)
    return driver


def close_welcome_modal(driver):
    modal_window = driver.find_element_by_class_name('VerifyCityModal__Actions')
    if modal_window:
        yes_button = modal_window.find_element_by_class_name('ButtonNext')
        ActionChains(driver).click(yes_button).perform()
    else:
        print ("ERROR!!!")


def get_html(driver):
    close_welcome_modal(driver)
    html_source = driver.page_source
    return html_source


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='ProductCard-Content')
    products = []
    for item in items:
        products.append(
            {
                'title': item.find('h4').get_text(strip=True),
                'link': HOST+item.get('href'),
                'price': item.find('data').get_text(strip=True),

            }
        )
    return products


def parse():
    cur_driver = get_driver(URL)
    html = get_html(cur_driver)
    items = []
    pages_count = get_pages_count(html)
    for page in range (1, 3):
        print (f'Parsing from {HOST} page {page} of {pages_count}...')
        cur_driver.close()
        cur_driver = get_driver(add_params(URL, params={'page': page}))
        html = get_html(cur_driver)
        items.extend(get_content(html))
    print (items)


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('a', class_='CategoryPagination-Arrow_direction_last').get('href')
    parsed = urlparse.urlparse(url)
    return int(parse_qs(parsed.query)['page'][0])