from sqlalchemy import Column, Date, Integer, String, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False, index=True)
    lastname = Column(String(50), nullable=False, index=True)
    email = Column(String(50), unique=True, index=True)
    phone = Column(String(50), nullable=False, index=True)
    birthday = Column(Date, nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())