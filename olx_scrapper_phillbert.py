import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("start-maximalized")
url = 'https://www.olx.co.id/jakarta-selatan_g4000030/q-mobil'
driver = webdriver.Chrome()
driver.get(url)

for i in range(100):
    time.sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR, "div._38O09 > button").click()
        time.sleep(3)
    except NoSuchElementException:
        break
time.sleep(10)

products = []
soup = BeautifulSoup(driver.page_source, "html.parser")
for item in soup.find_all('li', class_='_1DNjI'):
    product_name = item.find('span', class_='_2poNJ').text
    price = item.find('span', class_='_2Ks63').text
    products.append((product_name, price))

df = pd.DataFrame(products, columns=['Product Name', 'Price'])
print(df)

df.to_csv(r'OLX Scrapper Phillbert.csv', index=False)
print('Data saved in local disk')

driver.quit()
