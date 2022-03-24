# Gerador de Trades

## Sobre o projeto.
Gerador de trades é um projeto desenvolvido a partir de um desafio proposto por uma empresa. O nosso desafio era criar um gerador de trades que recebe 2 parâmetros, um stock-code e um numero de repetição, com base nesses dois parâmetros devo gerar aleatoriamente os outros dois. Agora vamos falar um pouco mais sobre as ferramentas utilizadas e por quê?

## Por que Postgres?
Essa resposta é um pouco confusa. Inicialmente iniciei meu projeto com MySQL, porem me deparei com um erro chamado de 'caching_sha2_password' e por não conseguir solucionar e já ter perdido muito tempo optei pela troca de banco de dados, dando sorte pelo ORM escolhido suportar SQLITE. Porem com SQLITE percebi que não iria conseguir dockerizar a partir disso alterei para Postgres.

## SQLAlchemy
Na primeira versão utilizei o Peewee como ORM. Já nesta v2 utilizei o SQLAlchemy pois é o ORM mais utilizado do Python, além de ter a maior comunidade e ser o preferido por diversas empresas. Fiz a modificação de ORM a fim de estudar e conhecer mais o SQLAlchemy.

## Pytest
Estou avançando com testes unitários em Python e por isso escolhi a biblioteca do Pytest. 
Essa parte do código ainda não está finalizada. Devo finalizar nos próximos dias. (Dia atual: 24/03)

## Sobre os requisitos solicitados no desafio.

### Gerador de trades
- [x] Gerador de trades
Como solicitado o usuário deve inserir apenas 2 parâmetros: uma sequencia de ativos em formato de string e a quantidade de vezes que deve ser realizada a compra em um formato de inteiro. Após isso o programa gerara automaticamente data e hora atual e um numero aleatório para o preço da ação.

### Listar Trades
- [x] Listar trades
Como solicitado pelo desafio, eu criei todas o retornos solicitador e como parte do desafio extra eu criei uma solicitação extra. Para criação dela pensei em um retorno que fosse agregar bastante conhecimento ao usuário.
Acredito que retornar o ativo e o quanto foi investido nele seja muito bom para o usuário.
<img align="center" src="https://i.imgur.com/EG8R9js.png">

## Requisitos para rodar o programa.
1- Docker<br>
2- Editor(preferencia por VS Code)<br>
3- Python<br>

## Como rodar o programa.
1- Abra a pasta do arquivo em seu editor favorito, logo em seguida abra um terminal.

2- Execute em seu terminal os seguintes comandos:
```bash
pip install poetry
```

```bash
poetry install
```

```bash
poetry shell
```
Esse comando irá instalar as dependências do projeto em uma .venv(Ambiente virtual) dentro de seu projeto.

3- Rode em seu terminal o comando: 
```bash
docker-compose up -d
```
Esse comando ira iniciar o banco de dados.

4- Para rodar a API basta digitar em seu terminal:
```bash
uvicorn app.main:app
```

5- Para testar a API você pode usar ou o swagger ou o Postman.
Para utilizar o swagger acesse em seu navegador: 
```bash
http://127.0.0.1:8000/docs
```
Para utilizar o Postman, aqui estão as rotas:
```bash
http://127.0.0.1:8000/create_trade
http://127.0.0.1:8000/queries
```

## Dificuldades

Minha dificuldade maior ainda é o uso do SQLAlchemy. Tive dificuldades em criar as consultas, porem rapidamente consegui lendo a documentação cria-las da melhor maneira possível.
