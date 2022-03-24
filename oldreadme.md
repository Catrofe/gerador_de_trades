# Gerador de trades

## Tópicos


## Sobre o projeto.
Gerador de trades é um projeto desenvolvido a partir de um desáfio proposto por uma empresa.
O nosso desafio era criar um gerador de trades que recebe 2 parametros, um stock code e um numero de repetição, com base nesses dois parametros devo gerar aleatóriamente os outros dois.
Agora vamos falar um pouco mais sobre as ferramentas utilizadas e por que?

### Por que SQLITE?
Essa resposta é um pouco confusa. Inicialmente iniciei meu projeto com MySQL, porem me deparei com um erro chamado de 'caching_sha2_password' e por não conseguir solucionar e já ter perdido muito tempo optei pela troca de banco de dados, dando sorte pelo ORM escolhido suportar SQLITE.

### Por que o desconhecido peewee?
Peewee foi o primeiro ORM com que tive contato, o mesmo é bem simples e tem uma curva de aprendizado muito fácil. Peewee tambem não é só mil maravilhas, caso eu escolhesse SQLAlchemy poderia conseguir o mesmo resultado, porem utilizando um ORM mais potente.
Algo que está em minha lista de estudos é o SQLAlchemy, então dentro das próximas semanas devo estar com ele "em dia"!
- [ ] Aprender SQLAlchemy

### Por que pytest?
A minha primeira interação com testes foi 2 dias antes do inicio do desafio, e Pytest foi a unica biblioteca que consegui ter tempo para estudar. 
Por esse motivo resolvi utilizar o pytest e ignorar os seus concorrentes.

## Sobre os requisitos solicitados no desafio.

### Gerador de trades
- [x] Gerador de trades
Como solicitado o usúario deve inserir apenas 2 parametros: uma sequencia de ativos em formato de string e a quantidade de vezes que deve ser realizada a compra em um formato de inteiro. Após isso o programa gerara automaticamente data e hora atual e um numero aleatório para o preço da ação.

### Listar Trades
- [x] Listar trades
Como solicitado pelo desafio, eu criei todas o retornos solicitador e como parte do desafio extra eu criei uma solicitação extra. Para criação dela pensei em um retorno que fosse agregar bastante conhecimento ao usuario.
Acredito que retornar o ativo e o quanto foi investido nele seja muito bom para o usuario.
<img align="center" src="https://i.imgur.com/BXtxN2Z.png">

## Como rodar o programa.
1- Abra a pasta do arquivo em seu editor favorito, logo em seguida aba um terminal.

2- Rode em seu terminal o comando: 
```bash
docker-compose up -d
```

Esse comando ira iniciar o banco de dados.

3- Leia a docstring do arquivo "main.py", a dosctring explica como alterar as variaveis para fazer o sistema funcionar.

4- Agora que já sabe como alterar as variavéis, basta alterar e seguir o passo 4.
<br>
<img src="https://i.imgur.com/e6L0qFP.png">

5- Para rodar o programa digite em seu console:
```bash
python main.py
```

## Lista de tarefas
- [x] Startar banco de ativos
- [X] Geração de trades
- [x] Tratamento de input: Compras
- [x] Tratamento de input: Ativos
- [x] Criação de testes
- [x] Criação do DB
- [x] Criação interface configurável e/ou CLI
- [x] Consultar ativos seguindo solicitações do desafio
- [x] Criar consultas alem do desafio
- [x] Dockerizar 
