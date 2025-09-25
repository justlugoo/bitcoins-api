from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.crypto import Crypto
from typing import List, Optional

class CryptoRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_symbol(self, symbol: str) -> Optional[Crypto]:
        """Obtener criptomoneda por símbolo"""
        return self.db.query(Crypto).filter(Crypto.symbol == symbol.upper()).first()
    
    def get_top_by_market_cap(self, limit: int = 10) -> List[Crypto]:
        """Obtener top criptomonedas por market cap"""
        return self.db.query(Crypto).order_by(desc(Crypto.market_cap)).limit(limit).all()
    
    def get_all(self) -> List[Crypto]:
        """Obtener todas las criptomonedas"""
        return self.db.query(Crypto).all()
    
    def get_by_symbols(self, symbol1: str, symbol2: str) -> tuple[Optional[Crypto], Optional[Crypto]]:
        """Obtener dos criptomonedas por sus símbolos"""
        crypto1 = self.get_by_symbol(symbol1)
        crypto2 = self.get_by_symbol(symbol2)
        return crypto1, crypto2
