from pydantic import BaseModel, Field, ConfigDict, validator, field_validator
from datetime import datetime
from typing import List, Optional
from enum import StrEnum
import json


class ImagePosition(str, StrEnum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


class NewsBlockBase(BaseModel):
    """Базовая схема блока новости."""
    title: str | None = Field(None, max_length=200, description="Заголовок блока")
    text_content: str | None = Field(None, description="Текстовое содержание блока")
    image_url: str | None = Field(None, description="URL изображения")
    image_position: ImagePosition | None = Field(
        None,
        description="Позиция изображения относительно текста (только если есть оба элемента)"
    )
    order: int = Field(0, ge=0, description="Порядок блока (начиная с 0)")
    meta: dict | None = Field(None, description="Дополнительные метаданные")

    @field_validator('image_url')
    @classmethod
    def validate_image_url(cls, v: str | None) -> str | None:
        """Валидация URL изображения."""
        if v and not v.startswith(('http://', 'https://', '/media/')):
            raise ValueError("URL изображения должен начинаться с http://, https:// или /media/")
        return v

    @field_validator('image_position')
    @classmethod
    def validate_image_position(cls, v: ImagePosition | None, values):
        """Валидация позиции изображения."""
        text_content = values.data.get('text_content')
        image_url = values.data.get('image_url')

        if v is not None:
            if not text_content or not image_url:
                raise ValueError("Позиция изображения может быть указана только если есть и текст и изображение")
        return v

    @field_validator('meta')
    @classmethod
    def validate_meta(cls, v: dict | None) -> dict | None:
        """Валидация метаданных."""
        if v is not None:
            try:
                json.dumps(v)  # Проверяем что можно сериализовать в JSON
            except TypeError:
                raise ValueError("Meta должен быть валидным JSON-объектом")
        return v


class NewsBlockCreate(NewsBlockBase):
    """Схема для создания блока новости."""
    pass


class NewsBlockUpdate(BaseModel):
    """Схема для обновления блока новости."""
    title: str | None = Field(None, max_length=200, description="Заголовок блока")
    text_content: str | None = Field(None, description="Текстовое содержание блока")
    image_url: str | None = Field(None, description="URL изображения")
    image_position: ImagePosition | None = Field(
        None,
        description="Позиция изображения относительно текста"
    )
    order: int | None = Field(None, ge=0, description="Порядок блока")
    meta: dict | None = Field(None, description="Дополнительные метаданные")


class NewsBlock(NewsBlockBase):
    """Схема для возврата блока новости."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    news_id: int
    created_at: datetime
    updated_at: datetime | None


class NewsBase(BaseModel):
    """Базовая схема новости."""
    title: str = Field(..., max_length=200, description="Заголовок новости")
    excerpt: str | None = Field(None, description="Краткое описание новости")
    cover_image: str | None = Field(None, description="URL обложки новости")
    is_published: bool = Field(default=False, description="Флаг публикации")
    blocks: List[NewsBlockCreate] = Field(..., description="Блоки новости")

    @field_validator('cover_image')
    @classmethod
    def validate_cover_image(cls, v: str | None) -> str | None:
        """Валидация URL обложки."""
        if v and not v.startswith(('http://', 'https://', '/media/')):
            raise ValueError("URL обложки должен начинаться с http://, https:// или /media/")
        return v

    @field_validator('blocks')
    @classmethod
    def validate_blocks(cls, v: List[NewsBlockCreate]) -> List[NewsBlockCreate]:
        """Валидация блоков."""
        if not v:
            raise ValueError("Новость должна содержать хотя бы один блок")

        # Проверяем что каждый блок имеет хотя бы текст или изображение
        for i, block in enumerate(v):
            if not block.text_content and not block.image_url:
                raise ValueError(f"Блок {i} должен содержать текст или изображение")

        return v


class NewsCreate(NewsBase):
    """Схема для создания новости."""
    publication_date: datetime = Field(default_factory=datetime.now, description="Дата публикации")


class NewsUpdate(BaseModel):
    """Схема для обновления новости."""
    title: str | None = Field(None, max_length=200, description="Заголовок новости")
    excerpt: str | None = Field(None, description="Краткое описание новости")
    cover_image: str | None = Field(None, description="URL обложки новости")
    is_published: bool | None = Field(None, description="Флаг публикации")
    publication_date: datetime | None = Field(None, description="Дата публикации")


class News(NewsBase):
    """Схема для возврата новости."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
    publication_date: datetime
    created_at: datetime
    updated_at: datetime | None
    blocks: List[NewsBlock] = Field(..., description="Блоки новости")


class NewsWithAuthor(News):
    """Схема новости с информацией об авторе."""
    author_username: str = Field(..., description="Имя автора")
    author_email: str | None = Field(None, description="Email автора")