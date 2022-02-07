"""
Arquivo responsável por gerar a trade
"""
from datetime import datetime
from random import random

from db_admin import Trade


class TradeGerenciador:
    def recebe_parametros(self, ativo, repeticao):
        return ativo, repeticao

    def retorna_data_e_hora(self):
        return datetime.now()  # .strftime("%d/%m/%Y %H:%M")

    def retorna_numero_aleatorio(self):
        return round((random() * 100), 2)

    def gera_trade(self):
        ativo, repeticao = self.recebe_parametros("LOGN3", 2)

        for i in range(repeticao):
            data_e_hora = self.retorna_data_e_hora()
            valor = self.retorna_numero_aleatorio()
            Trade.create(ativo=ativo, criacao_trade=data_e_hora, preco_trade=valor)
