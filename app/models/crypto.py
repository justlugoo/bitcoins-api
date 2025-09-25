from sqlalchemy import Column, String, Float, Integer
from app.core.database import Base

class Crypto(Base):
    __tablename__ = "cryptos"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    change_24h = Column(Float, nullable=False)
    market_cap = Column(Float, nullable=True)
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "name": self.name,
            "price": self.price,
            "change_24h": self.change_24h,
            "market_cap": self.market_cap
        }
