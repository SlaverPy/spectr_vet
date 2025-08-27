from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from .base import BaseModel
from .service_specialist import service_specialist  # Импортируем таблицу связи


class Specialist(BaseModel):
    """
    Модель ветеринарного специалиста.

    Представляет сотрудника ветеринарной клиники с профессиональной информацией
    и связью с конкретной клиникой и услугами.
    """
    __tablename__ = "specialists"

    first_name: Mapped[str] = mapped_column(String(50), doc="Имя специалиста (макс. 50 символов)")
    last_name: Mapped[str] = mapped_column(String(50), doc="Фамилия специалиста (макс. 50 символов)")
    patronymic: Mapped[str | None] = mapped_column(String(50), nullable=True,
                                                   doc="Отчество специалиста (макс. 50 символов)")
    specialization: Mapped[str] = mapped_column(String(100), doc="Специализация (макс. 100 символов)")
    experience: Mapped[int | None] = mapped_column(Integer, nullable=True, doc="Опыт работы в годах")
    description: Mapped[str | None] = mapped_column(Text, nullable=True, doc="Подробное описание специалиста")
    photo_url: Mapped[str | None] = mapped_column(String(255), nullable=True, doc="URL фотографии (макс. 255 символов)")

    # Foreign key
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), doc="ID клиники, к которой привязан специалист")

    # Relationships
    clinic: Mapped["Clinic"] = relationship(back_populates="specialists",
                                            doc="Объект клиники, к которой привязан специалист")

    # Связь многие-ко-многим с услугами
    services: Mapped[list["Service"]] = relationship(
        "Service",
        secondary=service_specialist,
        back_populates="specialists",
        doc="Услуги, которые предоставляет специалист"
    )