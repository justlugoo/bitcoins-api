# API PÚBLICA SIMPLE - FASTAPI

## PROMPT PARA LA IA

```
Crea una API REST simple con FastAPI para consultar precios de criptomonedas.

ENDPOINTS:
- GET /crypto/{symbol} - Precio actual de una cripto
- GET /crypto/top/10 - Top 10 criptos por market cap
- GET /crypto/compare/{symbol1}/{symbol2} - Comparar dos criptos
- GET / - Documentación básica HTML

DATOS MOCK (no API externa):
```python
crypto_data = {
    "BTC": {"name": "Bitcoin", "price": 43500.00, "change_24h": 2.5},
    "ETH": {"name": "Ethereum", "price": 2680.00, "change_24h": -1.2},
    "BNB": {"name": "Binance Coin", "price": 315.50, "change_24h": 0.8},
    "SOL": {"name": "Solana", "price": 98.75, "change_24h": 4.2},
    "ADA": {"name": "Cardano", "price": 0.52, "change_24h": -0.5}
}
```

ESTRUCTURA:
- Un solo archivo main.py
- Sin base de datos
- Respuestas JSON simples
- CORS habilitado
- Documentación automática

REQUISITOS:
- Código en menos de 100 líneas
- Deployable en Railway/Render
- Funcional desde cualquier dispositivo
```

## SETUP CON UV

### Instalación y entorno
```bash
# 1. Crear proyecto con uv
uv init fastapi-crypto-api
cd fastapi-crypto-api

# 2. Crear entorno virtual
uv venv

# 3. Activar entorno
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 4. Instalar dependencias
uv add fastapi "uvicorn[standard]"

# 5. Ejecutar
uv run uvicorn main:app --reload
```

## HOSTING RECOMENDADO (GRATIS)

### Railway (Más fácil)
```bash
# 1. Instala Railway CLI
npm install -g @railway/cli

# 2. Login y deploy
railway login
railway init
railway up
```

### Render (Más estable)
1. Sube tu código a GitHub
2. Conecta tu repo en render.com
3. Build Command: `uv sync`
4. Start Command: `uv run uvicorn main:app --host 0.0.0.0 --port $PORT`

### Replit (Más rápido para testing)
1. Crea nuevo Repl Python
2. Instala uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Pega el código y ejecuta con uv

## ARCHIVOS NECESARIOS

**pyproject.toml:** (uv lo genera automáticamente)

**requirements.txt:** (para compatibilidad hosting)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
```

**main.py:** (La IA te lo genera)

## CONSUMO DESDE CUALQUIER DISPOSITIVO

### JavaScript (Web/Móvil)
```javascript
// Obtener precio de Bitcoin
fetch('https://tu-api.railway.app/crypto/BTC')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python (Desktop/Script)
```python
import requests
response = requests.get('https://tu-api.railway.app/crypto/BTC')
print(response.json())
```

### cURL (Terminal)
```bash
curl https://tu-api.railway.app/crypto/BTC
```

## ALTERNATIVAS DE API

**API de Frases Motivacionales:** Devuelve frases random con autor y categoría
**API de Colores:** Genera paletas de colores con códigos HEX/RGB
**API de QR Codes:** Genera códigos QR desde texto
**API de Acortador de URLs:** Acorta URLs como bit.ly