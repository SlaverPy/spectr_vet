from sqlalchemy import Table, Column, ForeignKey
from .base import BaseModel

service_specialist = Table(
    'service_specialist',
    BaseModel.metadata,
    Column('service_id', ForeignKey('services.id', ondelete='CASCADE'), primary_key=True),
    Column('specialist_id', ForeignKey('specialists.id', ondelete='CASCADE'), primary_key=True)
)
