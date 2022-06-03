from email import header
from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

driver  = webdriver.Firefox(executable_path='F:\\Projects\\COVID-19Scrapper\\webscrape\\geckodriver-v0.31.0-win64\\geckodriver.exe')

driver.get('https://www.covid19india.org/')

timeout = 10
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "level-vaccinated")))
except:
    driver.quit()

table_data = driver.find_element(By.CLASS_NAME, "Table").text
table_list = table_data.split('\n')
up_arrow = chr(8593)
down_arrow = chr(8595)

for x in table_list:
    for y in range(len(x)):
        i = x[y]
        if i==up_arrow:
            table_list.remove(x)
        if i==down_arrow:
            table_list.remove(x)

total_rows = (len(table_list)-2)/7
print(total_rows)

data = []

i = 2
j = 9
num_row = 0
count = 9
while num_row<total_rows:
    temp_list = []
    while i<j:
        temp_list.append(table_list[i])
        i += 1
        count += 1

    data.append(temp_list)
    j = count
    num_row += 1


df = pd.DataFrame(data, header=True)
print(df)
df.to_csv('covid-data.csv')
driver.quit()

        