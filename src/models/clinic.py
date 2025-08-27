from sqlalchemy import String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from .base import BaseModel


class Clinic(BaseModel):
    """
    Модель ветеринарной клиники.

    Представляет собой физическую или юридическую единицу ветеринарной клиники
    с полной контактной информацией и описанием.
    """
    __tablename__ = "clinics"

    name: Mapped[str] = mapped_column(String(100), index=True, doc="Название клиники (макс. 100 символов)")
    address: Mapped[str] = mapped_column(Text, doc="Полный адрес клиники")
    phone_number: Mapped[str] = mapped_column(String(20), doc="Контактный телефон (макс. 20 символов)")
    email: Mapped[str] = mapped_column(String(100), doc="Email адрес (макс. 100 символов)")
    is_24_7: Mapped[bool] = mapped_column(
        default=False,
        doc="Флаг круглосуточной работы. Если True, поля start_time и end_time игнорируются"
    )
    map_url: Mapped[Optional[str]] = mapped_column(String(500), doc="Ссылка URL карты или навигационного сервиса")
    start_time: Mapped[str | None] = mapped_column(Time, doc="Время начала работы в формате HH:MM.")
    end_time: Mapped[str | None] = mapped_column(Time, doc="Время окончания работы в формате HH:MM.")
    description: Mapped[Optional[str]] = mapped_column(Text, doc="Подробное описание клиники")
    is_active: Mapped[bool] = mapped_column(default=True, doc="Флаг активности клиники (True/False)")

    # Relationships
    specialists: Mapped[list["Specialist"]] = relationship(
        back_populates="clinic",
        cascade="all, delete-orphan",
        doc="Список специалистов клиники"
    )
    services: Mapped[list["Service"]] = relationship(
        back_populates="clinic",
        cascade="all, delete-orphan",
        doc="Список услуг клиники"
    )
