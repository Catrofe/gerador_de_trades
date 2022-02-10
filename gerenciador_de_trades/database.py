from peewee import CharField, DateTimeField, FloatField, Model
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase("Trades.db")


class Trade(Model):
    ativo = CharField(null=False, max_length=15)
    criacao_trade = DateTimeField(null=False)
    preco_trade = FloatField(null=False)

    class Meta:
        database = db


class Ativo(Model):
    ativo = CharField(null=False, max_length=15)

    class Meta:
        database = db


db.create_tables([Trade, Ativo])
