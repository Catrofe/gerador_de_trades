FROM python:3.10

COPY ./pyproject.toml /pyproject.toml
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

RUN mkdir /gerador_de_trades
COPY . /gerador_de_trades
WORKDIR /gerador_de_trades

CMD ["python", "./main.py"]