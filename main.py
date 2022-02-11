"""
Use essa página para configurar sua aplicação:

ATIVOS: Insira em ativos os stock_codes que deseja,
eles podem ser listas ou strings.
Mantenha None para não gerar trade

REPETICAO: Insira um numero inteiro informando
quanto de ações deseja comprar.

CONSULTA: Caso deseja realizar uma consulta,
altere o numero para a consulta desejada,
caso não queira, mantenha None.
1- Retorna trades por ativo.
2- Retorna valor maior que.
Precisa de VALOR_CONSULTA.
3- Retorna valor maior que.
Precisa de VALOR_CONSULTA e TRADE_CONSULTA.
4- Retorna valor menor que.
Precisa de VALOR_CONSULTA.
5- Retorna valor menor que.
Precisa de VALOR_CONSULTA e TRADE_CONSULTA.
6- Retorna trade mais recente de ativo.
Precisa de TRADE_CONSULTA.
7- Retorna trade mais recente.
8- Retorna quanto foi investido por ativo.
"""
from typing import Optional

import gerenciador.database
from gerenciador.ativo import GerenciadorAtivo
from gerenciador.menu import Menu

ativos: Optional[str or None] = "B3SA3, BRSR6, BRAP4, BEEF3, VALE3"
repeticao: int = 2
opcao_consulta: Optional[int or None] = 8
trade_consulta: str = "ANIM3"
valor_consulta: Optional[float or str] = "82,18"


if __name__ == "__main__":
    gerenciador.database
    ativo_classe = GerenciadorAtivo().gerencia()
    menu = Menu(
        ativos, repeticao, opcao_consulta, trade_consulta, valor_consulta
    ).executa()
