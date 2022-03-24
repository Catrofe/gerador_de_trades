from dataclasses import dataclass

from fastapi import FastAPI, HTTPException
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.queries import check_query_to_perform
from app.trades import GenerationSuccess, GeneratorTrades
from database.database import build_engine, build_session_maker, setup_db
from models.models_main import InputQuery, InputTrade, OutputTrade

app = FastAPI()


@dataclass
class ServerContext:
    engine: Engine
    session_maker: sessionmaker


engine = build_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")
context = ServerContext(engine=engine, session_maker=build_session_maker(engine))


@app.on_event("startup")
def startup_event() -> None:
    setup_db(context.engine)


@app.post("/create_trade", status_code=201, response_model=OutputTrade)
def create_trade(trade: InputTrade) -> OutputTrade:
    generate_trade = GeneratorTrades(trade)
    response = generate_trade.generate_trade(context.session_maker)

    if isinstance(response, GenerationSuccess):
        return OutputTrade(repetition=response.repetition, message=response.message)

    raise HTTPException(status_code=response.code, detail=response.message)


@app.get("/queries", status_code=200)
def queries(query: InputQuery) -> InputQuery:
    response = check_query_to_perform(query, context.session_maker)

    return response
