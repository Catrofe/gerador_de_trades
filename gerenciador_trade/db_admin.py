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
        try:
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
        except TypeError:
            linha = (
                (
                    f"""ID: {dados.id} -
                         ativo: {dados.ativo} -
                         data de criação: {dados.criacao_trade} -
                         valor investido: {dados.preco_trade}"""
                )
                .replace("\n", "", 3)
                .replace("    ", "")
            )
            print(linha)

    def retorna_trades_por_ativo(self, ativo) -> None:
        dados = Trade.select().where(Trade.ativo == ativo)
        self.gera_prints(dados)

    def retorna_trades_por_valor_maior_que(self, valor: str) -> None:
        valor = self.formata_repeticao(valor)
        dados = Trade.select().where(Trade.preco_trade > valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_menor_que(self, valor: str) -> None:
        valor = self.formata_repeticao(valor)
        dados = Trade.select().where(Trade.preco_trade < valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_maior_que_ativo(self, ativo, valor) -> None:
        valor = self.formata_repeticao(valor)
        dados = Trade.select().where(Trade.ativo == ativo, Trade.preco_trade > valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_menor_que_ativo(self, ativo, valor) -> None:
        valor = self.formata_repeticao(valor)
        dados = Trade.select().where(Trade.ativo == ativo, Trade.preco_trade < valor)
        self.gera_prints(dados)

    def retorna_trade_mais_recente_por_ativo(self, ativo) -> None:
        dados = (
            Trade.select()
            .where(Trade.ativo == ativo)
            .order_by(Trade.criacao_trade.desc())
            .get()
        )
        self.gera_prints(dados)

    def retorna_trade_mais_recente(self) -> None:
        dados = Trade.select().order_by(Trade.criacao_trade.desc()).get()
        self.gera_prints(dados)

    def formata_repeticao(self, valor: str) -> float:
        try:
            return float(valor.replace(",", "."))
        except AttributeError:
            return float(valor)
