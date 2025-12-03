from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# ============================================================
# TABLAS INTERMEDIAS (m:n)
# ============================================================

class LibroAutorLink(SQLModel, table=True):
    id_libro: Optional[int] = Field(default=None, foreign_key="libro.id", primary_key=True)
    id_autor: Optional[int] = Field(default=None, foreign_key="autor.id", primary_key=True)


class LibroCategoriaLink(SQLModel, table=True):
    id_libro: Optional[int] = Field(default=None, foreign_key="libro.id", primary_key=True)
    id_categoria: Optional[int] = Field(default=None, foreign_key="categoria.id", primary_key=True)


# ============================================================
# CATÁLOGOS
# ============================================================

class Editorial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    direccion: str

    libros: List["Libro"] = Relationship(back_populates="editorial")


class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str

    libros: List["Libro"] = Relationship(back_populates="categorias", link_model=LibroCategoriaLink)


class PublicoObjetivo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str

    libros: List["Libro"] = Relationship(back_populates="publico_objetivo")


class Serie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numeroDeSerie: str
    descripcion_serie: str

    libros: List["Libro"] = Relationship(back_populates="serie")


class Autor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    libros: List["Libro"] = Relationship(back_populates="autores", link_model=LibroAutorLink)


# ============================================================
# TABLA PRINCIPAL: LIBRO
# ============================================================

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    isbn: str
    titulo: str
    ano_publicacion: str
    paginas: int
    precio: float
    formato: bool  # True = digital, False = fisicco

    # Relaciones 1:m
    editorial_id: Optional[int] = Field(default=None, foreign_key="editorial.id")
    editorial: Optional[Editorial] = Relationship(back_populates="libros")

    publico_objetivo_id: Optional[int] = Field(default=None, foreign_key="publicoobjetivo.id")
    publico_objetivo: Optional[PublicoObjetivo] = Relationship(back_populates="libros")

    serie_id: Optional[int] = Field(default=None, foreign_key="serie.id")
    serie: Optional[Serie] = Relationship(back_populates="libros")

    # Relaciones m:m
    autores: List[Autor] = Relationship(back_populates="libros", link_model=LibroAutorLink)
    categorias: List[Categoria] = Relationship(back_populates="libros", link_model=LibroCategoriaLink)
