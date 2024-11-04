import standards_configuration

import re

class ModelaNorma():

    #Lista dos padrões para utilizar nas funções da biblioteca RE.
    padrao_norma =r'(([A-Z]{3,4} (' ')){1,4})(\d{1,5})|(([A-Z]{2,4} (' ')){1,4})([A-Z]\d{1,5})|(([A-Z]{3,4} ){1,2}([A-Z]{3,4}/){1}([A-Z]{3,4} ){1})(\d{1,5})'
    padrao_item = r'\bItem\b'
    padrao_anexo = r'\bAnexo\b'
    padrao_data = r'(: \d{4})|(:\d{4})|(/ \d{4})|(/\d{4})'
    padrao_partes = r'(\bPartes\b \d{1,2}, \d{1,2} e \d{1,2}|\bPartes\b \d{1,2} \be\b \d{1,2})|\bParte\b \d{1,2} |-\d{1,2}| -\d{1,2}| - \d{1,2}|- \d{1,2}| \bParte\b  \d{1,2}|\bParte\b  \d{1,2}| \bPartes\b  \d{1,2} e \d{1,2}|\bPartes\b  \d{1,2} e \d{1,2}'
    padrao_anexo = r'( \bAnexos\b \d{1,2} \be\b \d{1,2}|\bAnexos\b \d{1,2} \be\b \d{1,2}|\bAnexo\b \d{1,2}| \bAnexo\b \d{1,2})'
    lista_padroes = [padrao_norma, padrao_item, 
                    padrao_data, padrao_partes, 
                    padrao_anexo]
    
    padrao_tag = r'ABNT|ASTM|ISO|NBR|IEC|NM|TS|CISPR'
    padrao_numero = r' \d{1,5} |\d{1,5} | \d{1,5}| [A-Z]{1}\d{1,5} |[A-Z]{1}\d{1,5} | [A-Z]{1}\d{1,5}'
    padrao_data_final = r'\d{1,4}'
    padrao_partes_e_anexo = r' \d{1,2} |\d{1,2} | \d{1,2}| -\d{1,2} |-\d{1,2} | -\d{1,2}| -\d {1,2} |-\d {1,2} | -\d {1,2}|-\d{1,2}'

    #Função inicializadora da classe, é nela que gerará automaticamente os resultados de buscas.
    def __init__(self, texto):
        self.texto = texto #Bloco de texto que será analisado (no contexto, ele é o bloco de caracteres retirado do escopo para a análise)
        '''
            O self.norma é uma lista, que guardará nela todos os resultados obtidos pela busca dos padrões!
            ela possui de forma fixa, indices, e cada indice, representa um resultado específico:

                [0]: É uma junção de TAG com Número;
                [1] Seria o item (não é mais utilizado);
                [2] Ano correspondente da norma;
                [3] Partes (se tiver);
                [4] Anexos (não é mais utilizado).
            
            Cada função dessa classe, analisa especificadamente cada indice dessa lista.
        '''
        self.norma = []
        self.tag = None
        self.numero = None
        self.item = []
        self.data = None
        self.partes = None
        self.anexo = []

        #Aqui é iniciado todos os métodos responsáveis para buscar/gravar os resultados formatados.
        self.busca_padrao()
        self.busca_numero()
        self.busca_parte()
        self.busca_ano()
        self.busca_tags()
        self.registra_norma()
        
    #Para cada expressão regular (padrão) na lista de padrões, ele vai comparar para ver se esse padrão dá "match" com o bloco de texto analisado.
    def busca_padrao(self):

        '''
        Esta função, define a lista self.norma, que é construída
        neste bloco de código. O índice é de acordo com os
        padrões, conforme você pode observar na variável
        lista_padroes.
        '''

        for padrao in self.lista_padroes:
            search = re.search(padrao, self.texto)
            if search:
                self.norma.append(search.group())
            else:
                self.norma.append('NA')
        return ''.join(self.norma)
    
    def busca_ano(self):  

        '''
        Esta função, define self.data como o ano encontrado
        no índice [2] de self.normas.
        '''

        search = re.search(self.padrao_data_final, self.norma[2])
        if search:
            self.data = search.group()

    def busca_tags(self):

        '''
        Esta função, define self.tag como a tag encontrada
        no índice [0] de self.normas.
        '''

        search = re.search(self.padrao_tag, self.norma[0]) 
        if search:
            self.tag = search.group()

    def busca_numero(self):

        '''
        Esta função, define self.numero como o número encontrado
        no índice [0] de self.normas.
        '''

        search = re.search(self.padrao_numero, self.norma[0]) 
        if search:
            self.numero = search.group()

    def busca_parte(self):

        '''
        Esta função analisa se o indice 3 de self.norma, possui algum
        padrão para formatar as partes da norma. Se caso houver, ele 
        formatará e definirá o valor de self.partes.
        '''

        search = re.findall(self.padrao_partes_e_anexo, self.norma[3])
        if search:
            search_result = str(search)
            self.partes = self.formatar_partes(search_result)
        
    def formatar_partes(self,string):

        '''
        Esta função tem como objetivo, receber a lista de partes
        e formatá-la em uma string, removendo os colchetes e
        aspas simples.
        '''

        string = string
        string = string.replace('[','')
        string = string.replace(']','')
        string = string.replace("'",'')
        return string

    def registra_norma(self):

        '''
        Esta função retorna um dicionário para a "normas_escopo.py" 
        que será utilizada para colocar no dataframe.
        '''

        return {
            'TAG PRINCIPAL': self.tag,
            'Numero': self.numero,
            'Parte': self.partes,
            'Ano': self.data,
            'Status': 'Analisar',
            'Data ultima verificacao': 'NA',
            'Erro status': '',
            'Link': ''
        }
