from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Создаем экземпляр приложения
app = FastAPI(title="VetClinic", debug=True)

# Настраиваем пути
BASE_DIR = Path(__file__).resolve().parent

# Монтируем статические файлы ПРАВИЛЬНО
app.mount("src/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Настраиваем шаблоны
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Простой асинхронный эндпоинт возвращающий HTML страницу
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница ветеринарной клиники
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Ветеринарная клиника Друг",
            "message": "Добро пожаловать в нашу клинику!"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )