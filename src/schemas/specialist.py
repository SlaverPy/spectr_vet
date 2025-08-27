from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationInfo
from typing import List, Optional
from datetime import datetime


class SpecialistBase(BaseModel):
    """Базовая схема специалиста."""
    first_name: str = Field(..., max_length=50, description="Имя специалиста")
    last_name: str = Field(..., max_length=50, description="Фамилия специалиста")
    patronymic: Optional[str] = Field(None, max_length=50, description="Отчество специалиста")
    specialization: str = Field(..., max_length=100, description="Специализация")
    experience: Optional[int] = Field(None, ge=0, le=100, description="Опыт работы в годах")
    description: Optional[str] = Field(None, description="Подробное описание")
    photo_url: Optional[str] = Field(None, description="URL фотографии")
    service_ids: Optional[List[int]] = Field(None, description="ID услуг, которые предоставляет специалист")

    @field_validator('photo_url')
    @classmethod
    def validate_photo_url(cls, v: Optional[str]) -> Optional[str]:
        """Валидация URL фотографии."""
        if v and not v.startswith(('http://', 'https://', '/')):
            raise ValueError("URL фотографии должен начинаться с http://, https:// или /")
        return v

    @field_validator('experience')
    @classmethod
    def validate_experience(cls, v: Optional[int]) -> Optional[int]:
        """Валидация опыта работы."""
        if v is not None and (v < 0 or v > 100):
            raise ValueError("Опыт работы должен быть от 0 до 100 лет")
        return v


class SpecialistCreate(SpecialistBase):
    """Схема для создания специалиста."""
    clinic_id: int = Field(..., description="ID клиники")


class SpecialistUpdate(BaseModel):
    """Схема для обновления специалиста."""
    first_name: Optional[str] = Field(None, max_length=50, description="Имя специалиста")
    last_name: Optional[str] = Field(None, max_length=50, description="Фамилия специалиста")
    patronymic: Optional[str] = Field(None, max_length=50, description="Отчество специалиста")
    specialization: Optional[str] = Field(None, max_length=100, description="Специализация")
    experience: Optional[int] = Field(None, ge=0, le=100, description="Опыт работы в годах")
    description: Optional[str] = Field(None, description="Подробное описание")
    photo_url: Optional[str] = Field(None, description="URL фотографии")
    service_ids: Optional[List[int]] = Field(None, description="ID услуг, которые предоставляет специалист")


class Specialist(SpecialistBase):
    """Схема для возврата специалиста."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    clinic_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    services: List["ServiceShort"] = Field(..., description="Услуги, которые предоставляет специалист")


class ServiceShort(BaseModel):
    """Короткая схема услуги для вложений."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    duration_minutes: Optional[int] = None
    category: str


class SpecialistWithClinic(Specialist):
    """Схема специалиста с информацией о клинике."""
    clinic_name: str = Field(..., description="Название клиники")
    clinic_address: str = Field(..., description="Адрес клиники")
    clinic_phone: str = Field(..., description="Телефон клиники")
