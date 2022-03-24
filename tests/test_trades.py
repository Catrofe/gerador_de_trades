from sqlalchemy.orm import sessionmaker

from app.trades import GeneratorTrades
from models.models_main import InputTrade


def test_verify_if_trade_exists_should_true():
    trade: str = "ANIM3, BBSE3, BRAP4, BPAC11"

    class_create = GeneratorTrades(InputTrade(active=trade, repetition=1), sessionmaker)

    result = class_create.verify_if_active_exists()

    assert result


def test_verify_if_trade_exists_should_false():
    trade: str = "ANIM3, BBSE3, BRAP4, BPAC"

    class_create = GeneratorTrades(InputTrade(active=trade, repetition=1), sessionmaker)

    result = class_create.verify_if_active_exists()

    assert not result


def test_verify_if_trade_exists_with_integer_should_false():
    trade: int = 5

    class_create = GeneratorTrades(InputTrade(active=trade, repetition=1), sessionmaker)

    result = class_create.verify_if_active_exists()

    assert not result
