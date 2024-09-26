import pandas as pd
import time
from datetime import date
import numpy as np
from pandas._libs.tslibs.nattype import NaTType
from Data import Data

_path_db = 'normas/db_excel/dataframe.xlsx'
_date = Data()
_data_frame = pd.read_excel(_path_db)
_period_valid = 14
_cover_result = {
        'Status': [],
        'Data ultima verificacao': [],
        'Erro status': []
}

"""

AVISOS:

ALGUM MOMENTO, VAI COMEÇAR A DAR CRASH POIS O LIMPA CHECKBOX DE CADA VERIFICAÇÃO
NÃO POSSUI O XPATH DA ISO PARA PODER VERIFICAR E LIMPAR!

"""

def start_read():
    for indice, linha in _data_frame.iterrows():
        if verify_year_nan(linha['Ano']):
            if need_verify(linha['Status'], linha['Data ultima verificacao']):
                if linha['TAG PRINCIPAL'] == 'ABNT':
                    start_aplication_ABNT(linha['TAG PRINCIPAL'], linha['Numero'], treat_year(linha['Ano']), treat_part(linha['Parte']), indice)
                elif linha['TAG PRINCIPAL'] == 'ASTM':
                    start_aplication_ASTM(linha['TAG PRINCIPAL'], linha['Numero'], treat_year(linha['Ano']), indice)
                    #start_aplication_ASTM
                elif linha['TAG PRINCIPAL'] == 'ISO':
                    start_aplication_ISO(linha['TAG PRINCIPAL'], linha['Numero'], treat_year(linha['Ano']), treat_part(linha['Parte']), indice)
                    #start_aplication_ISO
                else:
                    cover_result('erro status', "Don't have any tag that as verificate")
        else:
            print('Ano é NaN, por isso não será verificado!')

def treat_year(data):
    #this function just change the type of data (that is possible is float) to str.
    return str(int(data))

def treat_part(data):
    if verify_part_nan(data):
        return None
    else: 
        return str(int(data))

def need_verify(status, date):
    if status == 'Analisar':
        return True
    elif verify_frequency(_date.data_numero(date)):
        return True
    else:
        return False

def verify_frequency(date):
    today = _date.data_hoje_numero()
    if today > (date + _period_valid):
        #the frequency has been decide for "14", but you can change.
        return True
    else:
        return False

def verify_max_date(date):
    if verify_type(date) == str:
        if verify_frequency(date):
            return True
        else:
            return False
    else:
        if verify_frequency(date):
            return True
        else:
            return False

def verify_type(data):
    return type(data)

def verify_year_nan(year): 
    if pd.isnull(year):
        cover_result('erro status', 'Não foi possível verificar, pois não possui ANO')
        return False
    else:
        return True

def verify_part_nan(part): 
    if pd.isnull(part):
        cover_result('erro status', 'Não foi possível verificar, pois não possui ANO')
        return True
    else:
        return False

def cover_result(column, message):
    print(column, message)

def start_aplication_ISO(tag, number, year, part, indice):
    #can be refatored
    from analys_ISO import main
    result = main(tag, number, year, part)
    if result['RESULTADO'] == 'ATIVA':
        _data_frame.at[indice, 'Status'] = 'Conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    elif result['RESULTADO'] == 'ERROR':
        _data_frame.at[indice, 'Status'] = 'Analisar'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Erro status'] = result['WARNING']
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    else:
        _data_frame.at[indice, 'Status'] = 'Não conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    if result['WARNING'] == 'Parte não está presente':
        _data_frame.at[indice, 'Erro status'] = 'Problema na parte'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)

def start_aplication_ABNT(tag, number, year, part, indice):
    #can be refatored
    from analys_ABNT import busca_norma
    result = busca_norma(tag, number, year, part)
    if result['RESULTADO'] == 'ATIVA':
        _data_frame.at[indice, 'Status'] = 'Conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    elif result['RESULTADO'] == 'ERROR':
        _data_frame.at[indice, 'Status'] = 'Analisar'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Erro status'] = result['WARNING']
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    else:
        _data_frame.at[indice, 'Status'] = 'Não conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    if result['WARNING'] == 'Parte não está presente':
        _data_frame.at[indice, 'Erro status'] = 'Problema na parte'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)

def start_aplication_ASTM(tag, number, year, indice):
    #can be refatored
    from analys_ASTM import main
    result = main(tag, number, year)
    if result['RESULTADO'] == 'ATIVA':
        _data_frame.at[indice, 'Status'] = 'Conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    elif result['RESULTADO'] == 'ERROR':
        _data_frame.at[indice, 'Status'] = 'Analisar'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Erro status'] = result['WARNING']
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    else:
        _data_frame.at[indice, 'Status'] = 'Não conforme'
        _data_frame.at[indice, 'Data ultima verificacao'] = f'{_date.data_hoje()}'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)
    if result['WARNING'] == 'Parte não está presente':
        _data_frame.at[indice, 'Erro status'] = 'Problema na parte'
        _data_frame.at[indice, 'Link'] = result['LINK']
        _data_frame.at[indice, 'Descrição'] = result['DESCRIPTION']
        _data_frame.to_excel('dataframe.xlsx',index=False)
        _data_frame.to_excel(r'C:\Users\matheus.calvet\Desktop\teste\dataframe.xlsx', index=False)

def correct_year(year):
    if type(year) != str or type(year) != int or type(year) != float:
        return None
    if type(year) == float:
        new_ano = int(year)
        return str(new_ano)
    if type(year) == int:
        return str(year)

def __loop__():
    try:
        start_read()
    except:
        start_read()

__loop__()
