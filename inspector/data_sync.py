import configuration
from database.models.norma import Norma

""" 
Esse arquivo serve para capturar os registros do banco de dados e enviar para o script
de gerenciamento da automação.

Também é o arquivo responsável por devolver as informações para o banco de dados das
normas.
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

# entrada = [id, tag, number, part, year]
# saída = [código da norma completo, descrição, status (aqui inclui quanto o status da norma, quanto o status da verificação),
# data da última verificação]

#Precisamos fazer uma lógica para ver se a norma precisa ser verificada! (x-x-x  A fazer  x-x-x)
def __getData__():
    normas = Norma.select()
    key_entries = []

    # Para cada registro, ele enviará inclusive também, o ID do registro, para facilitar depois o update do resultado.

    for norma in normas:
        key_entries.append([norma.id, norma.tag_main, norma.number_main, norma.part_main, norma.ano_norma])

    return key_entries

# O id é o mais importante, é o que a função usará como referência.
# Essa função também possui uma lógica para setar a data da última verificação.
def __setData__(id_norma, codigo_norma, descricao_norma, status_norma):
    norma = Norma.get(Norma.id == id_norma)

    norma.codigo = codigo_norma
    norma.descricao = descricao_norma
    norma.situacao = status_norma
    norma.data_ultima_verificacao = 1

    print(f"O registro foi alterado com sucesso! ID: {id_norma}")