from fastapi import APIRouter
from app.api.crypto_routes import router as crypto_router

api_router = APIRouter()
api_router.include_router(crypto_router)
