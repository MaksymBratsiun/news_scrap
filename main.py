import requests
from bs4 import BeautifulSoup
from api import api


def unian_news():
    url = 'https://www.unian.ua/detail/all_news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    results = soup.find_all('a', {'class': 'list-thumbs__title'})
    for item in results:
        print(item.text, item['href'])


def exchange_rate():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    exch_rate = response.json()
    print(exch_rate)


def weather_current():
    lat = '50.452194'
    lon = '30.527561'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}')
    weather = response.json()
    print(weather)


if __name__ == '__main__':
    unian_news()
    exchange_rate()
    weather_current()
