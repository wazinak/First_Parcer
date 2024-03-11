
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=800,700")
options.add_argument("--disable-blink-features=AutomationConrtolled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.avito.ru/moskva/noutbuki?cd=1&q=macbook+pro+2023&s=104'
host = 'https://www.avito.ru'
data = []
def get_page():
    """фнкция загружает страницу"""
    driver.get(url)
    sleep(4)
    scroll_down()
    sleep(4)
    collect_data()
def page_next():
    """фнкция перелистывает на следующую страницу"""
    driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/'
                                      'div[3]/div[3]/div[4]/nav/ul/li[9]').click()
    sleep(5)
    scroll_down()
    sleep(3)
    collect_data()
def scroll_down():
    """Драйвер скролит вниз"""
    driver.execute_script("window. scrollBy(0, 13250)")
def collect_data():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    items = soup.find_all('div', class_='iva-item-content-rejJg')
    for item in items:
        name = item.find('h3',class_='styles-module-root-TWVKW styles-module-root-_'
                                     'KFFt styles-module-size_l-_oGDF styles-module-size_l_'
                                     'compensated-OK6a6 styles-module-size_l-hruVE styles-module-ellipsis-LKWy3'
                                     ' styles-module-weight_bold-Kpd5F stylesMarningNormal-module-root-OSCNq '
                                     'stylesMarningNormal-module-header-l-qvNIS').text
        price = item.find('div', class_='price-price-JP7qe').find_all('meta')[1].get('content')
        description = item.find('div',class_='iva-item-descriptionStep-C0ty1').text.strip()
        link = item.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
        data.append([name,price, description, host+link])
    sleep(2)
def main():
    get_page()
    page_next()
    page_next()

if __name__ == '__main__':
        main()