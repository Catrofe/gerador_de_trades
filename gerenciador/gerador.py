"""
Arquivo responsável por gerar a trade
"""
import random
from datetime import datetime
from typing import List

# import ativo
import database


class TradeGerenciador:

    def retorna_data_e_hora(self):
        return datetime.now()

    def retorna_numero_aleatorio(self):
        return round(random.uniform(1.0, 100.0), 2)

    def gera_trade(self, ativos, repeticao):
        ativos = self.formata_ativo(ativos)
        ativo = self.escolhe_aleatorio_ativo(ativos)

        repeticao = self.formata_repeticao(repeticao)

        for i in range(repeticao):
            data_e_hora = self.retorna_data_e_hora()
            valor = self.retorna_numero_aleatorio()
            database.Trade.create(ativo=ativo, criacao_trade=data_e_hora, preco_trade=valor)

    def formata_ativo(self, ativo: str) -> List:
        return ativo.replace(" ", "").split(",")

    def formata_repeticao(self, repeticao: str) -> int:
        return int(repeticao)

    def escolhe_aleatorio_ativo(self, ativo: List) -> str:
        quantidade = random.randint(0, (len(ativo) - 1))
        return ativo[quantidade]
