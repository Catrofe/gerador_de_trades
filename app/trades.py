import random
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from sqlalchemy.orm import sessionmaker

from database.database import Trade
from models.models_main import InputTrade


@dataclass
class Error:
    code: int
    reason: Literal["BAD_REQUEST", "CONFLICT", "UNKNOWN", "NOT_FOUND"]
    message: str


@dataclass
class GenerationSuccess:
    repetition: int
    message: str


class GeneratorTrades:
    def __init__(self, trade: InputTrade) -> None:
        self.active = trade.active
        self.repetition = trade.repetition

    def verify_if_active_exists(self) -> bool:
        try:
            print(self.active)
            list_active: list = self.active.replace(" ", "").split(",")

            list_formatted = []

            with open("ativos.txt", "r") as arquive:
                actives_txt = arquive.readlines()
            for iten_txt in actives_txt:
                list_formatted.append(iten_txt.replace("\n", ""))

            for iten in list_active:
                if iten not in list_formatted:
                    return False
            return True
        except AttributeError:
            return False

    def return_datetime_now(self) -> datetime:
        return datetime.now()

    def return_price_random(self) -> float:
        return round(random.uniform(1.0, 1000.0), 2)

    def random_active(self) -> str:
        active_list = self.active.replace(" ", "").split(",")
        return active_list[random.randint(0, len(active_list) - 1)]

    def generate_trade(self, session_maker: sessionmaker) -> Error | GenerationSuccess:

        try:
            response = self.verify_if_active_exists()

            if not response:
                return Error(400, "BAD_REQUEST", "ACTIVE_DOES_NOT_EXISTS")

            for iten in range(self.repetition):
                trade_add = Trade(
                    active=self.random_active(),
                    datetime=self.return_datetime_now(),
                    price=self.return_price_random(),
                )
                with session_maker() as session:
                    session.add(trade_add)
                    session.commit()

            return GenerationSuccess(
                repetition=self.repetition, message="TRADES_CREATED_SUCCESSFULLY"
            )
        except Exception:
            return Error(500, "UNKNOWN", "ERROR_INTERNAL")
