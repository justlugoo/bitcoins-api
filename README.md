# 🚀 Bitcoins API

API REST robusta para consultar precios de criptomonedas construida con FastAPI, SQLite y arquitectura clean usando **uv**.

🌐 **API en Vivo:** [https://bitcoins-api.vercel.app/](https://bitcoins-api.vercel.app/)

## 🏗️ Arquitectura

```
app/
├── __init__.py
├── api/                    # Capa de presentación
│   ├── __init__.py
│   └── crypto_routes.py   # Endpoints de la API
├── core/                   # Configuración central
│   ├── __init__.py
│   ├── database.py        # Configuración de BD
│   └── init_db.py         # Inicialización de datos
├── models/                 # Modelos de datos
│   ├── __init__.py
│   └── crypto.py          # Modelo Crypto
├── repositories/           # Capa de acceso a datos
│   ├── __init__.py
│   └── crypto_repository.py
└── services/              # Lógica de negocio
    ├── __init__.py
    └── crypto_service.py
```

## 🚀 Características

- ✅ **Arquitectura Clean**: Separación clara de responsabilidades
- ✅ **Base de datos híbrida**: SQLite local, datos mock en Vercel
- ✅ **FastAPI**: Framework moderno y rápido
- ✅ **CORS habilitado**: Acceso desde cualquier dispositivo
- ✅ **Documentación automática**: Swagger UI y ReDoc
- ✅ **Deploy en Vercel**: Configuración lista para producción
- ✅ **Manejo de errores**: Respuestas consistentes y descriptivas
- ✅ **Gestionado con uv**: Gestión moderna de dependencias
- ✅ **Funciona en producción**: Optimizado para Vercel serverless

## 📋 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Documentación HTML |
| `GET` | `/health` | Health check |
| `GET` | `/crypto/{symbol}` | Precio de una cripto |
| `GET` | `/crypto/top/{limit}` | Top criptos por market cap |
| `GET` | `/crypto/compare/{symbol1}/{symbol2}` | Comparar dos criptos |
| `GET` | `/crypto/` | Todas las criptos disponibles |

## 🛠️ Instalación y Uso

### Con UV (Recomendado)

```bash
# 1. Clonar el repositorio
git clone <tu-repo>
cd BitcoinsAPI

# 2. Instalar dependencias con uv
uv sync

# 3. Ejecutar la aplicación
uv run python main.py
```

### Método Tradicional

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la aplicación
python main.py
```

## 🌐 Deploy en Vercel

### 1. Preparar el proyecto

```bash
# Asegúrate de que todos los archivos estén en el repositorio
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Deploy en Vercel

1. Ve a [vercel.com](https://vercel.com)
2. Conecta tu repositorio de GitHub
3. Vercel detectará automáticamente que es un proyecto Python
4. El archivo `vercel.json` ya está configurado
5. ¡Deploy automático!

### 3. Variables de entorno (Opcional)

En Vercel, puedes configurar:
- `DATABASE_URL`: Para usar una BD externa (opcional, por defecto usa SQLite)

## 📊 Datos Mock Incluidos

La API incluye datos de las siguientes criptomonedas:

- **BTC** - Bitcoin
- **ETH** - Ethereum  
- **BNB** - Binance Coin
- **SOL** - Solana
- **ADA** - Cardano
- **XRP** - Ripple
- **DOGE** - Dogecoin
- **MATIC** - Polygon
- **AVAX** - Avalanche
- **DOT** - Polkadot

## 🔧 Ejemplos de Uso

### 🌐 **URL Base de la API**
```
https://bitcoins-api.vercel.app
```

### 📱 **JavaScript/Web**

```javascript
// Obtener precio de Bitcoin
fetch('https://bitcoins-api.vercel.app/crypto/BTC')
  .then(response => response.json())
  .then(data => console.log(data));

// Top 10 criptomonedas
fetch('https://bitcoins-api.vercel.app/crypto/top/10')
  .then(response => response.json())
  .then(data => console.log(data));

// Comparar Bitcoin y Ethereum
fetch('https://bitcoins-api.vercel.app/crypto/compare/BTC/ETH')
  .then(response => response.json())
  .then(data => console.log(data));

// Todas las criptomonedas disponibles
fetch('https://bitcoins-api.vercel.app/crypto/')
  .then(response => response.json())
  .then(data => console.log(data));
```

### 🐍 **Python**

```python
import requests

# Obtener precio de Bitcoin
response = requests.get('https://bitcoins-api.vercel.app/crypto/BTC')
print(response.json())

# Top 5 criptomonedas
response = requests.get('https://bitcoins-api.vercel.app/crypto/top/5')
print(response.json())

# Comparar dos criptomonedas
response = requests.get('https://bitcoins-api.vercel.app/crypto/compare/BTC/ETH')
print(response.json())

# Todas las criptomonedas
response = requests.get('https://bitcoins-api.vercel.app/crypto/')
print(response.json())
```

### 💻 **cURL**

```bash
# Precio de Bitcoin
curl https://bitcoins-api.vercel.app/crypto/BTC

# Top 10 criptomonedas
curl https://bitcoins-api.vercel.app/crypto/top/10

# Comparar Bitcoin y Ethereum
curl https://bitcoins-api.vercel.app/crypto/compare/BTC/ETH

# Todas las criptomonedas
curl https://bitcoins-api.vercel.app/crypto/
```

### 📊 **Respuestas de Ejemplo**

#### **Obtener una criptomoneda:**
```json
{
  "success": true,
  "data": {
    "symbol": "BTC",
    "name": "Bitcoin",
    "price": 43500.00,
    "change_24h": 2.5,
    "market_cap": 850000000000
  },
  "message": "Precio actual de Bitcoin"
}
```

#### **Top criptomonedas:**
```json
{
  "success": true,
  "data": [
    {
      "symbol": "BTC",
      "name": "Bitcoin",
      "price": 43500.00,
      "change_24h": 2.5,
      "market_cap": 850000000000
    },
    {
      "symbol": "ETH",
      "name": "Ethereum",
      "price": 2680.00,
      "change_24h": -1.2,
      "market_cap": 320000000000
    }
  ],
  "message": "Top 2 criptomonedas por market cap"
}
```

#### **Comparar criptomonedas:**
```json
{
  "success": true,
  "data": {
    "crypto1": {
      "symbol": "BTC",
      "name": "Bitcoin",
      "price": 43500.00,
      "change_24h": 2.5,
      "market_cap": 850000000000
    },
    "crypto2": {
      "symbol": "ETH",
      "name": "Ethereum",
      "price": 2680.00,
      "change_24h": -1.2,
      "market_cap": 320000000000
    },
    "comparison": {
      "price_difference": 40820.0,
      "price_ratio": 16.23,
      "market_cap_difference": 530000000000,
      "change_24h_difference": 3.7
    }
  },
  "message": "Comparación entre Bitcoin y Ethereum"
}
```

## 🚀 **Guía Rápida para Desarrolladores**

### **🔗 URLs Principales**
- **API Base**: `https://bitcoins-api.vercel.app`
- **Documentación**: `https://bitcoins-api.vercel.app/docs`
- **Health Check**: `https://bitcoins-api.vercel.app/health`

### **📋 Endpoints Disponibles**
| Endpoint | Método | Descripción | Ejemplo |
|----------|--------|-------------|---------|
| `/crypto/{symbol}` | GET | Precio de una cripto | `/crypto/BTC` |
| `/crypto/top/{limit}` | GET | Top criptos por market cap | `/crypto/top/10` |
| `/crypto/compare/{symbol1}/{symbol2}` | GET | Comparar dos criptos | `/crypto/compare/BTC/ETH` |
| `/crypto/` | GET | Todas las criptos | `/crypto/` |

### **⚡ Uso Rápido**
```bash
# Test rápido
curl https://bitcoins-api.vercel.app/crypto/BTC

# En JavaScript
fetch('https://bitcoins-api.vercel.app/crypto/BTC')
  .then(r => r.json())
  .then(console.log)
```

## 📚 Documentación

La API incluye documentación completa:

- **🌐 Página principal**: [https://bitcoins-api.vercel.app/](https://bitcoins-api.vercel.app/) - Guía de uso HTML
- **📖 Swagger UI**: [https://bitcoins-api.vercel.app/docs](https://bitcoins-api.vercel.app/docs) - Documentación interactiva
- **📚 ReDoc**: [https://bitcoins-api.vercel.app/redoc](https://bitcoins-api.vercel.app/redoc) - Documentación alternativa
- **❤️ Health Check**: [https://bitcoins-api.vercel.app/health](https://bitcoins-api.vercel.app/health) - Estado de la API

## 🧪 Testing

### **Local:**
```bash
# Ejecutar con uv
uv run python main.py

# Test manual
curl http://localhost:8000/health
```

### **Producción:**
```bash
# Health check
curl https://bitcoins-api.vercel.app/health

# Test endpoints
curl https://bitcoins-api.vercel.app/crypto/BTC
curl https://bitcoins-api.vercel.app/crypto/top/5
curl https://bitcoins-api.vercel.app/crypto/compare/BTC/ETH
```

## 🔒 Consideraciones de Seguridad

- ✅ **CORS habilitado** - Acceso desde cualquier origen
- ✅ **Datos mock** - No hay información real de mercado
- ✅ **Sin autenticación** - API pública para testing
- ✅ **Rate limiting** - Considera implementar en producción
- ✅ **HTTPS** - Comunicación segura en Vercel

## 📈 Próximas Mejoras

- [ ] **Integración con API real** - CoinGecko, CoinMarketCap
- [ ] **Autenticación JWT** - Para endpoints protegidos
- [ ] **Rate limiting** - Control de requests por IP
- [ ] **Cache con Redis** - Mejor rendimiento
- [ ] **Tests unitarios** - pytest y coverage
- [ ] **Logging estructurado** - Monitoreo de errores
- [ ] **Métricas** - Prometheus y Grafana
- [ ] **WebSocket** - Precios en tiempo real
- [ ] **Histórico de precios** - Base de datos temporal

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
