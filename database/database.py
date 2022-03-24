from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def build_engine(db_url: str) -> Engine:
    return create_engine(db_url)


def build_session_maker(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine)


def setup_db(engine: Engine) -> None:
    Base.metadata.create_all(engine)


class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    active = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)
