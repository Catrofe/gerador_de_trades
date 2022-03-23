from pydantic import BaseModel


class Trade(BaseModel):
    active: str
    repetition: int
