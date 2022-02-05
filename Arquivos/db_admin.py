"""
Arquivo responsável pela integração
com banco de dados.
"""


from peewee import CharField, DateTimeField, FloatField, Model
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase(
    database="trades", host="localhost", user="root", password=""
)


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = db


class Trade(BaseModel):
    stock_code = CharField(null=False)
    criacao_trade = DateTimeField(null=False)
    preco_trade = FloatField(null=False)


db.create_tables([Trade])
