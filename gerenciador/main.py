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
1- Retorna trades por ativo
2- Retorna valor maior que. 
Precisa de VALOR_CONSULTA
3- Retorna valor maior que. 
Precisa de VALOR_CONSULTA e TRADE_CONSULTA
4- Retorna valor menor que. 
Precisa de VALOR_CONSULTA
5- Retorna valor menor que. 
Precisa de VALOR_CONSULTA e TRADE_CONSULTA
6- Retorna trade mais recente de ativo. 
Precisa de TRADE_CONSULTA.
7- Retorna trade mais recente.
8- Retorna quanto foi investido por ativo.
"""
from typing import Optional
import menu

ATIVOS: Optional[str or None] = "B3SA3, ABCB4, ALUP11, BBSE3"
REPETICAO: int = 3
CONSULTA: Optional[int or None] = 7
TRADE_CONSULTA: str = "TPIS3"
VALOR_CONSULTA: float = 25.72

def executa_programa():
    anyway = menu.Menu()
    anyway.executa()


if __name__ == '__main__':
    executa_programa()


