from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Device(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(String(16), nullable=False)
    mac_address = Column(String(32), unique=True)
    serial_number = Column(String(64), unique=True)
    manufacturer = Column(String(255))
    description = Column(String())
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f"({self.id}) {self.name}"
