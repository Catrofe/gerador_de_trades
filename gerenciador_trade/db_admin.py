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
    ativo = CharField(null=False, max_length=15)
    criacao_trade = DateTimeField(null=False)
    preco_trade = FloatField(null=False)


db.create_tables([Trade])


class GerenciadorDB:
    #     Listar todos os Trades:
    # De um determinado ativo;
    def gera_prints(self, dados) -> None:
        print(type(dados))
        for linha in dados:
            dados = (
                (
                    f"""ID: {linha.id} -
                    ativo: {linha.ativo} -
                    data de criação: {linha.criacao_trade} -
                    valor investido: {linha.preco_trade}"""
                )
                .replace("\n", "", 3)
                .replace("    ", "")
            )
            print(dados)

    def retorna_trades_por_ativo(self, ativo) -> None:
        dados = Trade.select().where(Trade.ativo == ativo)
        self.gera_prints(dados)
