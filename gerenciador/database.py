from peewee import CharField, DateTimeField, FloatField, Model
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.postgres_ext import PostgresqlExtDatabase


db = PostgresqlExtDatabase('Trades', user='postgres', password='root')

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
