from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Создаем router
router = APIRouter(tags=["Main"])

# Настраиваем templates
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Ветеринарная клиника"}
    )

# @router.get("/clinics", response_class=HTMLResponse)
# async def clinics_page(request: Request):
#     """Страница клиник."""
#     return templates.TemplateResponse(
#         "clinics.html",
#         {"request": request, "title": "Клиники"}
#     )
#
# @router.get("/services", response_class=HTMLResponse)
# async def services_page(request: Request):
#     """Страница услуг."""
#     return templates.TemplateResponse(
#         "services.html",
#         {"request": request, "title": "Услуги"}
#     )
#
# @router.get("/specialists", response_class=HTMLResponse)
# async def specialists_page(request: Request):
#     """Страница специалистов."""
#     return templates.TemplateResponse(
#         "specialists.html",
#         {"request": request, "title": "Специалисты"}
#     )
#
# @router.get("/login", response_class=HTMLResponse)
# async def login_page(request: Request):
#     """Страница входа."""
#     return templates.TemplateResponse(
#         "login.html",
#         {"request": request, "title": "Вход в систему"}
#     )
#
# @router.get("/register", response_class=HTMLResponse)
# async def register_page(request: Request):
#     """Страница регистрации."""
#     return templates.TemplateResponse(
#         "register.html",
#         {"request": request, "title": "Регистрация"}
#     )
