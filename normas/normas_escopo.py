from modelos.ModelaNorma import ModelaNorma as mn
import pandas as pd
from PyPDF2 import PdfReader
import re
from datetime import datetime

lista = ["ABNT NBR 15709 / 2016 ", "ABNT NBR 11568:2016", "ASTM F1044/ 2005", 'ASTM F512-3:2013', 'ABNT NBR ISO 15093 Partes 2 e 3:2013']
dados = []
lista_das_normas = ["ISO", "ABNT", "ASTM", "IEC", "NM"]
lista_obj_normas = []

df = pd.DataFrame({
            'TAG PRINCIPAL':[],
            'Numero': [],
            'Descrição': [],
            'Parte': [],
            'Ano': [],
            'Status': [],
            'Data ultima verificacao': [],
            'Erro status': [],
            'Link': []
        })

def nova_linha(obj, data_frame): 
    nova_linha = obj.registra_norma()
    data_frame.loc[len(data_frame)] = nova_linha

def verifica_duplicata(obj, data_frame):
    for indice, linha in data_frame.iterrows():
        if linha['TAG PRINCIPAL'] == obj.tag and linha['Numero'] == obj.numero and linha['Parte'] == obj.partes and linha['Ano'] == obj.data:
            return False
    return True
            
def procura_norma():
    padrao = r"(" + "|".join(lista_das_normas) + r")"
    indice_item = 1
    with open('normas\escopo\CRL0495.pdf','rb') as f:
        pdf = PdfReader(f)
        num_pages = len(pdf.pages)
        lines = []
        for page in pdf.pages:
            page_text = page.extract_text()
            lines += page_text.split('\n')
        for i, line in enumerate(lines):
            match = re.search(padrao, line)
            if match:
                palavra = match.group(1)
                if i < len(lines) -1:
                    proxima_linha = lines[i + 1]
                    texto_completo = f"{line} {proxima_linha}"
                else:
                    texto_completo = line
                
                obj = mn(texto_completo)
                if verifica_duplicata(obj, df):
                    nova_linha(obj, df)
    df.to_excel('normas/db_excel/dataframe.xlsx', index=False)

start_time = datetime.now()
procura_norma()

print('Salvado com sucesso!')
elapsed_time = datetime.now() - start_time
print('Elapsed time: ', elapsed_time)

