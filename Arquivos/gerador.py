"""
Arquivo responsável por gerar a trade
"""

from datetime import datetime
from random import random


class Trade:
    def recebe_parametros(self, ativo, repeticao):
        return ativo, repeticao

    def retorna_data_e_hora(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    def retorna_numero_aleatorio(self):
        return round((random() * 100), 2)

    def gera_trade():
        ativo, repeticao = Trade.recebe_parametros("GSHP3", 5)
        data_e_hora = Trade.retorna_data_e_hora()
        valor = Trade.retorna_numero_aleatorio()

        # Criar função que insere trade no banco
        return ativo, repeticao, valor, data_e_hora
