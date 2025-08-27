from pydantic import BaseModel, Field, ConfigDict, validator, field_validator
from datetime import datetime
from typing import List, Optional
from enum import Enum


# ... остальные импорты и enum классы ...

class ServiceBase(BaseModel):
    """Базовая схема услуги."""
    # ... остальные поля без изменений ...
    name: str = Field(..., max_length=100, description="Название услуги")
    short_description: str | None = Field(None, max_length=200, description="Краткое описание")
    description: str | None = Field(None, description="Подробное описание")
    price: float = Field(..., ge=0, description="Базовая стоимость")
    min_price: float | None = Field(None, ge=0, description="Минимальная цена")
    max_price: float | None = Field(None, ge=0, description="Максимальная цена")
    duration_minutes: int | None = Field(None, ge=1, description="Продолжительность в минутах")
    min_duration: int | None = Field(None, ge=1, description="Минимальная продолжительность")
    max_duration: int | None = Field(None, ge=1, description="Максимальная продолжительность")
    category: ServiceCategory = Field(default=ServiceCategory.OTHER, description="Категория услуги")
    status: ServiceStatus = Field(default=ServiceStatus.ACTIVE, description="Статус услуги")
    is_popular: bool = Field(default=False, description="Популярная услуга")
    is_available_online: bool = Field(default=False, description="Доступна онлайн")
    is_emergency: bool = Field(default=False, description="Экстренная услуга")
    preparation_info: str | None = Field(None, description="Информация о подготовке")
    contraindications: str | None = Field(None, description="Противопоказания")
    required_specializations: List[str] | None = Field(None, description="Требуемые специализации")
    tags: List[str] | None = Field(None, description="Теги для поиска")
    image_url: str | None = Field(None, description="URL изображения")
    gallery: List[str] | None = Field(None, description="Галерея изображений")
    order_index: int = Field(default=0, ge=0, description="Порядковый индекс")
    specialist_ids: List[int] | None = Field(None, description="ID специалистов, предоставляющих услугу")


class ServiceCreate(ServiceBase):
    """Схема для создания услуги."""
    clinic_id: int = Field(..., description="ID клиники")


class ServiceUpdate(BaseModel):
    """Схема для обновления услуги."""
    # ... остальные поля ...
    specialist_ids: List[int] | None = Field(None, description="ID специалистов")


class Service(ServiceBase):
    """Схема для возврата услуги."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    clinic_id: int
    created_at: datetime
    updated_at: datetime | None
    specialists: List["SpecialistShort"] = Field(..., description="Специалисты, предоставляющие услугу")


class ServiceWithClinic(Service):
    """Схема услуги с информацией о клинике."""
    clinic_name: str = Field(..., description="Название клиники")
    clinic_address: str = Field(..., description="Адрес клиники")
    clinic_phone: str = Field(..., description="Телефон клиники")


# Добавляем короткую схему для специалиста
class SpecialistShort(BaseModel):
    """Короткая схема специалиста для вложений."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    specialization: str
    photo_url: str | None