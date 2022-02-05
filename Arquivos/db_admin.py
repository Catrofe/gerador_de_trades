"""
Arquivo responsável pela integração 
com banco de dados.
"""

from sqlite3 import Date
from peewee import *
from datetime import date
from playhouse.mysql_ext import MySQLConnectorDatabase
from datetime import datetime

db = MySQLConnectorDatabase('trades', host='localhost', user='root', password='')

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db


class Trade(BaseModel):
    stock_code = CharField(null=False)
    criacao_trade = DateTimeField(null=False)
    preco_trade = FloatField(null=False)

db.create_tables([Trade])

trade1 = Trade.create(stock_code="ABC12", criacao_trade=datetime.now(), preco_trade=89.0)