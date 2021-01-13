import requests, re, json
from bs4 import BeautifulSoup

URL = 'https://www.mechta.kz/api/main/catalog_new/index.php'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://www.mechta.kz/product/'


def get_content():
    params = dict(
        section='smartfony',
        catalog='true',
        page_element_count=0
    )
    response = requests.get(URL, params)
    json_data = response.json()
    item_count = json_data['data']['ALL_ITEMS']
    params['page_element_count'] = item_count

    response = requests.get(URL, params)
    json_data = response.json()

    products = []
    for item in json_data['data']['ITEMS']:
        products.append({
            'title': item['NAME'],
            'link': HOST + item['CODE'],
            'price': item['PRICE']['PRICE']
        })
    return products


def parse():
    items = get_content()
    print(items)
    print(f'Parsed {len(items)} items')
    return json.dumps(items)


# def check():
#     items = get_content()
#     print(f'Parsed {len(items)} items')
#     obj = Data(title=items[0]['title'], link=items[0]['link'], price=items[0]['price'])
#     print (obj)
#     obj.save()
