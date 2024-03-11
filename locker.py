import requests
from bs4 import BeautifulSoup

url = 'https://www.velostrana.ru/velozapchasti/kolesa/'
response = requests.get(url)
#print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all("div", class_="product-card__model")
price = soup.find_all('div', class_='product-card__price-new')
#links = soup.find('div', class_='product-card__body').find('a', class_='product-card__title').get('href')
all = soup.find_all('div', class_='page__content')
for i in range(0,len(name)):
    print(name[i].text + ' :  ' + price[i].text)
