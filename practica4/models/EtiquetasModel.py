
#Aqui se crean los  modelos para base de datos

from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
# ITEM: idItem , peso, ganancia, categorias (etiquetas), EnvioFInal|=Null 
# ETIQUETAS: idEtiqueta, descripcion 

# Tabla intermediria : ITEM_TIENE_EQTIQUETA
class ItemEtiquetaLink(SQLModel, table=True):
    item_id: Optional[int] = Field(default=None, foreign_key="item.id", primary_key=True)
    etiqueta_id: Optional[int] = Field(default=None, foreign_key="etiqueta.id", primary_key=True)


# Tabla principal: ITEM
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    peso: float
    ganancia: float
    envio_final: Optional[str] = None  # ejemplo de campo adicional

    etiquetas: List["Etiqueta"] = Relationship(back_populates="items", link_model=ItemEtiquetaLink)


# Tabla ETIQUETA
class Etiqueta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str
    items: List[Item] = Relationship(back_populates="etiquetas", link_model=ItemEtiquetaLink)

#tabla de envios 
class Envio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str

