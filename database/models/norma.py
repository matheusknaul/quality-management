from peewee import Model, CharField, IntegerField, BooleanField, DateTimeField
from database.database import db
import datetime

class Norma(Model):
    codigo = CharField()
    descricao = CharField()
    ano_norma = IntegerField()
    situacao = BooleanField()
    data_ultima_verificacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db 