"""
Arquivo que configura ativos
"""
from gerenciador.database import Ativo


class GerenciadorAtivo:
    def gerencia(self) -> None:
        valor_dados = self.verifica_se_dados_existem()

        if valor_dados == 0:
            self.adiciona_ativos()
        elif valor_dados < 156 or valor_dados > 156:
            Ativo.delete()
            with open("app/ativos.txt", "r") as arquivo:
                for ativo in arquivo.readlines():
                    Ativo.create(ativo=ativo.replace("\n", ""))
        else:
            return "Banco está em funcionamento."

    def verifica_se_dados_existem(self) -> int:
        dados = Ativo.select()
        return len(dados)

    def adiciona_ativos(self) -> None:
        with open("ativos.txt", "r") as arquivo:
            for ativo in arquivo.readlines():
                Ativo.create(ativo=ativo.replace("\n", ""))

    def verifica_se_ativo_existe(self, ativo: str) -> bool:
        linha = Ativo.select(Ativo.ativo).where(Ativo.ativo == ativo)
        if len(linha):
            return True
        elif not len(linha):
            return False

oi = GerenciadorAtivo()
oi.gerencia()