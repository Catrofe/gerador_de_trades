"""
Arquivo que inicia ativos.
"""


class Ativos:
    def retorna_ativos_existentes(self):
        dados = []
        with open("dados/ativos.txt", "r") as arquivo:
            for ativo in arquivo.readlines():
                dados.append(ativo.replace("\n", ""))
            return dados

    def verifica_se_ativo_existe(self, ativo):
        dados = Ativos.retorna_ativos_existentes(self)
        return ativo in dados
