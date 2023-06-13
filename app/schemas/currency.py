from pydantic import BaseModel


class CurrencyResponse(BaseModel):
    id: int
    name: str
    price: float
    timestamp: int

    class Config:
        orm_mode = True
