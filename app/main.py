from dataclasses import dataclass

from fastapi import FastAPI
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from database.database import build_engine, build_session_maker, setup_db
from models.models_main import Trade

app = FastAPI()


@dataclass
class ServerContext:
    engine: Engine
    session_maker: sessionmaker


engine = build_engine("sqlite:///db.sqlite3")
context = ServerContext(engine=engine, session_maker=build_session_maker(engine))


@app.on_event("startup")
def startup_event() -> None:
    setup_db(context.engine)


@app.post("create_trade")
def create_trade(trade: Trade):
    pass
