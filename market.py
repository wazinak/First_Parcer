
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

data = []
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=700,700")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})
host = 'https://market.yandex.ru'
url = 'https://market.yandex.ru/catalog--korma-dlia-koshek/73690/list?hid=15685457&promo-type=market'
driver.get(url)
sleep(3)
sale = driver.find_element('xpath','//*[@id="serpTop"]/div/div/div[1]/div/div/noindex/div/button[4]')
sale.click()
sleep(3)
knopka = driver.find_element('xpath', '//*[@id="searchFilters"]/div/div[3]/div/div/div/div/div[4]/div/fieldset/div/div/div[2]')
knopka.click()
sleep(3)
poisk = driver.find_element('xpath', '//*[@id="searchFilters"]/div/div[3]/div/div/div/div/div[4]/div/fieldset/div/div/div[1]')
poisk.click()
perfict_fit = driver.find_element('xpath', '//*[@id="searchFilters"]/div/div[3]/div/div/div/div/div[4]/div/fieldset/div/div/div[2]/div/div/div/div/div/div[14]')
perfict_fit.click()
sleep(5)
# driver.execute_script("window. scrollBy(0, 2800)")
# #driver.save_screenshot('screenshot.png')
# sleep(5)
# next_page = driver.find_element('xpath', '/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[5]/div/div/div/div/div/div/div/div[7]/div/div/div[2]/div/div[4]/div')
# next_page.click()
soup = BeautifulSoup(driver.page_source, 'lxml')
corma = soup.find_all('div', class_='_2im8- _2S9MU _2jRxX')
data = []
for p in range(3):
    print(p)
    driver.execute_script("window. scrollBy(0, 2550)")
    sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[5]/div/div/div/div/div/div/div/div[7]/div/div/div[1]/div/button'))).click()

    for corm in corma:
        name = corm.find('span', class_='_1E10J _2o124 _3VXOR').text
        link = corm.find('a').get('href')
        sale = corm.find('span', class_='_1oI3I').text
        data.append([sale, name, link])

print(len(data))
headers = ["sale", 'name', 'link']
df = pd.DataFrame(data, columns=headers)
csv_name = 'corm_cat' + '.csv'
df.to_csv(csv_name)

