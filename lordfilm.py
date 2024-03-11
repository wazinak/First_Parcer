import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for p in range(1,101):
    url = f'https://lo1.lordfilm7.work/filmy/page/{p}/'
    res = requests.get(url)
    print(res.status_code)
    print(p)
    soup = BeautifulSoup(res.text, 'lxml')
    films = soup.find_all('div',class_='th-item')

    for film in films:
        name = film.find('div',class_='th-title').text
        try:
            rate = film.find('div',class_='th-rate th-rate-imdb').find('span').text
        except AttributeError:
            continue
        html = film.find('a',class_='th-in with-mask').get('href')
        data.append([name, rate, html])

headers = ["name", 'rate', 'html']
df = pd.DataFrame(data, columns=headers)
csv_name = 'lordfilm' + '.csv'
df.to_csv(csv_name)
print(len(data))





#print(name)
#print(rate)
#print(html)
#name = soup.find('div',class_='th-item').find('div',class_='th-title').text
#rate = soup.find('div',class_='th-item').find('div',class_='th-rate th-rate-imdb').find('span').text
#html = soup.find('div',class_='th-item').find('a',class_='th-in with-mask').get('href')