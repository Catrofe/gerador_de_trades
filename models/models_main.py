from pydantic import BaseModel


class InputTrade(BaseModel):
    active: str
    repetition: int


class OutputTrade(BaseModel):
    repetition: int
    message: str


class InputQuery(BaseModel):
    index: int
    active: str
    price: float
