
#Aqui se crean el modelo de item para base de datos
from typing import Optional
from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ganancia: float
    peso: float


# class ItemBase(SQLModel):
#     ganancia: float
#     peso: float

# class Item(ItemBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
    
# class ItemCreate(ItemBase):
#     pass

# class ItemUpdate(SQLModel):
#     ganancia: Optional[float] = None
#     peso: Optional[float] = None
