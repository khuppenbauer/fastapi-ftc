# models.py
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class Ftc(Base):
  __tablename__ = 'ftc'

  id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
  firstname = Column(String(255))
  lastname = Column(String(255))
  street = Column(String(255))
  city = Column(String(255))
  email = Column(String(255))
  phone = Column(String(255))
  phone_emergency = Column(String(255))
  age = Column(Float)
  level = Column(String(255))
  lunch_saturday = Column(String(255))
  lunch_sunday = Column(String(255))
