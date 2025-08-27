from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Optional


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей SQLAlchemy.
    Предоставляет метаданные и общую конфигурацию для всех таблиц.
    """
    pass


class BaseModel(Base):
    """
    Абстрактная базовая модель со стандартными полями.
    Все модели должны наследоваться от этого класса.

    Attributes:
        id (int): Уникальный идентификатор записи (первичный ключ)
        created_at (datetime): Дата и время создания записи
        updated_at (Optional[datetime]): Дата и время последнего обновления записи
    """
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )