from sqlalchemy import String, Text, Integer, DateTime, Numeric, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import BaseModel


class Promotion(BaseModel):
    """
    Модель акции или специального предложения.

    Представляет маркетинговую акцию клиники с ограниченным сроком действия
    и информацией о скидке или специальных условиях.
    """
    __tablename__ = "promotions"

    title: Mapped[str] = mapped_column(String(200), doc="Заголовок акции (макс. 200 символов)")
    short_description: Mapped[str | None] = mapped_column(
        String(300), nullable=True, doc="Краткое описание акции для карточек (макс. 300 символов)")
    description: Mapped[str | None] = mapped_column(Text, nullable=True,
                                                    doc="Подробное описание акции с HTML-разметкой")
    discount_type: Mapped[str] = mapped_column(
        String(20), default="percentage",
        doc="Тип скидки: 'percentage' - процент, 'fixed' - фиксированная, 'gift' - подарок")
    discount_value: Mapped[float | None] = mapped_column(
        Numeric(10, 2), nullable=True, doc="Значение скидки (процент или фиксированная сумма)")
    original_price: Mapped[float | None] = mapped_column(
        Numeric(10, 2), nullable=True, doc="Исходная цена (для отображения старой цены)")
    final_price: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, doc="Финальная цена после скидки")
    start_date: Mapped[datetime] = mapped_column(DateTime, doc="Дата и время начала акции")
    end_date: Mapped[datetime] = mapped_column(DateTime, doc="Дата и время окончания акции")
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True, doc="URL основного изображения акции")
    gallery: Mapped[list[str] | None] = mapped_column(
        ARRAY(String), nullable=True, doc="Массив URL дополнительных изображений акции")
    is_active: Mapped[bool] = mapped_column(default=True, doc="Флаг активности акции (True/False)")
    is_featured: Mapped[bool] = mapped_column(default=False, doc="Флаг featured акции (для выделения на главной)")
    conditions: Mapped[str | None] = mapped_column(Text, nullable=True, doc="Условия акции (требования, ограничения)")
    promo_code: Mapped[str | None] = mapped_column(String(50), nullable=True, doc="Промокод для акции (если требуется)")
    clinic_id: Mapped[int | None] = mapped_column(
        ForeignKey("clinics.id"), nullable=True, doc="ID клиники, к которой привязана акция (None для всех клиник)")
    service_ids: Mapped[list[int] | None] = mapped_column(
        ARRAY(Integer), nullable=True, doc="Массив ID услуг, к которым применяется акция")

    # Relationships
    clinic: Mapped["Clinic | None"] = relationship(back_populates="promotions")
