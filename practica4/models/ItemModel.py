
#Aqui se crean el modelo de item para base de datos
from typing import Optional
from sqlmodel import SQLModel, Field

# ITEM: idItem , peso, ganancia, categorias (etiquetas), EnvioFInal|=Null 

# class Item(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)

#     ganancia: float
#     peso: float

