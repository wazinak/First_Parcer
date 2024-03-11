import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
data = []
for p in range(1,11):
    print(p)
    HOST = 'https://www.ivi.ru'
    url = f"https://www.ivi.ru/movies/2023/page{p}"
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    films = soup.find_all('li', class_='gallery__item gallery__item_virtual')
    sleep(2)
    for film in films:
        try:
            name = film.find('span', class_='nbl-slimPosterBlock__titleText').text
        except AttributeError:
            continue
        try:
            film_type = film.find('div', class_='nbl-poster__propertiesInfo').find('div', class_='nbl-poster__propertiesRow').text
        except AttributeError:
            continue
        try:
            rating = film.find('div', class_='nbl-poster__propertiesRow').text
        except AttributeError:
            continue
        try:
            html = HOST + film.find('a').get('href')
        except AttributeError:
            continue
        data.append([name, film_type,rating,html])
headers = ["name", 'film_type', "rating", 'html']
df = pd.DataFrame(data, columns=headers)
csv_name = 'ivi' + '.csv'
df.to_csv(csv_name)
print(len(data))



