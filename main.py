import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from api import api


def unian_news():
    url = 'https://www.unian.ua/detail/all_news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    results = soup.find_all('a', {'class': 'list-thumbs__title'})
    return_result = []
    for item in results:
        return_result.append({'header': item.text.replace('\n', ''), 'url': item['href']})
    return return_result


def exchange_rate():
    response = requests.get('https://jobs.dou.ua/vacancies/feeds/?category=Python')
    exch_rate = response.json()
    return exch_rate


def weather_current():
    lat = '50.452194'
    lon = '30.527561'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}')
    weather = response.json()
    return weather


def dou_news():
    driver = webdriver.Chrome()
    driver.get("https://dou.ua/")
    driver.quit()


if __name__ == '__main__':
    # print(unian_news())
    # print(exchange_rate())
    # print(weather_current())
    dou_news()
