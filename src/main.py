from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import sys
import uvicorn

# Импортируем config с возможностью инициализации
from src.core.config import init_config

# Получаем режим из аргументов командной строки
env = sys.argv[1] if len(sys.argv) > 1 else None

# Инициализируем конфигурацию
config = init_config(env)

app = FastAPI(
    title="Vet Clinic API",
    description="API для ветеринарной клиники",
    version="1.0.0",
    debug=config.DEBUG
)

# Mount static files
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Include routers
from src.views.main import router as main_router

app.include_router(main_router)


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Vet Clinic API is running",
        "environment": config.ENV,
        "debug": config.DEBUG
    }


# Запуск приложения
if __name__ == "__main__":
    print("🚀 Запуск Vet Clinic API...")
    print(f"📊 Режим: {config.ENV}")
    print(f"🐛 Debug: {config.DEBUG}")
    print(f"🗄️  DB Echo: {config.DB_ECHO}")
    print(f"🔗 Database: {config.DATABASE_URL}")
    print(f"📖 Документация: http://localhost:8000/api/docs")
    print(f"🌐 Главная: http://localhost:8000/")

    # Правильный вызов uvicorn с reload
    if config.DEBUG:
        # Development режим - с reload
        uvicorn.run(
            "src.main:app",  # Передаем как строку импорта
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="debug"
        )
    else:
        # Production/Testing режим - без reload
        uvicorn.run(
            app,  # Можно передавать объект
            host="0.0.0.0",
            port=8000,
            log_level="info"
        )