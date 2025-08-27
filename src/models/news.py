from sqlalchemy import String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import BaseModel
from enum import StrEnum


class ImagePosition(str, StrEnum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


class NewsBlock(BaseModel):
    """
    Модель блока новости.

    Универсальный блок, который может содержать текст, изображение или оба элемента
    с возможностью выбора позиции изображения относительно текста.
    """
    __tablename__ = "news_blocks"

    news_id: Mapped[int] = mapped_column(ForeignKey("news.id", ondelete="CASCADE"),
                                         doc="ID новости, к которой принадлежит блок")
    title: Mapped[str | None] = mapped_column(String(200), nullable=True, doc="Заголовок блока (опционально)")
    text_content: Mapped[str | None] = mapped_column(Text, nullable=True,  doc="Текстовое содержание блока")
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True, doc="URL изображения (опционально)")
    image_position: Mapped[ImagePosition | None] = mapped_column(Enum(ImagePosition), nullable=True,
                                                                 doc="Позиция изображения относительно текста")
    order: Mapped[int] = mapped_column(default=0, doc="Порядок блока в новости")
    meta: Mapped[dict | None] = mapped_column(Text, nullable=True, doc="Дополнительные метаданные в формате JSON")

    # Relationship
    news: Mapped["News"] = relationship(back_populates="blocks")


class News(BaseModel):
    """
    Модель новости клиники.

    Представляет новостную статью или объявление, опубликованное клиникой,
    с информацией об авторе и статусе публикации.
    """
    __tablename__ = "news"

    title: Mapped[str] = mapped_column(String(200), doc="Заголовок новости")
    excerpt: Mapped[str | None] = mapped_column(Text, nullable=True, doc="Краткое описание новости для превью")
    publication_date: Mapped[datetime] = mapped_column(DateTime, doc="Дата публикации")
    cover_image: Mapped[str | None] = mapped_column(String(255), nullable=True, doc="URL обложки новости")
    is_published: Mapped[bool] = mapped_column(default=False, doc="Флаг публикации (True/False)")

    # Foreign key
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        doc="ID пользователя-автора новости"
    )

    # Relationships
    author: Mapped["User"] = relationship(
        back_populates="news",
        doc="Объект пользователя-автора новости"
    )
    blocks: Mapped[list["NewsBlock"]] = relationship(
        "NewsBlock",
        back_populates="news",
        cascade="all, delete-orphan",
        order_by="NewsBlock.order",
        doc="Блоки новости в порядке отображения"
    )
