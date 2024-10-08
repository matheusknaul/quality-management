from types import NoneType
from database.models.norma import Norma

""" 
Esse arquivo serve para capturar os registros do banco de dados e enviar para o script
de gerenciamento da automação.
"""

# class Norma(BaseModel):
#     codigo = CharField()
#     descricao = CharField()
#     ano_norma = IntegerField()
#     situacao = CharField()
#     data_ultima_verificacao = DateTimeField(default=datetime.datetime.now)
#     tag_main = CharField()
#     part_main = CharField()
#     number_main = CharField()

#key entry é a chave com os itens que serão necessários para o automatizador realizar a pesquisa.

# entrada = [tag, number, part, year]
# saída = [código da norma completo, descrição, status (aqui inclui quanto o status da norma, quanto o status da verificação), data da última verificação]

def __getData__():
    normas = Norma.select()
    key_entries = []

    for norma in normas:
        key_entries.append([norma.tag_main, norma.number_main, norma.part_main, norma.ano_norma])

    return key_entries
