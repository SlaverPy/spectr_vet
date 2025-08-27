from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime


class SpecialistBase(BaseModel):
    """Базовая схема специалиста."""
    first_name: str = Field(..., max_length=50, description="Имя специалиста")
    last_name: str = Field(..., max_length=50, description="Фамилия специалиста")
    patronymic: str | None = Field(None, max_length=50, description="Отчество специалиста")
    specialization: str = Field(..., max_length=100, description="Специализация")
    experience: int | None = Field(None, ge=0, description="Опыт работы в годах")
    description: str | None = Field(None, description="Подробное описание")
    photo_url: str | None = Field(None, description="URL фотографии")
    service_ids: List[int] | None = Field(None, description="ID услуг, которые предоставляет специалист")


class SpecialistCreate(SpecialistBase):
    """Схема для создания специалиста."""
    clinic_id: int = Field(..., description="ID клиники")


class Specialist(SpecialistBase):
    """Схема для возврата специалиста."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    clinic_id: int
    created_at: datetime
    updated_at: datetime | None
    services: List["ServiceShort"] = Field(..., description="Услуги, которые предоставляет специалист")


# Добавляем короткую схему для услуги
class ServiceShort(BaseModel):
    """Короткая схема услуги для вложений."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    duration_minutes: int | None
    category: str