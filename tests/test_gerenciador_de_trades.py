# from gerenciador_de_trades import __version__
from gerenciador import gerador
# from gerenciador.main import main

trade = gerador.TradeGerenciador()


class TestTradeGerenciador:
    def test_retorna_numero_aleatorio(self):
        lista = []
        for i in range(100000):
            lista.append(trade.retorna_numero_aleatorio())
        assert max(lista) == 100.0 and min(lista) == 1

    def test_formata_ativo(self):
        dados = trade.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")
        assert len(dados) == 4 and dados == ["B3SA3", "ABCB4", "ANIM3", "BBDC4"]

    def test_escolhe_aleatorio_ativo(self):
        dados = trade.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")

        escolha = trade.escolhe_aleatorio_ativo(dados)
        assert escolha in dados

    def test_formata_repeticao(self):
        assert trade.formata_repeticao("10") == 10
