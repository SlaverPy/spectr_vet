from pydantic import BaseModel, Field, validator, ConfigDict, EmailStr
from datetime import datetime, date
from typing import Optional, List, Any
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    CLINIC_MANAGER = "clinic_manager"
    DOCTOR = "doctor"
    RECEPTIONIST = "receptionist"
    CLIENT = "client"


class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    PENDING = "pending"


class UserBase(BaseModel):
    """Базовая схема пользователя."""
    email: EmailStr = Field(..., description="Email адрес")
    first_name: str = Field(..., max_length=50, description="Имя пользователя")
    last_name: str = Field(..., max_length=50, description="Фамилия пользователя")
    phone_number: Optional[str] = Field(None, max_length=20, description="Номер телефона")
    is_active: bool = Field(default=True, description="Активен ли пользователь")

    @validator('phone_number')
    def validate_phone_number(cls, v: Optional[str]) -> Optional[str]:
        """Валидация номера телефона."""
        if v is not None:
            # Убираем все нецифровые символы кроме +
            cleaned = ''.join(c for c in v if c.isdigit() or c == '+')
            if not cleaned.startswith('+') and len(cleaned) not in (10, 11):
                raise ValueError("Некорректный формат номера телефона")
        return v


# Схемы для персонала клиники
class ClinicStaffBase(UserBase):
    """Базовая схема персонала клиники."""
    role: UserRole = Field(..., description="Роль в системе")
    clinic_id: int = Field(..., description="ID клиники")
    specialization: Optional[str] = Field(None, max_length=100, description="Специализация")
    license_number: Optional[str] = Field(None, max_length=50, description="Номер лицензии")

    @validator('role')
    def validate_staff_role(cls, v: UserRole) -> UserRole:
        """Валидация роли для персонала."""
        if v == UserRole.CLIENT:
            raise ValueError("Персонал не может иметь роль клиента")
        return v


class ClinicStaffCreate(ClinicStaffBase):
    """Схема для создания персонала клиники."""
    password: str = Field(..., min_length=6, description="Пароль")

    @validator('password')
    def validate_password(cls, v: str) -> str:
        """Валидация пароля."""
        if len(v) < 6:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        return v


class ClinicStaffUpdate(BaseModel):
    """Схема для обновления персонала клиники."""
    email: Optional[EmailStr] = Field(None, description="Email адрес")
    first_name: Optional[str] = Field(None, max_length=50, description="Имя пользователя")
    last_name: Optional[str] = Field(None, max_length=50, description="Фамилия пользователя")
    phone_number: Optional[str] = Field(None, max_length=20, description="Номер телефона")
    is_active: Optional[bool] = Field(None, description="Активен ли пользователь")
    role: Optional[UserRole] = Field(None, description="Роль в системе")
    specialization: Optional[str] = Field(None, max_length=100, description="Специализация")
    license_number: Optional[str] = Field(None, max_length=50, description="Номер лицензии")

    @validator('role')
    def validate_staff_role(cls, v: Optional[UserRole]) -> Optional[UserRole]:
        """Валидация роли для персонала."""
        if v == UserRole.CLIENT:
            raise ValueError("Персонал не может иметь роль клиента")
        return v


# Схемы для клиентов
class ClientBase(UserBase):
    """Базовая схема клиента."""
    date_of_birth: Optional[date] = Field(None, description="Дата рождения")
    address: Optional[str] = Field(None, description="Адрес")
    emergency_contact: Optional[str] = Field(None, max_length=100, description="Экстренный контакт")
    blood_type: Optional[str] = Field(None, max_length=5, description="Группа крови")
    allergies: Optional[List[str]] = Field(None, description="Аллергии")
    chronic_diseases: Optional[List[str]] = Field(None, description="Хронические заболевания")

    @validator('blood_type')
    def validate_blood_type(cls, v: Optional[str]) -> Optional[str]:
        """Валидация группы крови."""
        if v is not None:
            valid_blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
            if v.upper() not in valid_blood_types:
                raise ValueError("Некорректная группа крови")
        return v

    @validator('date_of_birth')
    def validate_date_of_birth(cls, v: Optional[date]) -> Optional[date]:
        """Валидация даты рождения."""
        if v is not None:
            if v > date.today():
                raise ValueError("Дата рождения не может быть в будущем")
            age = (date.today() - v).days // 365
            if age < 0 or age > 120:
                raise ValueError("Некорректная дата рождения")
        return v


class ClientCreate(ClientBase):
    """Схема для создания клиента."""
    password: str = Field(..., min_length=6, description="Пароль")

    @validator('password')
    def validate_password(cls, v: str) -> str:
        """Валидация пароля."""
        if len(v) < 6:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль должна содержать хотя бы одну цифру")
        return v


class ClientUpdate(BaseModel):
    """Схема для обновления клиента."""
    email: Optional[EmailStr] = Field(None, description="Email адрес")
    first_name: Optional[str] = Field(None, max_length=50, description="Имя пользователя")
    last_name: Optional[str] = Field(None, max_length=50, description="Фамилия пользователя")
    phone_number: Optional[str] = Field(None, max_length=20, description="Номер телефона")
    is_active: Optional[bool] = Field(None, description="Активен ли пользователь")
    date_of_birth: Optional[date] = Field(None, description="Дата рождения")
    address: Optional[str] = Field(None, description="Адрес")
    emergency_contact: Optional[str] = Field(None, max_length=100, description="Экстренный контакт")
    blood_type: Optional[str] = Field(None, max_length=5, description="Группа крови")
    allergies: Optional[List[str]] = Field(None, description="Аллергии")
    chronic_diseases: Optional[List[str]] = Field(None, description="Хронические заболевания")


# Общие схемы ответа
class ClinicStaffResponse(ClinicStaffBase):
    """Схема для возврата данных персонала."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: UserStatus
    created_at: datetime
    updated_at: Optional[datetime]
    last_login: Optional[datetime]


class ClientResponse(ClientBase):
    """Схема для возврата данных клиента."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: UserRole = UserRole.CLIENT
    status: UserStatus
    created_at: datetime
    updated_at: Optional[datetime]
    last_login: Optional[datetime]


# Схемы для аутентификации
class UserLogin(BaseModel):
    """Схема для входа пользователя."""
    email: EmailStr
    password: str


class Token(BaseModel):
    """Схема токена."""
    access_token: str
    token_type: str = "bearer"
    user_type: str  # "staff" или "client"


class PasswordChange(BaseModel):
    """Схема для изменения пароля."""
    current_password: str
    new_password: str

    @validator('new_password')
    def validate_new_password(cls, v: str) -> str:
        """Валидация нового пароля."""
        if len(v) < 6:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        return v
