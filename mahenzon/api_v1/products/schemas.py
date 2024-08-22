from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductPartial(ProductCreate):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
