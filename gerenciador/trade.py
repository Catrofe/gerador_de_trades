"""
Arquivo responsável pela integração
com banco de dados.
"""
from typing import Optional

from peewee import fn

from gerenciador.database import Trade


class GerenciadorDBTrade:
    #     Listar todos os Trades:
    # De um determinado ativo;
    def gera_prints(self, dados: str) -> None:
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

    def gera_prints_agrupados(self, dados: str) -> None:

        try:
            for linha in dados:
                dados = (
                    (
                        f"""ativo: {linha.ativo} -
                        valor investido: {round(linha.sum, 2)}"""
                    )
                    .replace("\n", "", 1)
                    .replace("    ", "")
                )
                print(dados)

        except TypeError:
            linha = (
                (
                    f"""ativo: {dados.ativo} -
                    valor investido: {round(dados.sum, 2)}"""
                )
                .replace("\n", "", 1)
                .replace("    ", "")
            )
            print(linha)

    def retorna_trades_por_ativo(self, ativo: str) -> None:
        ativo = self.formata_ativo(ativo)
        dados = Trade.select().where(Trade.ativo == ativo)
        self.gera_prints(dados)

    def retorna_trades_por_valor_maior_que(self, valor: str) -> None:
        valor = self.formata_valor(valor)
        dados = Trade.select().where(Trade.preco_trade > valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_menor_que(self, valor: Optional[float]) -> None:
        valor = self.formata_valor(valor)
        dados = Trade.select().where(Trade.preco_trade < valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_maior_que_ativo(
        self, ativo: str, valor: Optional[float]
    ) -> None:
        valor = self.formata_valor(valor)
        dados = Trade.select().where(Trade.ativo == ativo, Trade.preco_trade > valor)
        self.gera_prints(dados)

    def retorna_trades_por_valor_menor_que_ativo(
        self, ativo: str, valor: Optional[float]
    ) -> None:
        valor = self.formata_valor(valor)
        dados = Trade.select().where(Trade.ativo == ativo, Trade.preco_trade < valor)
        self.gera_prints(dados)

    def retorna_trade_mais_recente_por_ativo(self, ativo: Optional[float]) -> None:
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

    def formata_valor(self, valor: str) -> float:
        try:
            return float(valor.replace(",", "."))
        except AttributeError:
            return float(valor)

    def retorna_agrupamento_de_ativos_e_investimentos(self):
        dados = Trade.select(Trade.ativo, fn.SUM(Trade.preco_trade)).group_by(
            Trade.ativo
        )
        self.gera_prints_agrupados(dados)
