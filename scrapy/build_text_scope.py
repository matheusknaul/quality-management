import re
from PyPDF2 import PdfReader

"""
Esse arquivo junta o texto de todas as páginas e junta em uma só string.

Ele também remove blocos padrões de texto que se repetem na string.
"""

#finalizado

def __build_text__(pdf):
    builded_text = concatena_paginas(pega_texto_pdf(pdf))
    return builded_text

def remove_text(original_text, remove_block):
    return original_text.replace(remove_block, '')

def concatena_paginas(lista_de_paginas):
    """Essa função pega todos os itens da lista (lista de páginas) e concatena e uma string, ou seja
    em um único texto.

    Args:
        lista_de_paginas (list): lista das páginas

    Returns:
        string: Texto total do pdf.
    """
    lista_de_paginas_concatenadas = ''
    for item in range(len(lista_de_paginas)):
        new_pagina = remove_text(lista_de_paginas[item], f'ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - ENSAIO  Norma de Origem: NIT-DICLA-016 Folha: {item+1}   FOR-CGCRE- 003 – Rev. 12 – Publicado Set/19 – Pg. 0{item+1} /06  ACREDITAÇÃO N  TIPO DE INSTALAÇÃO CRL 0495  INSTALAÇÃO PERMANENTE ÁREA DE ATIVIDADE / PRODUTO CLASSE DE ENSAIO / DESCRIÇÃO DO ENSAIO NORMA E /OU PROCEDIMENTO')
        new_pagina_1 = remove_text(new_pagina, f'ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - ENSAIO  Norma de Origem: NIT-DICLA-016 Folha: {item+1}   FOR-CGCRE- 003 – Rev. 12 – Publicado Set/19 – Pg. {item+1} /06  ACREDITAÇÃO N  TIPO DE INSTALAÇÃO CRL 0495  INSTALAÇÃO PERMANENTE ÁREA DE ATIVIDADE / PRODUTO CLASSE DE ENSAIO / DESCRIÇÃO DO ENSAIO NORMA E /OU PROCEDIMENTO')
        new_pagina_2 = remove_text(new_pagina_1, f'ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - ENSAIO  Norma de Origem: NIT-DICLA-016 Folha: {item+1}   FOR-CGCRE- 003 – Rev. 12 – Publicado Set/19 – Pg. 0 {item+1}/06  ACREDITAÇÃO N  TIPO DE INSTALAÇÃO CRL 0495  INSTALAÇÃO PERMANENTE ÁREA DE ATIVIDADE / PRODUTO CLASSE DE ENSAIO / DESCRIÇÃO DO ENSAIO NORMA E /OU PROCEDIMENTO')
        lista_de_paginas_concatenadas = lista_de_paginas_concatenadas + new_pagina_2
    return lista_de_paginas_concatenadas

def pega_texto_pdf(pdf):
    """
    Essa função extrai o texto de todas as páginas do PDF
    escolhido.

    Args:
        pdf (str): Caminho do arquivo.

    Returns:
        list: Uma lista de strings, onde cada string é o texto de uma página do PDF.
    """
    pageList = []
    with open(pdf,'rb') as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            page_text = page.extract_text().replace('\n','')
            pageList.append(page_text)
    return pageList
