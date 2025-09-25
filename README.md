# 🚀 Bitcoins API

API REST robusta para consultar precios de criptomonedas construida con FastAPI, SQLite y arquitectura clean usando **uv**.

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
- ✅ **Base de datos SQLite**: Persistencia de datos mock
- ✅ **FastAPI**: Framework moderno y rápido
- ✅ **CORS habilitado**: Acceso desde cualquier dispositivo
- ✅ **Documentación automática**: Swagger UI y ReDoc
- ✅ **Deploy en Vercel**: Configuración lista para producción
- ✅ **Manejo de errores**: Respuestas consistentes y descriptivas
- ✅ **Gestionado con uv**: Gestión moderna de dependencias

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

### JavaScript/Web

```javascript
// Obtener precio de Bitcoin
fetch('https://tu-api.vercel.app/crypto/BTC')
  .then(response => response.json())
  .then(data => console.log(data));

// Top 10 criptomonedas
fetch('https://tu-api.vercel.app/crypto/top/10')
  .then(response => response.json())
  .then(data => console.log(data));

// Comparar Bitcoin y Ethereum
fetch('https://tu-api.vercel.app/crypto/compare/BTC/ETH')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python

```python
import requests

# Obtener precio de Bitcoin
response = requests.get('https://tu-api.vercel.app/crypto/BTC')
print(response.json())

# Top 5 criptomonedas
response = requests.get('https://tu-api.vercel.app/crypto/top/5')
print(response.json())
```

### cURL

```bash
# Precio de Bitcoin
curl https://tu-api.vercel.app/crypto/BTC

# Top 10
curl https://tu-api.vercel.app/crypto/top/10

# Comparar
curl https://tu-api.vercel.app/crypto/compare/BTC/ETH
```

## 📚 Documentación

Una vez desplegada, la API incluye:

- **Swagger UI**: `/docs` - Documentación interactiva
- **ReDoc**: `/redoc` - Documentación alternativa
- **Página principal**: `/` - Guía de uso HTML

## 🧪 Testing

```bash
# Ejecutar con uv
uv run python main.py

# Test manual
curl http://localhost:8000/health
```

## 🔒 Consideraciones de Seguridad

- CORS configurado para permitir acceso desde cualquier origen
- En producción, considera restringir orígenes específicos
- Los datos son mock, no hay información real de mercado
- SQLite es adecuado para desarrollo y testing

## 📈 Próximas Mejoras

- [ ] Integración con API real de criptomonedas
- [ ] Autenticación y autorización
- [ ] Rate limiting
- [ ] Cache con Redis
- [ ] Tests unitarios y de integración
- [ ] Logging estructurado
- [ ] Métricas y monitoreo

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
