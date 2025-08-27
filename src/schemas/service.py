from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationInfo
from datetime import datetime
from typing import List, Optional
from enum import Enum


class ServiceCategory(Enum):
    CONSULTATION = "consultation"
    DIAGNOSTICS = "diagnostics"
    TREATMENT = "treatment"
    SURGERY = "surgery"
    VACCINATION = "vaccination"
    GROOMING = "grooming"
    HOSPITALIZATION = "hospitalization"
    OTHER = "other"


class ServiceStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class ServiceBase(BaseModel):
    """Базовая схема услуги."""
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

    @field_validator('min_price', 'max_price')
    @classmethod
    def validate_price_range(cls, v: Optional[float], info: ValidationInfo) -> Optional[float]:
        """Валидация диапазона цен."""
        if v is not None:
            data = info.data
            price = data.get('price')
            if price is not None:
                if 'min_price' in info.field_name and v > price:
                    raise ValueError("Минимальная цена не может быть больше базовой")
                if 'max_price' in info.field_name and v < price:
                    raise ValueError("Максимальная цена не может быть меньше базовой")
        return v

    @field_validator('min_duration', 'max_duration')
    @classmethod
    def validate_duration_range(cls, v: Optional[int], info: ValidationInfo) -> Optional[int]:
        """Валидация диапазона продолжительности."""
        if v is not None:
            data = info.data
            duration = data.get('duration_minutes')
            if duration is not None:
                if 'min_duration' in info.field_name and v > duration:
                    raise ValueError("Минимальная продолжительность не может быть больше базовой")
                if 'max_duration' in info.field_name and v < duration:
                    raise ValueError("Максимальная продолжительность не может быть меньше базовой")
        return v


class ServiceCreate(ServiceBase):
    """Схема для создания услуги."""
    clinic_id: int = Field(..., description="ID клиники")


class ServiceUpdate(BaseModel):
    """Схема для обновления услуги."""
    name: Optional[str] = Field(None, max_length=100, description="Название услуги")
    short_description: Optional[str] = Field(None, max_length=200, description="Краткое описание")
    description: Optional[str] = Field(None, description="Подробное описание")
    price: Optional[float] = Field(None, ge=0, description="Базовая стоимость")
    min_price: Optional[float] = Field(None, ge=0, description="Минимальная цена")
    max_price: Optional[float] = Field(None, ge=0, description="Максимальная цена")
    duration_minutes: Optional[int] = Field(None, ge=1, description="Продолжительность в минутах")
    min_duration: Optional[int] = Field(None, ge=1, description="Минимальная продолжительность")
    max_duration: Optional[int] = Field(None, ge=1, description="Максимальная продолжительность")
    category: Optional[ServiceCategory] = Field(None, description="Категория услуги")
    status: Optional[ServiceStatus] = Field(None, description="Статус услуги")
    is_popular: Optional[bool] = Field(None, description="Популярная услуга")
    is_available_online: Optional[bool] = Field(None, description="Доступна онлайн")
    is_emergency: Optional[bool] = Field(None, description="Экстренная услуга")
    preparation_info: Optional[str] = Field(None, description="Информация о подготовке")
    contraindications: Optional[str] = Field(None, description="Противопоказания")
    required_specializations: Optional[List[str]] = Field(None, description="Требуемые специализации")
    tags: Optional[List[str]] = Field(None, description="Теги для поиска")
    image_url: Optional[str] = Field(None, description="URL изображения")
    gallery: Optional[List[str]] = Field(None, description="Галерея изображений")
    order_index: Optional[int] = Field(None, ge=0, description="Порядковый индекс")
    specialist_ids: Optional[List[int]] = Field(None, description="ID специалистов, предоставляющих услугу")


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


class SpecialistShort(BaseModel):
    """Короткая схема специалиста для вложений."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    specialization: str
    photo_url: str | None
