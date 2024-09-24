from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pandas._libs.tslibs.nattype import NaTType
from bs4 import BeautifulSoup
import requests
import time

pc_casa_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_casa_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
pc_trabalho_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_trabalho_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'

link_abnt = 'https://www.abntcatalogo.com.br/pav.aspx'

service = Service(executable_path = pc_trabalho_gecko)
options = Options()
options.binary_location = pc_trabalho_firefox
driver = webdriver.Firefox(service=service, options=options)

driver.get(link_abnt)
time.sleep(10)

with open("abnt.txt", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

driver.find_element('xpath', '//*[@id="cphPagina_pnlNorma"]/div/div[1]/div[2]/label').click()
time.sleep(5)
driver.find_element('xpath', '//*[@id="cphPagina_pnlNorma"]/div/div[1]/div[11]/label').click()
time.sleep(5)

with open('astm.txt', 'w', encoding="utf-8") as file:
    file.write(driver.page_source)

driver.find_element('xpath', '//*[@id="cphPagina_pnlNorma"]/div/div[1]/div[11]/label').click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, '#cphPagina_pnlNorma > div > div:nth-child(1) > div:nth-child(5) > label').click()
time.sleep(5)

with open('iso.txt', 'w', encoding="utf-8") as file:
    file.write(driver.page_source)