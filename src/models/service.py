from sqlalchemy import String, Text, Integer, ForeignKey, Numeric, ARRAY, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel
from enum import StrEnum
from .service_specialist import service_specialist


class ServiceCategory(StrEnum):
    CONSULTATION = "consultation"
    DIAGNOSTICS = "diagnostics"
    SURGERY = "surgery"
    VACCINATION = "vaccination"
    DENTISTRY = "dentistry"
    DERMATOLOGY = "dermatology"
    OPHTHALMOLOGY = "ophthalmology"
    CARDIOLOGY = "cardiology"
    ULTRASOUND = "ultrasound"
    LABORATORY = "laboratory"
    GROOMING = "grooming"
    HOSPITALIZATION = "hospitalization"
    OTHER = "other"


class ServiceStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class Service(BaseModel):
    """
    Модель ветеринарной услуги.

    Представляет услугу, предоставляемую ветеринарной клиникой,
    с детальной информацией о стоимости, продолжительности, категории и других параметрах.
    """
    __tablename__ = "services"

    name: Mapped[str] = mapped_column(String(100), doc="Название услуги (макс. 100 символов)")
    short_description: Mapped[str | None] = mapped_column(
        String(200), nullable=True, doc="Краткое описание услуги для карточек (макс. 200 символов)")
    description: Mapped[str | None] = mapped_column(Text, nullable=True,
                                                    doc="Подробное описание услуги с HTML-разметкой")
    price: Mapped[float] = mapped_column(Numeric(10, 2), doc="Базовая стоимость услуги")
    min_price: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True,
                                                    doc="Минимальная цена (для услуг с диапазоном цен)")
    max_price: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True,
                                                    doc="Максимальная цена (для услуг с диапазоном цен)")
    duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True,
                                                         doc="Продолжительность услуги в минутах")
    min_duration: Mapped[int | None] = mapped_column(Integer, nullable=True, doc="Минимальная продолжительность (мин)")
    max_duration: Mapped[int | None] = mapped_column(Integer, nullable=True, doc="Максимальная продолжительность (мин)")
    category: Mapped[ServiceCategory] = mapped_column(Enum(ServiceCategory), default=ServiceCategory.OTHER,
                                                      doc="Категория услуги")
    status: Mapped[ServiceStatus] = mapped_column(Enum(ServiceStatus), default=ServiceStatus.ACTIVE,
                                                  doc="Статус услуги")
    is_popular: Mapped[bool] = mapped_column(default=False, doc="Флаг популярной услуги (отображается в featured)")
    is_available_online: Mapped[bool] = mapped_column(default=False, doc="Доступна ли услуга онлайн (телемедицина)")
    is_emergency: Mapped[bool] = mapped_column(default=False, doc="Является ли услуга экстренной")
    preparation_info: Mapped[str | None] = mapped_column(Text, nullable=True, doc="Информация о подготовке к услуге")
    contraindications: Mapped[str | None] = mapped_column(Text, nullable=True, doc="Противопоказания к услуге")
    required_specializations: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True,
                                                                       doc="Требуемые специализации врачей")
    tags: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True, doc="Теги для поиска и фильтрации")
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True, doc="URL изображения услуги")
    gallery: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True,
                                                      doc="Массив URL дополнительных изображений")
    order_index: Mapped[int] = mapped_column(Integer, default=0, doc="Порядковый индекс для сортировки")

    # Foreign keys
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), doc="ID клиники, предоставляющей услугу")

    # Relationships
    clinic: Mapped["Clinic"] = relationship(back_populates="services", doc="Объект клиники, предоставляющей услугу")

    # Связь многие-ко-многим со специалистами
    specialists: Mapped[list["Specialist"]] = relationship(
        "Specialist",
        secondary=service_specialist,
        back_populates="services",
        doc="Специалисты, которые предоставляют эту услугу"
    )
