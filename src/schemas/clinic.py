from pydantic import BaseModel, Field, validator, ConfigDict, HttpUrl
from datetime import time, datetime
from typing import Optional, Any


class ClinicBase(BaseModel):
    """Базовая схема клиники."""
    name: str = Field(..., max_length=100, description="Название клиники")
    address: str = Field(..., description="Полный адрес клиники")
    phone_number: str = Field(..., max_length=20, description="Контактный телефон")
    email: str = Field(..., max_length=100, description="Email адрес")
    is_24_7: bool = Field(default=False, description="Круглосуточная работа")
    start_time: time | None = Field(None, description="Время начала работы")
    end_time: time | None = Field(None, description="Время окончания работы")
    map_url: str | None = Field(
        None,
        max_length=500,
        description="Ссылка на схему проезда (URL карты или навигационного сервиса)"
    )
    description: str | None = Field(None, description="Описание клиники")
    is_active: bool = Field(default=True, description="Активна ли клиника")

    @validator('start_time', 'end_time')
    def validate_working_hours(cls, v: Optional[time], values: dict[str, Any]) -> Optional[time]:
        """Валидация времени работы."""
        is_24_7 = values.get('is_24_7', False)

        if is_24_7 and v is not None:
            raise ValueError("Время работы не должно указываться для круглосуточной клиники")

        if not is_24_7 and v is None:
            raise ValueError("Время работы обязательно для не круглосуточных клиник")

        return v

    @validator('end_time')
    def validate_end_time(cls, v: Optional[time], values: dict[str, Any]) -> Optional[time]:
        """Валидация что время окончания после времени начала."""
        start_time = values.get('start_time')
        is_24_7 = values.get('is_24_7', False)

        if not is_24_7 and start_time and v and v <= start_time:
            raise ValueError("Время окончания должно быть после времени начала")

        return v

    @validator('map_url')
    def validate_map_url(cls, v: Optional[str]) -> Optional[str]:
        """Валидация ссылки на карту."""
        if v and not v.startswith(('http://', 'https://', 'yandexmaps://', 'yandexnavi://')):
            raise ValueError("Ссылка на карту должна начинаться с http://, https:// или навигационного протокола")
        return v


class ClinicCreate(ClinicBase):
    """Схема для создания клиники."""
    pass


class ClinicUpdate(BaseModel):
    """Схема для обновления клиники."""
    name: Optional[str] = Field(None, max_length=100, description="Название клиники")
    address: Optional[str] = Field(None, description="Полный адрес клиники")
    phone_number: Optional[str] = Field(None, max_length=20, description="Контактный телефон")
    email: Optional[str] = Field(None, max_length=100, description="Email адрес")
    is_24_7: Optional[bool] = Field(None, description="Круглосуточная работа")
    start_time: Optional[time] = Field(None, description="Время начала работы")
    end_time: Optional[time] = Field(None, description="Время окончания работы")
    map_url: Optional[str] = Field(
        None,
        max_length=500,
        description="Ссылка на схему проезда (URL карты или навигационного сервиса)"
    )
    description: Optional[str] = Field(None, description="Описание клиники")
    is_active: Optional[bool] = Field(None, description="Активна ли клиника")


class Clinic(ClinicBase):
    """Схема для возврата клиники."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime]