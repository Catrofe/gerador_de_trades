# Gerador de trades

## Tópicos


## Sobre o projeto.
Gerador de trades é um projeto desenvolvido a partir de um desafio proposto por uma empresa.
O nosso desafio era criar um gerador de trades que recebe 2 parâmetros, um stock-code e um numero de repetição, com base nesses dois parâmetros devo gerar aleatoriamente os outros dois.
Agora vamos falar um pouco mais sobre as ferramentas utilizadas e por quê?

### Por que Postgres?
Essa resposta é um pouco confusa. Inicialmente iniciei meu projeto com MySQL, porem me deparei com um erro chamado de 'caching_sha2_password' e por não conseguir solucionar e já ter perdido muito tempo optei pela troca de banco de dados, dando sorte pelo ORM escolhido suportar SQLITE. Porem com SQLITE percebi que não iria conseguir dockerizar a partir disso alterei para Postgres.

### Por que o desconhecido peewee?
Peewee foi o primeiro ORM com que tive contato, o mesmo é bem simples e tem uma curva de aprendizado muito fácil. Peewee também não é mil maravilhas, caso eu escolhesse SQLAlchemy poderia conseguir o mesmo resultado, porem utilizando um ORM mais potente.
Algo que está em minha lista de estudos é o SQLAlchemy, então dentro das próximas semanas devo estar com ele "em dia"!

### Por que pytest?
A minha primeira interação com testes foi 2 dias antes do inicio do desafio, e Pytest foi a única biblioteca que consegui ter tempo para estudar. 
Por esse motivo resolvi utilizar o pytest e ignorar os seus concorrentes.

## Sobre os requisitos solicitados no desafio.

### Gerador de trades
- [x] Gerador de trades
Como solicitado o usuário deve inserir apenas 2 parâmetros: uma sequencia de ativos em formato de string e a quantidade de vezes que deve ser realizada a compra em um formato de inteiro. Após isso o programa gerara automaticamente data e hora atual e um numero aleatório para o preço da ação.

### Listar Trades
- [x] Listar trades
Como solicitado pelo desafio, eu criei todas o retornos solicitador e como parte do desafio extra eu criei uma solicitação extra. Para criação dela pensei em um retorno que fosse agregar bastante conhecimento ao usuário.
Acredito que retornar o ativo e o quanto foi investido nele seja muito bom para o usuário.
<img align="center" src="https://i.imgur.com/BXtxN2Z.png">

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

4- Leia a docstring do arquivo "main.py", a docsctring explica como alterar as variáveis para fazer o sistema funcionar.

5- Agora basta alterar as variáveis.
<br>
<img src="https://i.imgur.com/e6L0qFP.png">

6- Para rodar o programa digite em seu console:
```bash
python main.py
```

## Possíveis Melhorias

### MAIN.PY
Acredito que a forma como estou rodando meu programa não é das melhores, porem acabei tendo dificuldades em como construir uma boa CLI

### Adicionar Tkinter e API
Adicionar uma interface e/ou até mesmo uma API REST seria uma ótima melhoria para o projeto.

## Dificuldades

Sem duvidas minha maior dificuldade foi a criação do main, diversas vezes apaguei todo meu código e recomecei, não consegui pensar em uma boa forma de rodar meu programa. Acabei optando por rodar ele dessa forma, porem não acredito ser a melhor para o usuário.

Uma outra dificuldade foi a utilização do Docker, foi a primeira vez que utilizei o mesmo, porem assumo que não foi nenhum bicho de 7 cabeças.

Desde já agradeço a empresa e toda a equipe pela chance de realizar esse desafio <3.
