from peewee import CharField, IntegerField, BooleanField, DateTimeField
from .base import BaseModel
import datetime

class Norma(BaseModel):
    codigo = CharField()
    descricao = CharField()
    ano_norma = IntegerField()
    situacao = BooleanField()
    data_ultima_verificacao = DateTimeField(default=datetime.datetime.now)







    