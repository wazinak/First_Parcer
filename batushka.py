import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
data = []
for p in range(1,94):
    url = f'https://www.velostrana.ru/velozapchasti/kolesa/{p}.html'
    host = 'https://www.velostrana.ru'
    res = requests.get(url)
    print(res.status_code)
    soup = BeautifulSoup(res.text, 'lxml')
    boxes = soup.find_all('div', class_='product-grid__item')
    print(p)
    sleep(1)
    for i in boxes:
        try:
            name = i.find('a', class_='product-card__title').find('div',class_='product-card__model').text
        except AttributeError:
            continue
        try:
            price = i.find('div', class_='product-card__pricebox-main').find('div', class_='product-card__price-new').text
        except AttributeError:
            print(0)
        stock = i.find('div', class_='product-card__pricebox-main').find('div',class_='product-card__instock').text.lstrip()
        html = i.find('a', class_='product-card__title').get('href')
        data.append([name, price, stock,html])
headers = ["name", 'price', "stock", 'html']
df = pd.DataFrame(data, columns=headers)
csv_name = 'vela_kolesa' + '.csv'
df.to_csv(csv_name)
print(len(data))












