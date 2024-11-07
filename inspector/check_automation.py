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
from data_sync import __setData__


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

#[tag_norma, numero_norma, parte_norma, ano_norma]

# Seção do checkbox

"""
    Para analisar os resultados, o mais ideal, é analisar cada card de resultado que o site irá gerar para nós.
    No entanto, o site da ABNT CATALOGO tem várias variáveis para demonstrar os resultados que, não valerá a pena levantar
    todas elas.

    Por isso, fui obrigado a fazer um laço indefinido, onde o range não terá rastreio em nenhum variável e ele só irá
    parar a execução quando achar o "melhor resultado" ou, quando acabar a aparições dos resultados.

    Neste caso, o "melhor resultado", é aquele que está incluso o número da norma e a sua parte (isso significa que é
    o resultado ideal).
"""

def iec_check(driver, norma_info):
    print('usou a IEC')
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[4]/label').click()
    time.sleep(2)
    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(norma_info[2])
    time.sleep(1)
    # Parte da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(norma_info[3])
    time.sleep(1)
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
    time.sleep(2)

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)

    if norma_info[3] != 'null':
        verificacao = norma_info[2] + '-' + norma_info[3]
    else:
        verificacao = norma_info[2]
    print(f'Esse é o verificação da ISO: {verificacao}')
    for resultado in range(999):
        cardResult = soup.find('div', id=f'cphPagina_rptLista_pnlProduto_{resultado}')
        if cardResult:
            h2 = cardResult.find('h2')
            link = h2.find('a')
            print(f'Esse aqui é o h2: {h2}')
            if verificacao in h2.text:
                driver.find_element(By.ID, f'{link.get('id')}').click()
                time.sleep(2)
                break
    time.sleep(1)
    titulo_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaNumero"]').text

    if norma_info[4] != 'null':
        verificacao = verificacao + ":" + str(norma_info[4])
        print(f'verificação com ano: {verificacao}')

    status_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaStatus"]').text

    if status_resultado == "EM VIGOR":
        status_norma = "Conforme"
    else:
        status_norma = "Não conforme"
    if verificacao in titulo_resultado:
        codigo_norma = titulo_resultado
    else:
        status_norma = "Não conforme"

    descricao_norma = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaTitulo"]').text
    
    #entry = [id, tag, numero, parte, ano]
    #[id_norma, codigo_norma, descricao_norma, status]

    link = driver.current_url

    return [norma_info[0], codigo_norma, descricao_norma, status_norma, link]

def iso_check(driver, norma_info):

    # Seção do checkbox

    print('usou a ISO')
    driver.find_element(By.CSS_SELECTOR, '#cphPagina_pnlNorma > div > div:nth-child(1) > div:nth-child(5) > label').click()
    time.sleep(2)

    # Seção de preencher as informações da norma

    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(norma_info[2])
    time.sleep(1)
    # Parte da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(norma_info[3])
    time.sleep(1)
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
    time.sleep(2)

    # Seção dos resultados
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)

    if norma_info[3] != 'null':
        verificacao = norma_info[2] + '-' + norma_info[3]
    else:
        verificacao = norma_info[2]
    print(f'Esse é o verificação da ISO: {verificacao}')
    for resultado in range(999):
        cardResult = soup.find('div', id=f'cphPagina_rptLista_pnlProduto_{resultado}')
        if cardResult:
            h2 = cardResult.find('h2')
            link = h2.find('a')
            print(f'Esse aqui é o h2: {h2}')
            if verificacao in h2.text:
                driver.find_element(By.ID, f'{link.get('id')}').click()
                time.sleep(2)
                break

    # Seção do perfil
    time.sleep(1)
    titulo_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaNumero"]').text

    if norma_info[4] != 'null':
        verificacao = verificacao + ":" + str(norma_info[4])
        print(f'verificação com ano: {verificacao}')

    status_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaStatus"]').text

    if status_resultado == "EM VIGOR":
        status_norma = "Conforme"
    else:
        status_norma = "Não conforme"
    if verificacao in titulo_resultado:
        codigo_norma = titulo_resultado
    else:
        status_norma = "Não conforme"

    descricao_norma = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaTitulo"]').text
    
    #entry = [id, tag, numero, parte, ano]
    #[id_norma, codigo_norma, descricao_norma, status]

    link = driver.current_url

    return [norma_info[0], codigo_norma, descricao_norma, status_norma, link]


def astm_check(driver, norma_info):

    # Seção do checkbox

    print('usou a ASTM')
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[11]/label').click()
    time.sleep(2)

    # Seção de preencher os resultados

    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_NumeroUnico"]').send_keys(norma_info[2])
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
    time.sleep(2)

    # Seção dos resultados

    #entry = [id, tag, numero, parte, ano]
    #[id_norma, codigo_norma, descricao_norma, status]
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    if norma_info[3] != 'null':
        verificacao = norma_info[2] + '-' + norma_info[3]
    else:
        verificacao = norma_info[2]
    for resultado in range(999):
        cardResult = soup.find('div', id=f'cphPagina_rptLista_pnlProduto_{resultado}')
        if cardResult:
            h2 = cardResult.find('h2')
            link = h2.find('a')
            print(f'Esse aqui é o h2: {h2}')
            if verificacao in h2.text:
                driver.find_element(By.ID, f'{link.get('id')}').click()
                time.sleep(2)
                break

    # Seção do perfil
    time.sleep(1)
    titulo_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaNumero"]').text

    if norma_info[4] != 'null':
        ano_astm = str(norma_info[4])
        verificacao = verificacao + ":" + ano_astm[2:]
        print(f'astm com ano formatado: {verificacao}')

    status_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaStatus"]').text
    if status_resultado == "EM VIGOR":
        status_norma =  "Conforme"
    else:
        status_norma = "Não conforme"
    
    if verificacao in titulo_resultado:
        codigo_norma = titulo_resultado
    else:
        codigo_norma = titulo_resultado
        status_norma = "Não conforme"
        
    descricao_norma = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaTitulo"]').text

    link = driver.current_url

    return [norma_info[0], codigo_norma, descricao_norma, status_norma, link]

def abnt_check(driver, norma_info):

    # Seção do checkbox

    print('usou a ABNT')
    driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()
    time.sleep(2)

    # Seção de preencher os resultados

    # Número da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(norma_info[2])
    # Parte da norma
    driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Parte"]').send_keys(norma_info[3])
    # Scroll pra baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Botão de pesquisar
    driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
    time.sleep(3)

    # Seção dos resultados
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)

    print(f'Essa é a parte da norma: {norma_info[3]}')
    if norma_info[3] != 'null':
        verificacao = norma_info[2] + "-" + norma_info[3]
    else:
        verificacao = norma_info[2]
    print(f'Esse foi o fruto do verificacao: {verificacao}')
    #[tag_norma, numero_norma, parte_norma, ano_norma]
    for resultado in range(999):
        cardResult = soup.find('div', id=f'cphPagina_rptLista_pnlProduto_{resultado}')
        if cardResult:
            h2 = cardResult.find('h2')
            link = h2.find('a')
            print(f'Esse aqui é o h2: {h2}')
            if verificacao in h2.text:
                driver.find_element(By.ID, f'{link.get('id')}').click()
                time.sleep(2)
                break
    
    # Seção do perfil

    time.sleep(1)
    titulo_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaNumero"]').text

    if norma_info[4] != 'null':
        verificacao = verificacao + ":" + str(norma_info[4])
        print(f'verificação com ano: {verificacao}')

    status_resultado = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaStatus"]').text

    if status_resultado == "EM VIGOR":
        status_norma = "Conforme"
    else:
        status_norma = "Não conforme"
    if verificacao in titulo_resultado:
        codigo_norma = titulo_resultado
    else:
        status_norma = "Não conforme"

    descricao_norma = driver.find_element('xpath', '//*[@id="cphPagina_lblNormaTitulo"]').text
    
    #entry = [id, tag, numero, parte, ano]
    #[id_norma, codigo_norma, descricao_norma, status]

    link = driver.current_url

    return [norma_info[0], codigo_norma, descricao_norma, status_norma, link]
    
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
    check_norma = {
        'ASTM': astm_check,
        'ABNT': abnt_check,
        'ISO': iso_check,
    }
    try:
        resultado = check_norma[tag_norma](driver, [id_norma, tag_norma, numero_norma, parte_norma, ano_norma])

        __setData__(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
    except Exception as e:
        __setData__(id_norma, tag_norma + " " + numero_norma, "", "Error", "")
    time.sleep(1)

    driver.quit()
    print('Drive finalizado')