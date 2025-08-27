from pydantic import BaseModel, Field, ConfigDict, validator, field_validator
from datetime import datetime
from typing import List, Optional
from enum import Enum


class DiscountType(str, Enum):
    PERCENTAGE = "percentage"
    FIXED = "fixed"
    GIFT = "gift"
    SPECIAL = "special"


class PromotionBase(BaseModel):
    """Базовая схема акции."""
    title: str = Field(..., max_length=200, description="Заголовок акции")
    short_description: str | None = Field(None, max_length=300, description="Краткое описание")
    description: str | None = Field(None, description="Подробное описание с HTML")
    discount_type: DiscountType = Field(default=DiscountType.PERCENTAGE, description="Тип скидки")
    discount_value: float | None = Field(None, ge=0, description="Значение скидки")
    original_price: float | None = Field(None, ge=0, description="Исходная цена")
    final_price: float | None = Field(None, ge=0, description="Финальная цена")
    start_date: datetime = Field(..., description="Дата начала акции")
    end_date: datetime = Field(..., description="Дата окончания акции")
    image_url: str | None = Field(None, description="URL основного изображения")
    gallery: List[str] | None = Field(None, description="Массив URL дополнительных изображений")
    is_active: bool = Field(default=True, description="Активна ли акция")
    is_featured: bool = Field(default=False, description="Выделенная акция")
    conditions: str | None = Field(None, description="Условия акции")
    promo_code: str | None = Field(None, max_length=50, description="Промокод")
    clinic_id: int | None = Field(None, description="ID клиники")
    service_ids: List[int] | None = Field(None, description="ID услуг")

    @field_validator('end_date')
    @classmethod
    def validate_end_date(cls, v: datetime, values):
        """Валидация даты окончания."""
        start_date = values.data.get('start_date')
        if start_date and v <= start_date:
            raise ValueError("Дата окончания должна быть после даты начала")
        return v

    @field_validator('discount_value')
    @classmethod
    def validate_discount_value(cls, v: float | None, values):
        """Валидация значения скидки."""
        discount_type = values.data.get('discount_type')

        if discount_type == DiscountType.PERCENTAGE and v is not None:
            if v > 100:
                raise ValueError("Процент скидки не может превышать 100%")
            if v <= 0:
                raise ValueError("Процент скидки должен быть положительным")

        elif discount_type == DiscountType.FIXED and v is not None:
            if v <= 0:
                raise ValueError("Фиксированная скидка должна быть положительной")

        return v

    @field_validator('image_url', 'gallery')
    @classmethod
    def validate_image_urls(cls, v, values):
        """Валидация URL изображений."""
        if isinstance(v, str):
            if v and not v.startswith(('http://', 'https://', '/media/')):
                raise ValueError("URL изображения должен начинаться с http://, https:// или /media/")
        elif isinstance(v, list):
            for url in v:
                if url and not url.startswith(('http://', 'https://', '/media/')):
                    raise ValueError("URL изображения должен начинаться с http://, https:// или /media/")
        return v


class PromotionCreate(PromotionBase):
    """Схема для создания акции."""
    pass


class PromotionUpdate(BaseModel):
    """Схема для обновления акции."""
    title: str | None = Field(None, max_length=200, description="Заголовок акции")
    short_description: str | None = Field(None, max_length=300, description="Краткое описание")
    description: str | None = Field(None, description="Подробное описание")
    discount_type: DiscountType | None = Field(None, description="Тип скидки")
    discount_value: float | None = Field(None, ge=0, description="Значение скидки")
    original_price: float | None = Field(None, ge=0, description="Исходная цена")
    final_price: float | None = Field(None, ge=0, description="Финальная цена")
    start_date: datetime | None = Field(None, description="Дата начала")
    end_date: datetime | None = Field(None, description="Дата окончания")
    image_url: str | None = Field(None, description="URL изображения")
    gallery: List[str] | None = Field(None, description="Галерея изображений")
    is_active: bool | None = Field(None, description="Активна ли акция")
    is_featured: bool | None = Field(None, description="Выделенная акция")
    conditions: str | None = Field(None, description="Условия акции")
    promo_code: str | None = Field(None, max_length=50, description="Промокод")
    clinic_id: int | None = Field(None, description="ID клиники")
    service_ids: List[int] | None = Field(None, description="ID услуг")


class Promotion(PromotionBase):
    """Схема для возврата акции."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime | None


class PromotionWithClinic(Promotion):
    """Схема акции с информацией о клинике."""
    clinic_name: str | None = Field(None, description="Название клиники")
    clinic_address: str | None = Field(None, description="Адрес клиники")
