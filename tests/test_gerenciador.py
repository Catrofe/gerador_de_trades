from gerenciador import ativo, database, gerador, trade

gerador = gerador.TradeGerenciador()
ativo = ativo.GerenciadorAtivo()
db_trade = trade.GerenciadorDBTrade()


class TestTradeGerenciador:
    def test_retorna_numero_aleatorio(self):
        lista = []
        for i in range(100000):
            lista.append(gerador.retorna_numero_aleatorio())
        assert max(lista) == 100.0 and min(lista) == 1

    def test_formata_ativo(self):
        dados = gerador.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")
        assert len(dados) == 4 and dados == ["B3SA3", "ABCB4", "ANIM3", "BBDC4"]

    def test_escolhe_aleatorio_ativo(self):
        dados = gerador.formata_ativo("B3SA3, ABCB4, ANIM3, BBDC4")

        escolha = gerador.escolhe_aleatorio_ativo(dados)
        assert escolha in dados

    def test_formata_repeticao(self):
        assert gerador.formata_repeticao("10") == 10


class TestGerenciadorAtivo:
    def test_verifica_se_ativo_existe_string(self):
        assert ativo.verifica_se_ativo_existe("ITUB3")

    def test_verifica_se_ativo_existe_none(self):
        assert not ativo.verifica_se_ativo_existe(None)

    def test_veririca_se_ativo_existe_int(self):
        assert not ativo.verifica_se_ativo_existe(2)

    def test_faz_banco_se_recriar(self):
        database.Ativo.create(ativo="ativo")
        assert ativo.gerencia() == 156


class TestTradeDB:
    def test_formata_repeticao(self):
        assert db_trade.formata_valor(22.5)

    def test_formata_repeticao_string(self):
        assert db_trade.formata_valor("22,5")
