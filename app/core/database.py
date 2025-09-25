from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuración de la base de datos
# En Vercel usamos SQLite en memoria, localmente usamos archivo
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./crypto_api.db")
if "vercel.app" in os.getenv("VERCEL_URL", ""):
    DATABASE_URL = "sqlite:///:memory:"

# Crear engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()