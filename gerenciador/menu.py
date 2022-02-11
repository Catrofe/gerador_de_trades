from gerenciador.gerador import TradeGerenciador
from gerenciador.trade import GerenciadorDBTrade


class Menu:
    def __init__(
        self, ativos, repeticao, opcao_consulta, trade_consulta, valor_consulta
    ):
        self.ativos = ativos
        self.repeticao = repeticao
        self.opcao_consulta = opcao_consulta
        self.trade_consulta = trade_consulta
        self.valor_consulta = valor_consulta

    def consultas(self):
        db = GerenciadorDBTrade()
        if self.opcao_consulta is None:
            pass
        elif self.opcao_consulta == 1:
            db.retorna_trades_por_ativo(self.trade_consulta)
        elif self.opcao_consulta == 2:
            db.retorna_trades_por_valor_maior_que(self.valor_consulta)
        elif self.opcao_consulta == 3:
            db.retorna_trades_por_valor_maior_que_ativo(
                self.trade_consulta, self.valor_consulta
            )
        elif self.opcao_consulta == 4:
            db.retorna_trades_por_valor_menor_que(self.valor_consulta)
        elif self.opcao_consulta == 5:
            db.retorna_trades_por_valor_menor_que_ativo(
                self.trade_consulta, self.valor_consulta
            )
        elif self.opcao_consulta == 6:
            db.retorna_trade_mais_recente_por_ativo(self.trade_consulta)
        elif self.opcao_consulta == 7:
            db.retorna_trade_mais_recente()
        elif self.opcao_consulta == 8:
            db.retorna_agrupamento_de_ativos_e_investimentos()

        else:
            print("Error")

    def trade(self):
        trade = TradeGerenciador()
        if type(self.ativos) == str:
            trade.gera_trade(self.ativos, self.repeticao)

    def executa(self):
        self.consultas()
        self.trade()
