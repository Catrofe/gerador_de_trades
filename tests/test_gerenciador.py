# from gerenciador_de_trades import __version__
from gerenciador import gerador
from gerenciador import ativo
# from gerenciador.main import main




class TestTradeGerenciador:
    def __init__(self) -> None:
        self.trade = gerador.TradeGerenciador()

    def test_retorna_numero_aleatorio(self):
        lista = []
        for i in range(100000):
            lista.append(self.trade.retorna_numero_aleatorio())
        assert max(lista) == 100.0 and min(lista) == 1

    def test_formata_ativo(self):
        dados = self.trade.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")
        assert len(dados) == 4 and dados == ["B3SA3", "ABCB4", "ANIM3", "BBDC4"]

    def test_escolhe_aleatorio_ativo(self):
        dados = self.trade.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")

        escolha = self.trade.escolhe_aleatorio_ativo(dados)
        assert escolha in dados

    def test_formata_repeticao(self):
        assert self.trade.formata_repeticao("10") == 10

class TestGerenciadorAtivo:
    def __init__(self) -> None:
        self.ativo = GerenciadorAtivo()