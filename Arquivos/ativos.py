"""
Arquivo que inicia ativos.
"""


def retorna_ativos_existentes():
    dados = []
    with open("dados/ativos.txt", "r") as arquivo:
        for ativo in arquivo.readlines():
            dados.append(ativo.replace("\n", ""))
        return dados


dados = retorna_ativos_existentes()

print("BIDI11" in dados)
