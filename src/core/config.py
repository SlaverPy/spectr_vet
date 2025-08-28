import os
import sys
from typing import Optional
from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


class Settings(BaseSettings):
    """Базовые настройки приложения."""

    # Режим работы
    ENV: str = "development"  # development, testing, production
    DEBUG: bool = True

    # Настройки базы данных
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "vet_clinic"
    DB_USER: str = "user"
    DB_PASSWORD: str = "password"
    DB_ECHO: bool = False

    # Генерируемый URL базы данных
    DATABASE_URL: Optional[PostgresDsn] = None

    # JWT настройки
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> str:
        """Собирает URL подключения к базе данных."""
        if isinstance(v, str):
            return v

        values = info.data
        # Для тестовой среды используем другую базу
        if values.get("ENV") == "testing":
            db_name = f"test_{values.get('DB_NAME')}"
        else:
            db_name = values.get("DB_NAME")

        return f"postgresql+asyncpg://{values.get('DB_USER')}:{values.get('DB_PASSWORD')}@{values.get('DB_HOST')}:{values.get('DB_PORT')}/{db_name}"

    @field_validator("DB_ECHO")
    @classmethod
    def set_db_echo_based_on_env(cls, v: bool, info: ValidationInfo) -> bool:
        """Устанавливает echo на основе окружения."""
        values = info.data
        env = values.get("ENV")
        if env == "development":
            return True
        elif env == "testing":
            return False
        return v

    @field_validator("DEBUG")
    @classmethod
    def set_debug_based_on_env(cls, v: bool, info: ValidationInfo) -> bool:
        """Устанавливает debug на основе окружения."""
        values = info.data
        env = values.get("ENV")
        if env == "development":
            return True
        elif env == "testing":
            return False
        return v


class DevelopmentConfig(Settings):
    """Конфигурация для разработки."""

    class Config:
        env_prefix = "DEV_"

    def __init__(self, **kwargs):
        kwargs.setdefault('ENV', 'development')
        kwargs.setdefault('DEBUG', True)
        kwargs.setdefault('DB_ECHO', True)
        super().__init__(**kwargs)


class TestingConfig(Settings):
    """Конфигурация для тестирования."""

    class Config:
        env_prefix = "TEST_"

    def __init__(self, **kwargs):
        kwargs.setdefault('ENV', 'testing')
        kwargs.setdefault('DEBUG', False)
        kwargs.setdefault('DB_ECHO', False)
        super().__init__(**kwargs)


class ProductionConfig(Settings):
    """Конфигурация для продакшена."""

    class Config:
        env_prefix = "PROD_"

    def __init__(self, **kwargs):
        kwargs.setdefault('ENV', 'production')
        kwargs.setdefault('DEBUG', False)
        kwargs.setdefault('DB_ECHO', False)
        super().__init__(**kwargs)


def get_config(env: Optional[str] = None) -> Settings:
    """Возвращает конфигурацию в зависимости от окружения."""
    if env is None:
        # Сначала проверяем аргументы командной строки
        if len(sys.argv) > 1:
            env = sys.argv[1].lower()
        # Затем переменные окружения
        else:
            env = os.getenv("ENV", "development").lower()

    config_map = {
        "dev": DevelopmentConfig,
        "development": DevelopmentConfig,
        "test": TestingConfig,
        "testing": TestingConfig,
        "prod": ProductionConfig,
        "production": ProductionConfig,
    }

    config_class = config_map.get(env, DevelopmentConfig)
    return config_class()


# Глобальный экземпляр конфигурации (будет создан при первом импорте)
config = None

def init_config(env: Optional[str] = None):
    """Инициализирует конфигурацию (вызывается явно)."""
    global config
    config = get_config(env)
    return config