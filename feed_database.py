from types import NoneType
from database.models.norma import Norma

"""
Esse código serve, caso você precise adicionar registros no banco de dados no shell.

"""

# class Norma(BaseModel):
#     codigo = CharField()
#     descricao = CharField()
#     ano_norma = IntegerField()
#     situacao = CharField()
#     data_ultima_verificacao = DateTimeField(default=datetime.datetime.now)

# for i in range(10):
#     new_norma = Norma.create(codigo='ABNT NBR 7206', descricao='Implantes cirurgicos', ano_norma=2013, situacao='Conforme')

""" 
Para adicionar registros com base em leitura no excel, usaremos o openpyxl.
"""

from openpyxl import load_workbook
import openpyxl
import re

_dataframepath_ = 'dataframe.xlsx'

def get_dado_excel(planilha_excel):
    wb = load_workbook(planilha_excel)
    sheet = wb['Sheet1']

    total_linhas = sheet.max_row

    next_linha = []
    for row in range(2, total_linhas + 1):
        print(f'número da linha {row}')
        codigo_norma = str(sheet[f'A{row}'].value) + " " + str(sheet[f'B{row}'].value)
        ano_da_norma = sheet[f'E{row}'].value
        if not ano_da_norma:
            ano_da_norma = 1
        status = sheet[f'F{row}'].value
        partes_da_norma = sheet[f'D{row}'].value #talvez mudar
        if partes_da_norma:
            partes = re.findall(r'\d', sheet[f'D{row}'].value)
            print(f"esse daqui é a lista de partes gerada do findall{partes}")
            while partes:
                primeira_parte = partes.pop(0)
                new_codigo_norma = codigo_norma + "-" + primeira_parte
                new_norma = Norma.create(codigo=new_codigo_norma, descricao='', ano_norma=ano_da_norma, situacao=status)
                print(f"esse daqui é a lista de partes após o pop{partes}")
        else:
            new_norma = Norma.create(codigo=codigo_norma, descricao='', ano_norma=ano_da_norma, situacao=status)

get_dado_excel(_dataframepath_)