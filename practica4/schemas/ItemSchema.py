from pydantic import BaseModel
from typing import Optional, List
from schemas.EitquetaSchema import EtiquetaRead  # esquema de respuesta de etiquetas

# ----------------- ITEM BASE -----------------
class ItemBase(BaseModel):
    ganancia: float
    peso: float

class ItemCreate(ItemBase):

    etiquetas_ids: Optional[List[int]] = []


class ItemUpdate(BaseModel):
    ganancia: Optional[float] = None
    peso: Optional[float] = None
    etiquetas_ids: Optional[List[int]] = []


class ItemRead(ItemBase):
    id: int
    etiquetas: List[EtiquetaRead] = []  # aquí se devuelven las etiquetas relacionadas
    envio_final: Optional[str] = None 
    class Config:
        from_attributes = True  
