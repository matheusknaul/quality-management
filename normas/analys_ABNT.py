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



class DontHaveYear(Exception):
    print('Não tem ano!')

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


#Limpar a tag do ISO também!!
def clear_checkbox(tag):
    driver.get(link_abnt)
    time.sleep(10)

    from analys_checkbox import search_checkbox

    tags = search_checkbox(driver.page_source, tag)
    print(tags)
    if tags['ABNT']:
        print('true 1')
        driver.find_element('xpath', xpath_checkbox['abnt']).click()
        time.sleep(5)
    if tags['ASTM']:
        print('true 2')
        driver.find_element('xpath', xpath_checkbox['astm']).click()
        time.sleep(5)
    if tags['ISO']:
        print('true 3')
        driver.find_element(By.CSS_SELECTOR, '#cphPagina_pnlNorma > div > div:nth-child(1) > div:nth-child(5) > label').click()
        time.sleep(5)        
    return True

def pega_titulo():
    titulo = driver.find_element(By.ID, '#cphPagina_lblNormaTitulo').text
    return titulo

def selecionar_tag(tag):
    time.sleep(2)
    from analys_checkbox import confirm_checkbox
    if confirm_checkbox(driver.page_source, tag):
        driver.find_element('xpath',xpath_checkbox[f'{tag}'.lower()]).click()
    return tag

def adicionar_numero(numero):
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(numero)
    time.sleep(5)
    return numero

def adicionar_parte(parte):
    if parte:
        driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(parte)
    return parte

def analisa_resultado(tag, numero, ano, parte):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source)

        with open("lista_resultado.txt", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        titulo_link = []
        for h2 in soup.find_all('h2'):
            if tag in h2.string and numero in h2.string:
                #A tag e o número estão aqui
                #print(h2.a)
                #print(h2.a.get('id'))
                titulo_link.append(h2.a)
            
        driver.find_element(By.ID, titulo_link[0].get('id')).click()
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source)

        with open("perfil_normal.txt", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        titulo_norma = soup.h2.string
        if tag in titulo_norma and numero in titulo_norma and ano in titulo_norma:
            #A tag e o número estão dentro do titulo do perfil
            result['DESCRIPTION'] = soup.find('span', id='cphPagina_lblNormaTitulo').string
            print(f'Essa é a descrição da norma: {soup.find('span', id='cphPagina_lblNormaTitulo').string}')
            if soup.find('span', id='cphPagina_lblNormaStatus').string == 'ACTIVE' or "EM VIGOR":
                #Ela está ativa
                result['RESULTADO'] = 'ATIVA'
                url_atual = driver.current_url
                print(parte)
                if parte:
                    if parte in titulo_norma:
                                    #Tem parte e ela está presente no titulo
                        result['WARNING'] = 'OK'
                    else:
                                    #Possui parte, mas não está presente no titulo
                        result['WARNING'] = 'Parte não está presente'
                else:
                        #Não possui parte
                    result['WARNING'] = 'OK'
            else:
                    #Não está ativa.
                result['RESULTADO'] = 'DESATIVADA'
                url_atual = driver.current_url
        else:
                #Alguns componentes avaliados não estão de acordo
            pass
        result['LINK'] = driver.current_url
    except Exception as e:
                #Provavelmente algum erro com a norma escrita no data frame
                result['RESULTADO'] = 'ERROR'
                result['WARNING'] = f'ERROR: {e}'

def busca_norma(tag, number, year, parte=None):
    if clear_checkbox(tag):
        analisa_resultado(selecionar_tag(tag), adicionar_numero(number), year, adicionar_parte(parte))
    return result


busca_norma('ABNT', '17025','2017')

#span.id = cphPagina_lblNormaNumero (perfil da norma/titulo)
#span.id = cphPagina_lblNormaStatus (perfil da norma/status)

#h2.a.id = cphPagina_rptLista_cmdCodigo_{indice} (lista de resultado/titulo norma) o que estamos buscando geralmente é o primeiro da lista, ou seja, cphPagina_rptLista_cmdCodigo_0

#span.id = cphPagina_lblPesquisa2Contador = quantidade de resultados para produtos ABNT, teria que dar um .string para obter tudo.