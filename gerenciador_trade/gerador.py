"""
Arquivo responsável por gerar a trade
"""
import random
from datetime import datetime
from typing import List

from gerenciador_trade.ativos import Ativos
from gerenciador_trade.db_admin import Trade


class TradeGerenciador:
    def recebe_parametros(self):
        while True:
            ativo = self.formata_ativo(
                input(
                    "Insira o ativo seguindo o seguinte exemplo: BBSE3, ANIM3, LOGN3\n"
                )
            )
            repeticao = self.formata_repeticao(
                input("Insira um número inteiro informando a quantidade de compras.\n")
            )

            dados = Ativos()
            novo_ativo = self.escolhe_aleatorio_ativo(ativo)

            if dados.verifica_se_ativo_existe(novo_ativo):
                return novo_ativo, repeticao
            else:
                print("Ativo errado ou inexistente")
                continue

    def retorna_data_e_hora(self):
        return datetime.now()

    def retorna_numero_aleatorio(self):
        return round(random.uniform(1.0, 100.0), 2)

    def gera_trade(self):
        ativos, repeticao = self.recebe_parametros()

        for i in range(repeticao):
            data_e_hora = self.retorna_data_e_hora()
            valor = self.retorna_numero_aleatorio()
            Trade.create(ativo=ativos, criacao_trade=data_e_hora, preco_trade=valor)

    def formata_ativo(self, ativo: str) -> List:
        return ativo.replace(" ", "").split(",")

    def formata_repeticao(self, repeticao: str) -> int:
        return int(repeticao)

    def escolhe_aleatorio_ativo(self, ativo: List) -> str:
        quantidade = random.randint(1, len(ativo))
        return ativo[quantidade]
