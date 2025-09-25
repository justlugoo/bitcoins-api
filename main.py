from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.api import api_router
from app.core.init_db import init_db
import os

# Crear aplicación FastAPI
app = FastAPI(
    title="Bitcoins API",
    description="API REST para consultar precios de criptomonedas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas de la API
app.include_router(api_router)

# Ruta raíz con documentación HTML
@app.get("/", response_class=HTMLResponse)
async def root():
    """Página de inicio con documentación básica"""
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bitcoins API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }
            .endpoint {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                border-left: 4px solid #3498db;
            }
            .method {
                font-weight: bold;
                color: #27ae60;
            }
            .url {
                font-family: monospace;
                background: #e9ecef;
                padding: 2px 6px;
                border-radius: 3px;
            }
            .description {
                color: #6c757d;
                margin-top: 5px;
            }
            .links {
                text-align: center;
                margin-top: 30px;
            }
            .links a {
                display: inline-block;
                margin: 0 10px;
                padding: 10px 20px;
                background: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
            }
            .links a:hover {
                background: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Bitcoins API</h1>
            <p style="text-align: center; color: #6c757d; margin-bottom: 30px;">
                API REST para consultar precios de criptomonedas
            </p>
            
            <h2>📋 Endpoints Disponibles</h2>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/crypto/{symbol}</div>
                <div class="description">Obtener precio actual de una criptomoneda</div>
            </div>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/crypto/top/{limit}</div>
                <div class="description">Obtener top criptomonedas por market cap</div>
            </div>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/crypto/compare/{symbol1}/{symbol2}</div>
                <div class="description">Comparar dos criptomonedas</div>
            </div>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/crypto/</div>
                <div class="description">Obtener todas las criptomonedas disponibles</div>
            </div>
            
            <h2>💡 Ejemplos de Uso</h2>
            <ul>
                <li><strong>Bitcoin:</strong> <code>/crypto/BTC</code></li>
                <li><strong>Top 10:</strong> <code>/crypto/top/10</code></li>
                <li><strong>Comparar:</strong> <code>/crypto/compare/BTC/ETH</code></li>
            </ul>
            
            <div class="links">
                <a href="/docs">📚 Documentación Interactiva</a>
                <a href="/redoc">📖 ReDoc</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

# Inicializar base de datos al arrancar
@app.on_event("startup")
async def startup_event():
    """Inicializar la base de datos con datos mock al arrancar la aplicación"""
    init_db()

# Health check
@app.get("/health")
async def health_check():
    """Endpoint de salud para verificar que la API está funcionando"""
    return {
        "status": "healthy",
        "message": "Bitcoins API is running",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)