#Esquemas son utilizados para el manejo de la API 
from pydantic import BaseModel
from typing import  Optional

class ItemBase(BaseModel):
    ganancia: float
    peso: float
    
# Datos que el cliente envía al crear un item
class ItemCreate(BaseModel):
    ganancia: float
    peso: float

# Datos que el cliente puede actualizar parcialmente
class ItemUpdate(BaseModel):
    ganancia: Optional[float] = None
    peso: Optional[float] = None

# Datos que la API devuelve al cliente
class ItemRead(BaseModel):
    id: int
    ganancia: float
    peso: float

    class Config:
        orm_mode = True  # permite devolver objetos SQLModel/SQLAlchemy directamente


