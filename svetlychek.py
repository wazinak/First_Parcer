
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

data = []
options = Options()
options.add_argument("--window-size=800,700")
options.add_argument("--disable-blink-features=AutomationConrtolled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.avito.ru'
driver.get(url)
sleep(5)
# driver.back()
# driver.forward()
# sleep(3)
# print('URL страницы:', driver.current_url)
# current_title = driver.title
# print('заголовок', current_title)
# print(driver.page_source)
input_tab = driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]')
input_tab.click()
sleep(2)
# input_tab.send_keys('macbook pro 2017')
# sleep(2)
# input_tab.send_keys(Keys.BACK_SPACE*20)
# sleep(2)
input_tab.send_keys('macbook pro 2023')
sleep(5)
poisk = driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/button')
poisk.click()
sleep(5)
nas_computer = driver.find_element('xpath','//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[1]/div/div[1]/ul/li[1]/ul/li[1]/div/div/div/div/div/a')
nas_computer.click()
sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # прокрутка до конца страницы
element = driver.find_element('xpath','//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)

sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
elements = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
pages = soup.find('a',class_='styles-module-item-kF45w styles-module-item_size_s-Tvz95 styles-module-item_last-vIJIa styles-module-item_link-_bV2N').find('span', class_='styles-module-text-InivV').text
pages = int(pages)
for p in range(pages+1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[9]'))).click()

    for i in elements:
        name = i.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('title')
        price = i.find('div', class_='price-price-JP7qe').find_all('meta')[1].get('content')
        description = i.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s_compensated-Wo8uc styles-module-size_s-_P6ZA styles-module-ellipsis-LKWy3 stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-noAccent-nZxz7 styles-module-root_bottom-XgXHc styles-module-margin-bottom_6-nU1Wp').text.strip()
        link = i.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
        data.append([name,price,description, url + link])
    sleep(5)

print(len(data))
headers = ["name", 'price', 'description', 'link']
df = pd.DataFrame(data, columns=headers)
csv_name = 'avito_macbookpro' + '.csv'
df.to_csv(csv_name)


