from sqlalchemy import String, Boolean, Text, DateTime, Enum, ARRAY, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from .base import BaseModel
from enum import StrEnum


class UserRole(StrEnum):
    ADMIN = "admin"
    CLINIC_MANAGER = "clinic_manager"
    DOCTOR = "doctor"
    RECEPTIONIST = "receptionist"
    CLIENT = "client"


class UserStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    PENDING = "pending"


class BaseUser(BaseModel):
    """
    Базовая модель пользователя с общими полями
    """
    __abstract__ = True

    # Основная информация
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, doc="Email адрес")
    hashed_password: Mapped[str] = mapped_column(String(255), doc="Хэшированный пароль")

    # Персональная информация
    first_name: Mapped[str] = mapped_column(String(50), doc="Имя пользователя")
    last_name: Mapped[str] = mapped_column(String(50), doc="Фамилия пользователя")
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, doc="Номер телефона")

    # Статус и безопасность
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), default=UserStatus.ACTIVE)
    is_active: Mapped[bool] = mapped_column(default=True)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class ClinicStaff(BaseUser):
    """
    Персонал клиники
    """
    __tablename__ = "clinic_staff"

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), doc="Роль в клинике")

    # Связь с клиникой
    clinic_id: Mapped[int] = mapped_column(Integer, ForeignKey("clinics.id"), doc="ID клиники")

    # Дополнительные поля для персонала
    specialization: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, doc="Специализация (для врачей)")
    license_number: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, doc="Номер лицензии")

    # Relationships
    clinic: Mapped["Clinic"] = relationship("Clinic", back_populates="staff")
    appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="doctor",
                                                             foreign_keys="Appointment.doctor_id")


class Client(BaseUser):
    """
    Клиент клиники
    """
    __tablename__ = "clients"

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.CLIENT)

    # Дополнительные поля для клиентов
    date_of_birth: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, doc="Дата рождения")
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True, doc="Адрес")
    emergency_contact: Mapped[Optional[str]] = mapped_column(String(100), nullable=True,
                                                             doc="Контактное лицо на случай экстренной ситуации")

    # Medical information
    blood_type: Mapped[Optional[str]] = mapped_column(String(5), nullable=True, doc="Группа крови")
    allergies: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String), nullable=True, doc="Аллергии")
    chronic_diseases: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String), nullable=True,
                                                                  doc="Хронические заболевания")

    # Relationships
    appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="client",
                                                             foreign_keys="Appointment.client_id")
    medical_records: Mapped[list["MedicalRecord"]] = relationship("MedicalRecord", back_populates="client")
