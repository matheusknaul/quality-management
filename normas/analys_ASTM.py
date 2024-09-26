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

class NoInputNumber(Exception):
    def __init__(self, message='Não foi possível enviar a key do número'):
        self.message = message
        super().__init__(self.message)

class NoButtonClicker(Exception):
    def __init__(self, message='Não foi possivel clicar no botão'):
        self.message = message
        super().__init__(self.message)

class NoSelectTag(Exception):
    def __init__(self, message='Não foi possivel selecionar a tag'):
        self.message = message
        super().__init__(self.message)

pc_casa_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_casa_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
pc_trabalho_gecko = r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python312\geckodriver.exe'
pc_trabalho_firefox = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'

link_abnt = 'https://www.abntcatalogo.com.br/pav.aspx'

xpath_checkbox = {
    'abnt': '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label',
    'astm': '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[11]/label'
}

result = {
    'RESULTADO': '',
    'DESCRIPTION': '',
    'WARNING': ''
}

service = Service(executable_path = pc_trabalho_gecko)
options = Options()
options.binary_location = pc_trabalho_firefox
driver = webdriver.Firefox(service=service, options=options)

abnt_catalogo = requests.get(link_abnt)
html = abnt_catalogo.text

soup = BeautifulSoup(html)

def page_source(archive_name):    
    soup = BeautifulSoup(driver.page_source)
    with open(archive_name, "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    return driver.page_source

def add_number(number_of_standard):
    # try:
    #     driver.find_element(By.ID, 'ctl00_cphPagina_txtNM_NumeroUnico_ClientState').send_keys(number_of_standard)
    # except NoInputNumber as e:
    #     print(f'Ocorreu um erro: {e.message}')
    # return number_of_standard
    time.sleep(5)
    page_source('analise_ASTM')
    driver.find_element(By.CSS_SELECTOR, '#ctl00_cphPagina_txtNM_NumeroUnico').send_keys(number_of_standard)
    time.sleep(5)
    return number_of_standard

def select_tag(tag_of_standard):
    time.sleep(2)
    from analys_checkbox import confirm_checkbox
    if confirm_checkbox(driver.page_source, tag_of_standard):
        driver.find_element('xpath',xpath_checkbox[f'{tag_of_standard}'.lower()]).click()
    return tag_of_standard

#Limpar a tag do ISO também!!
def clear_checkbox(tag):
    driver.get(link_abnt)
    time.sleep(10)

    from analys_checkbox import search_checkbox

    tags = search_checkbox(driver.page_source, tag)
    print(tags)
    if tags['ABNT']:
        driver.find_element('xpath', xpath_checkbox['abnt']).click()
        time.sleep(5)
    if tags['ASTM']:
        driver.find_element('xpath', xpath_checkbox['astm']).click()
        time.sleep(5)
    if tags['ISO']:
        driver.find_element(By.CSS_SELECTOR, '#cphPagina_pnlNorma > div > div:nth-child(1) > div:nth-child(5) > label').click()
        time.sleep(5)        
    return True
    

def start_search(tag, number, year):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
        time.sleep(10)
    except NoButtonClicker as e:
        print(f'Ocorreu um erro: {e.message}')
    return page_source('result_list_ASTM.txt')

def analys_result_of_list(tag, number, year, html_of_page_contain_list):
    #html_of_page_contain_list = page.source
    soup = BeautifulSoup(html_of_page_contain_list)
    titulo_link = []
    for h2 in soup.find_all('h2'):
        if tag in h2.string and number in h2.string:
                #A tag e o número estão aqui
                #print(h2.a)
                #print(h2.a.get('id'))
            titulo_link.append(h2.a)    
    driver.find_element(By.ID, titulo_link[0].get('id')).click()
    time.sleep(10)
    html = driver.page_source
    page_source('analys_profile')
    return analys_profile(tag, number, year, html)

def analys_profile(tag, number, year, html_of_page_profile_standard):
    #html_of_page_contain_list = page.source
    soup = BeautifulSoup(html_of_page_profile_standard)
    titulo_norma = soup.h2.string
    year_detailed = year[-2:]
    if tag in titulo_norma and number in titulo_norma and year_detailed == titulo_norma[-2:]:
        #A tag e o número estão dentro do titulo do perfil
        result['DESCRIPTION'] = soup.find('span', id='cphPagina_lblNormaTitulo').string
        print(f'Essa é a descrição da norma: {soup.find('span', id='cphPagina_lblNormaTitulo').string}')
        if soup.find('span', id='cphPagina_lblNormaStatus').string == 'ACTIVE' or "EM VIGOR":
            #Ela está ativa
            result['RESULTADO'] = 'ATIVA'
            result['WARNING'] = 'OK'
            url_atual = driver.current_url
        else:
                #Não está ativa.
            result['RESULTADO'] = 'DESATIVADA'
            url_atual = driver.current_url
    else:
        #Alguns componentes avaliados não estão de acordo
        pass
    result['LINK'] = driver.current_url

def main(tag, number, year):
    if clear_checkbox(tag): 
        list_of_result = start_search(select_tag(tag), add_number(number), year)
        analys_result_of_list(tag, number, year, list_of_result)
    return result
