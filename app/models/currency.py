from sqlalchemy import BigInteger, Column, Float, Text

from app.core.db import Base


class Currency(Base):
    name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)

    def __repr__(self):
        return (
            f'\nТикер валюты: {self.name}'
            f'\nЦена: {self.price}'
            f'\nВремя: {self.timestamp},\n'
        )
