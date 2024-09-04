from peewee import CharField, ForeignKeyField
from .base import BaseModel

class Categoria(BaseModel):
    nome = CharField(unique=True)

class Fornecedor(BaseModel):
    nome = CharField()
    email = CharField()
    
    estado = CharField()
    cidade = CharField()
    cep = CharField()
    endereco = CharField()
    
    cnpj = CharField()
    ie = CharField()

    categoria = ForeignKeyField(Categoria, backref='fornecedores')