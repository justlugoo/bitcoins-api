from sqlalchemy.orm import Session
from app.repositories.crypto_repository import CryptoRepository
from app.models.crypto import Crypto
from typing import List, Optional, Dict, Any

class CryptoService:
    def __init__(self, db: Session):
        self.repository = CryptoRepository(db)
    
    def get_crypto_by_symbol(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Obtener información de una criptomoneda por símbolo"""
        crypto = self.repository.get_by_symbol(symbol)
        if not crypto:
            return None
        return crypto.to_dict()
    
    def get_top_cryptos(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Obtener top criptomonedas por market cap"""
        cryptos = self.repository.get_top_by_market_cap(limit)
        return [crypto.to_dict() for crypto in cryptos]
    
    def compare_cryptos(self, symbol1: str, symbol2: str) -> Optional[Dict[str, Any]]:
        """Comparar dos criptomonedas"""
        crypto1, crypto2 = self.repository.get_by_symbols(symbol1, symbol2)
        
        if not crypto1 or not crypto2:
            return None
        
        # Calcular comparación
        price_difference = crypto1.price - crypto2.price
        price_ratio = crypto1.price / crypto2.price if crypto2.price > 0 else 0
        
        return {
            "crypto1": crypto1.to_dict(),
            "crypto2": crypto2.to_dict(),
            "comparison": {
                "price_difference": round(price_difference, 2),
                "price_ratio": round(price_ratio, 2),
                "market_cap_difference": crypto1.market_cap - crypto2.market_cap if crypto1.market_cap and crypto2.market_cap else None,
                "change_24h_difference": crypto1.change_24h - crypto2.change_24h
            }
        }
    
    def get_all_cryptos(self) -> List[Dict[str, Any]]:
        """Obtener todas las criptomonedas"""
        cryptos = self.repository.get_all()
        return [crypto.to_dict() for crypto in cryptos]
