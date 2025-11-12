from typing import Optional, List
from datetime import date
from pydantic import BaseModel


# ============================================================
# SCHEMAS PARA CATALOGOS
# ============================================================

class EditorialBase(BaseModel):
    nombre: str
    direccion: str


class EditorialRead(EditorialBase):
    id: int


class CategoriaBase(BaseModel):
    descripcion: str


class CategoriaRead(CategoriaBase):
    id: int


class PublicoObjetivoBase(BaseModel):
    descripcion: str


class PublicoObjetivoRead(PublicoObjetivoBase):
    id: int


class SerieBase(BaseModel):
    numeroDeSerie: str
    descripcion_serie: str


class SerieRead(SerieBase):
    id: int


class AutorBase(BaseModel):
    nombre: str


class AutorRead(AutorBase):
    id: int


# ============================================================
# SCHEMAS PARA LIBRO
# ============================================================

class LibroBase(BaseModel):
    isbn: str
    titulo: str
    ano_publicacion: Optional[str]
    paginas: int
    precio: float
    formato: bool  # True = digital, False = fisico

    editorial_id: Optional[int]
    publico_objetivo_id: Optional[int]
    serie_id: Optional[int]


# Al crear un libro: se permiten solo los IDs de relaciones
# y listas de IDs para autores y categorías
class LibroCreate(LibroBase):
    autores_ids: Optional[List[int]] = []
    categorias_ids: Optional[List[int]] = []


#  Al leer un libro: se devuelven objetos anidados (relaciones)
class LibroRead(LibroBase):
    id: int
    editorial: Optional[EditorialRead]
    publico_objetivo: Optional[PublicoObjetivoRead]
    serie: Optional[SerieRead]
    autores: Optional[List[AutorRead]] = []
    categorias: Optional[List[CategoriaRead]] = []

    class Config:
        orm_mode = True
