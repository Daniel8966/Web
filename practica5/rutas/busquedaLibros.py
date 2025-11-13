from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Categoria, Libro, LibroAutorLink, LibroCategoriaLink
from models.modelos import Categoria as CategoriaModelo
from schemas.librosEschema import LibroRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/BuscarLibros",
    tags=["BuscarLibros"]
)

@router.get("/LibrosPorAutor/{autor_id}", response_model=list[LibroRead])
def obtener_libros_por_autor(autor_id: int, session: SessionDep):
    statement = (
        select(Libro)
        .join(LibroAutorLink)
        .where(LibroAutorLink.id_autor == autor_id)
    )
    libros = session.exec(statement).all()
    return libros

@router.get("/LibrosPorCategoria/{categoria_id}", response_model=list[LibroRead])
def obtener_libros_por_categoria(categoria_id: int, session: SessionDep):
    statement = (
        select(Libro)
        .join(LibroCategoriaLink)
        .where(LibroCategoriaLink.id_categoria == categoria_id)
    )
    libros = session.exec(statement).all()
    return libros


@router.get("/LibrosPorSerie/{serie_id}", response_model=list[LibroRead])
def obtener_libros_por_serie(serie_id: int, session: SessionDep):
    statement = select(Libro).where(Libro.serie_id == serie_id)
    libros = session.exec(statement).all()
    return libros

@router.get("/LibrosPorPublico/{publico_objetivo_id}", response_model=list[LibroRead])
def obtener_libros_por_publico(publico_objetivo_id: int, session: SessionDep):
    statement = select(Libro).where(Libro.publico_objetivo_id == publico_objetivo_id)
    libros = session.exec(statement).all()
    return libros

