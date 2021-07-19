import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/marka-suzuki/'
# URL = 'https://auto.ria.com/uk/newauto/marka-acura/'
HOST = 'https://auto.ria.com'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36', 'accepy':'*/*'}


def get_html_auto(url, params=None):
    r = requests.get(url,headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages_conuts = soup.find_all('span', class_='mhide')
    if pages_conuts:
        return int(pages_conuts[-1].get_text())
    else:
        return 1
    print(pages_conuts)
      


def get_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    # print(items)
    # print(items)
    test = None
    cars_suzuki = []
    for item in items:
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text().replace(' грн',''),
        else:
            uah_price = 'NOT PRICE'
        cars_suzuki.append({
            'title':item.find('span', class_='link').get_text(strip=True),
            'link':HOST + item.find('a').get('href'),
            'usd_price':item.find('span', class_='bold').get_text(strip=True).replace(' $',''),
            'uah_price':uah_price,
            'city':item.find('span', class_='item region').get_text()
        })
    # test = soup.find_all('span', class_='green bold size22')
    # print(test)
    return cars_suzuki
    

def parse():
    html_auto = get_html_auto(URL)
    if html_auto.status_code == 200:
        # print(html_auto.text)
        # cars_suzuki = get_info(html_auto.text)
        pages_conts_fair = get_pages_count(html_auto.text)
        print(pages_conts_fair)
    else:
        print('Error')

parse()


