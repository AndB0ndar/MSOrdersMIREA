from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    location_id: int
    status: Optional[str] = "pending"


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

