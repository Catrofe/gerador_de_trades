from gerador import TradeGerenciador
from trade import GerenciadorDBTrade

class Menu:
    def __init__(self):
        self.Trade = TradeGerenciador()
        self.db_trade = GerenciadorDBTrade()

    def __str__(self):
        retorno = """GERADOR DE TRADE
                1- Para gerar novas trades.
                Abaixo estão as consultas:
                2- Para trades de um determinado ativo.
                3- Retorna trades por valor menor que o inserido.
                4- Retorna valor por menor que o inserido com filtro de ativo.
                5- Retorna trades por valor maior que o inserido.
                6- Retorna valor por maior que o inserido com filtro de ativo.
                7- Retorna trade mais recente do ativo escolhido.
                8- Retorna trade mais recente.
                9- Retorna total investido por ativo.(Extra)\n"""

        return retorno

    def menu_escolha(self):
        print(self)

oi = Menu()
oi.menu_escolha()