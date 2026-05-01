# Bot de Telegram - Mini Asistente

Bot conversacional para Telegram desarrollado en Python como proyecto académico para la asignatura de Inteligencia Artificial 1.

## 📋 Comandos disponibles

- `/hola` - Saludo básico del bot
- `/hora` - Muestra la hora actual del sistema
- `/contacto` - Información de contacto (correo de contacto)
- `/proyecto` - Descripción breve del proyecto

## 🚀 Requisitos previos

- Python 3.7 o superior
- Acceso a internet
- Token de bot de Telegram (obtenido de BotFather)

## 📦 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd tu_carpeta_del_proyecto
```

### 2. Crear un ambiente virtual (recomendado)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

- Copia el archivo `.env.example` y renómbralo a `.env`
- Obtén tu token de BotFather en Telegram (@BotFather)
- Reemplaza `YOUR_BOT_TOKEN` en el archivo `.env` con tu token real

**Archivo `.env` (no compartir):**
```
BOT_TOKEN=tu_token_aqui
```

## 🎯 Ejecución

```bash
python bot.py
```

El bot mostrará el mensaje: "Bot iniciado. Presiona Ctrl+C para detener."

Para detener el bot: **Ctrl+C**

## 📁 Estructura del proyecto

```
.
├── bot.py              # Archivo principal del bot
├── .env                # Variables de entorno (no versionado)
├── .env.example        # Plantilla de .env
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## ⚙️ Cómo obtener el TOKEN de Telegram

1. Abre Telegram y busca a **@BotFather**
2. Envía el comando `/newbot`
3. Sigue las instrucciones (nombre y nombre de usuario del bot)
4. Copia el token generado
5. Pégalo en el archivo `.env`

## 🔒 Consideraciones de seguridad

- **NUNCA** compartas tu archivo `.env` en repositorios públicos
- El archivo `.env` está incluido en `.gitignore` por defecto
- Usa `pip freeze > requirements.txt` para actualizar dependencias

## 🛠️ Tecnologías utilizadas

- **Python 3** - Lenguaje principal
- **requests** - Para comunicación con la API de Telegram
- **python-dotenv** - Para gestión de variables de entorno

## 📝 Notas

- El bot usa **polling** para recibir actualizaciones (no webhooks)
- Manejo básico de errores incluido
- Código modular y comentado para fácil comprensión

## 👥 Autores

Proyecto desarrollado para el curso de Inteligencia Artificial 1.

## 📄 Licencia

Este proyecto es académico y se proporciona como referencia educativa.
