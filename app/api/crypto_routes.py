from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.crypto_service import CryptoService
from typing import List, Dict, Any

router = APIRouter(prefix="/crypto", tags=["crypto"])

@router.get("/{symbol}")
async def get_crypto_price(symbol: str, db: Session = Depends(get_db)):
    """Obtener precio actual de una criptomoneda"""
    service = CryptoService(db)
    result = service.get_crypto_by_symbol(symbol)
    
    if not result:
        raise HTTPException(status_code=404, detail=f"Criptomoneda {symbol.upper()} no encontrada")
    
    return {
        "success": True,
        "data": result,
        "message": f"Precio actual de {result['name']}"
    }

@router.get("/top/{limit}")
async def get_top_cryptos(limit: int = 10, db: Session = Depends(get_db)):
    """Obtener top criptomonedas por market cap"""
    if limit <= 0 or limit > 50:
        raise HTTPException(status_code=400, detail="El límite debe estar entre 1 y 50")
    
    service = CryptoService(db)
    result = service.get_top_cryptos(limit)
    
    return {
        "success": True,
        "data": result,
        "message": f"Top {len(result)} criptomonedas por market cap"
    }

@router.get("/compare/{symbol1}/{symbol2}")
async def compare_cryptos(symbol1: str, symbol2: str, db: Session = Depends(get_db)):
    """Comparar dos criptomonedas"""
    service = CryptoService(db)
    result = service.compare_cryptos(symbol1, symbol2)
    
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No se pudieron encontrar una o ambas criptomonedas: {symbol1.upper()}, {symbol2.upper()}"
        )
    
    return {
        "success": True,
        "data": result,
        "message": f"Comparación entre {result['crypto1']['name']} y {result['crypto2']['name']}"
    }

@router.get("/")
async def get_all_cryptos(db: Session = Depends(get_db)):
    """Obtener todas las criptomonedas disponibles"""
    service = CryptoService(db)
    result = service.get_all_cryptos()
    
    return {
        "success": True,
        "data": result,
        "message": f"Lista de {len(result)} criptomonedas disponibles"
    }
