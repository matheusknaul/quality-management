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
import time

pc_casa_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_casa_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
pc_trabalho_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_trabalho_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'

service = Service(executable_path = pc_trabalho_gecko)
options = Options()
options.binary_location = pc_trabalho_firefox
driver = webdriver.Firefox(service=service, options=options)

# Acesse uma URL
driver.get("https://www.google.com")

# Aguarde 5 segundos antes de fechar o navegador
time.sleep(5)

# Fecha o navegador
driver.quit()

print('O código continuou!')