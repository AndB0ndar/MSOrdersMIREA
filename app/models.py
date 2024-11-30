from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    location_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    status = Column(String, default="pending", index=True)

