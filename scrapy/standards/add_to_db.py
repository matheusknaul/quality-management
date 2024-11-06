from standard_features import build_standard
from separate_text import __separate__
from openpyxl import load_workbook
from peewee import fn

workbook = load_workbook('scrapy/tabela_ensaio.xlsx')
worksheet = workbook['Sheet']

lista = []
for cell in worksheet['B']:
    if cell.value:
        lista.append(__separate__(cell.value))

# for item in lista:
#     if item:
#         print(item)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from types import NoneType
from database.models.norma import Norma

# class Norma(BaseModel):
#     codigo = CharField()
#     descricao = CharField()
#     ano_norma = IntegerField()
#     situacao = CharField()
#     data_ultima_verificacao = DateTimeField(default=datetime.datetime.now)
#     tag_main = CharField()
#     part_main = CharField()
#     number_main = CharField()
#     link = CharField()

for item in lista:
    if item:
        print(item, f'your len: {len(item)}')
        if len(item) > 1:
            for element in item:
                if len(element) > 2:
                    for indice in range(len(element)):
                else:
                    Norma.create
        else: 
            for number_element in range(len(item)):
                print(item[number_element], "aaaaaaaaaaaaaaaaaaaaa", item[number_element])
                new_codigo_norma = item[number_element][1]
                Norma.create(codigo = new_codigo_norma, descricao="", ano_norma=item[number_element][0][2], situacao="Analisar", tag_main=item[number_element][0][0], part_main=item[number_element][0][3], number_main=item[number_element][0][1], link="")
        else:
            new_codigo_norma = item[0][1]
            Norma.create(codigo = new_codigo_norma, descricao="", ano_norma=item[0][0][2], situacao="Analisar", tag_main=item[0][0][0], part_main=item[0][0][3], number_main=item[0][0][1], link="")








# from types import NoneType
# from database.models.norma import Norma

# new_norma = Norma.create(codigo=new_codigo_norma, descricao='', ano_norma=ano_da_norma, situacao=status, tag_main=tag_norma, part_main=primeira_parte, number_main=number_norma)
# print(f"esse daqui é a lista de partes após o pop{partes}")
