from sqlalchemy.orm import Session
from app.repositories.crypto_repository import CryptoRepository
from app.models.crypto import Crypto
from app.core.init_db import get_mock_data
from typing import List, Optional, Dict, Any
import os

class CryptoService:
    def __init__(self, db: Session):
        self.repository = CryptoRepository(db)
        self.is_vercel = "vercel.app" in os.getenv("VERCEL_URL", "")
        self.mock_data = get_mock_data()
    
    def get_crypto_by_symbol(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Obtener información de una criptomoneda por símbolo"""
        if self.is_vercel:
            # En Vercel, usar datos mock directamente
            for crypto in self.mock_data:
                if crypto["symbol"].upper() == symbol.upper():
                    return crypto
            return None
        else:
            # Localmente, usar base de datos
            crypto = self.repository.get_by_symbol(symbol)
            if not crypto:
                return None
            return crypto.to_dict()
    
    def get_top_cryptos(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Obtener top criptomonedas por market cap"""
        if self.is_vercel:
            # En Vercel, usar datos mock directamente
            sorted_cryptos = sorted(self.mock_data, key=lambda x: x["market_cap"], reverse=True)
            return sorted_cryptos[:limit]
        else:
            # Localmente, usar base de datos
            cryptos = self.repository.get_top_by_market_cap(limit)
            return [crypto.to_dict() for crypto in cryptos]
    
    def compare_cryptos(self, symbol1: str, symbol2: str) -> Optional[Dict[str, Any]]:
        """Comparar dos criptomonedas"""
        if self.is_vercel:
            # En Vercel, usar datos mock directamente
            crypto1 = None
            crypto2 = None
            for crypto in self.mock_data:
                if crypto["symbol"].upper() == symbol1.upper():
                    crypto1 = crypto
                if crypto["symbol"].upper() == symbol2.upper():
                    crypto2 = crypto
            
            if not crypto1 or not crypto2:
                return None
        else:
            # Localmente, usar base de datos
            crypto1, crypto2 = self.repository.get_by_symbols(symbol1, symbol2)
            if not crypto1 or not crypto2:
                return None
            crypto1 = crypto1.to_dict()
            crypto2 = crypto2.to_dict()
        
        # Calcular comparación
        price_difference = crypto1["price"] - crypto2["price"]
        price_ratio = crypto1["price"] / crypto2["price"] if crypto2["price"] > 0 else 0
        
        return {
            "crypto1": crypto1,
            "crypto2": crypto2,
            "comparison": {
                "price_difference": round(price_difference, 2),
                "price_ratio": round(price_ratio, 2),
                "market_cap_difference": crypto1["market_cap"] - crypto2["market_cap"] if crypto1["market_cap"] and crypto2["market_cap"] else None,
                "change_24h_difference": crypto1["change_24h"] - crypto2["change_24h"]
            }
        }
    
    def get_all_cryptos(self) -> List[Dict[str, Any]]:
        """Obtener todas las criptomonedas"""
        if self.is_vercel:
            # En Vercel, usar datos mock directamente
            return self.mock_data
        else:
            # Localmente, usar base de datos
            cryptos = self.repository.get_all()
            return [crypto.to_dict() for crypto in cryptos]