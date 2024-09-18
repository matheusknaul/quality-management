from peewee import CharField, BooleanField,ForeignKeyField
from .base import BaseModel

class Funcao(BaseModel):
    nome = CharField(unique=True)

class User(BaseModel):
    username = CharField(unique=True)
    nome = CharField()
    password_hash = CharField(max_length=128)
    funcao = ForeignKeyField(Funcao, backref='users')


    