from main import ATIVOS, REPETICAO, CONSULTA, TRADE_CONSULTA, VALOR_CONSULTA
from trade import GerenciadorDBTrade
from gerador import TradeGerenciador


class Menu:
    def consulta(self):
        db = GerenciadorDBTrade()
        if CONSULTA == None:
            pass
        elif CONSULTA == 1:
            db.retorna_trades_por_ativo(TRADE_CONSULTA)
        elif CONSULTA == 2:
            db.retorna_trades_por_valor_maior_que(VALOR_CONSULTA)
        elif CONSULTA == 3:
            db.retorna_trades_por_valor_maior_que_ativo(TRADE_CONSULTA, VALOR_CONSULTA)
        elif CONSULTA == 4:
            db.retorna_trades_por_valor_menor_que(VALOR_CONSULTA)
        elif CONSULTA == 5:
            db.retorna_trades_por_valor_menor_que_ativo(TRADE_CONSULTA, VALOR_CONSULTA)
        elif CONSULTA == 6:
            db.retorna_trade_mais_recente_por_ativo(TRADE_CONSULTA)
        elif CONSULTA == 7:
            db.retorna_trade_mais_recente()
        elif CONSULTA == 8:
            db.retorna_agrupamento_de_ativos_e_investimentos()
        else:
            print("Error")

    def trade(self):
        trade = TradeGerenciador()
        if type(ATIVOS) == str:
            trade.gera_trade(ATIVOS, REPETICAO)

    def executa(self):
        self.consulta()
        self.trade()
