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
import sys
import os
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

pc_casa_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_casa_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
pc_trabalho_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_trabalho_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'

link_abnt = 'https://www.abntcatalogo.com.br/pav.aspx'

service = Service(executable_path = pc_trabalho_gecko)
options = Options()
options.binary_location = pc_trabalho_firefox

abnt_catalogo = requests.get(link_abnt)
html = abnt_catalogo.text

# Seção do checkbox
def iso_checkbox(driver):
    print('usou a ISO')
    driver.find_element(By.CSS_SELECTOR, '#cphPagina_pnlNorma > div > div:nth-child(1) > div:nth-child(5) > label').click()

def astm_checkbox(driver):
    print('usou a ASTM')
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[11]/label').click()

def abnt_checkbox(driver):
    print('usou a ABNT')
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()

# Seção do preenchimento
#[tag_norma, numero_norma, parte_norma, ano_norma]

def iso_fill(driver, norma_info):
    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(norma_info[1])
    # Parte da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(norma_info[2])
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()

def astm_fill(driver, norma_info):
    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_NumeroUnico"]').send_keys(norma_info[1])
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()

def abnt_fill(driver, norma_info):
    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(norma_info[1])
    # Parte da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(norma_info[2])
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()

# Seção dos resultados

# Seção do perfil

def __main__(list):
    track_list(list)

def track_list(list):
    for element in list:
        print(element)
        search_norma(element[0], element[1], element[2], element[3], element[4])

def search_norma(id_norma, tag_norma, numero_norma, parte_norma, ano_norma):
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(link_abnt)
    time.sleep(3)
    """
    Desmarcar a tag ABNT que vem marcada por padrão.
    """
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()
    time.sleep(2)
    """ 
    Parte do search para marcar o checkbox.
    """
    valid_checkbox = {
        'ASTM': astm_checkbox,
        'ABNT': abnt_checkbox,
        'ISO': iso_checkbox,
    }
       
    valid_checkbox[tag_norma](driver)
    time.sleep(3)

    """ 
    Parte do preenchimento das informações da norma.
    """
    norma_fill = {
        'ASTM': astm_fill,
        'ABNT': abnt_fill,
        'ISO': iso_fill
    }

    norma_fill[tag_norma](driver, [tag_norma, numero_norma, parte_norma, ano_norma])
    time.sleep(5)

    driver.quit()
    print('Drive finalizado')