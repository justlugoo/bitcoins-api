from sqlalchemy.orm import Session
from app.core.database import engine, Base
from app.models.crypto import Crypto

def init_db():
    """Inicializar la base de datos con datos mock"""
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    # Crear sesión
    db = Session(engine)
    
    try:
        # Verificar si ya existen datos
        if db.query(Crypto).first() is None:
            # Datos mock iniciales
            mock_cryptos = [
                Crypto(symbol="BTC", name="Bitcoin", price=43500.00, change_24h=2.5, market_cap=850000000000),
                Crypto(symbol="ETH", name="Ethereum", price=2680.00, change_24h=-1.2, market_cap=320000000000),
                Crypto(symbol="BNB", name="Binance Coin", price=315.50, change_24h=0.8, market_cap=48000000000),
                Crypto(symbol="SOL", name="Solana", price=98.75, change_24h=4.2, market_cap=42000000000),
                Crypto(symbol="ADA", name="Cardano", price=0.52, change_24h=-0.5, market_cap=18000000000),
                Crypto(symbol="XRP", name="Ripple", price=0.62, change_24h=1.8, market_cap=35000000000),
                Crypto(symbol="DOGE", name="Dogecoin", price=0.08, change_24h=3.1, market_cap=12000000000),
                Crypto(symbol="MATIC", name="Polygon", price=0.85, change_24h=-2.3, market_cap=8000000000),
                Crypto(symbol="AVAX", name="Avalanche", price=25.40, change_24h=1.5, market_cap=6000000000),
                Crypto(symbol="DOT", name="Polkadot", price=6.80, change_24h=-0.8, market_cap=8500000000)
            ]
            
            # Insertar datos
            for crypto in mock_cryptos:
                db.add(crypto)
            
            db.commit()
            print("Base de datos inicializada con datos mock")
        else:
            print("La base de datos ya contiene datos")
            
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
        db.rollback()
    finally:
        db.close()
