from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Libro, Autor, Categoria
from schemas.librosEschema import LibroCreate, LibroRead, LibroUpdate
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/Libros",
    tags=["Libros"]
)


@router.post("/RegistrarLibro", response_model=LibroRead)
def crear_libro(libro: LibroCreate, session: SessionDep):

    #Crear el objeto localmente
    nuevo_libro = Libro(
        isbn=libro.isbn,
        titulo=libro.titulo,
        ano_publicacion=libro.ano_publicacion,
        paginas=libro.paginas,
        precio=libro.precio,
        formato=libro.formato,
        editorial_id=libro.editorial_id,
        publico_objetivo_id=libro.publico_objetivo_id,
        serie_id=libro.serie_id,
    )

    #Consultra la lista a tra vez de la tabla multirelacion para ambos
    if libro.autores_ids:
        autores = session.exec(select(Autor).where(Autor.id.in_(libro.autores_ids))).all() # type: ignore
        nuevo_libro.autores = autores # type: ignore

    if libro.categorias_ids:
        categorias = session.exec(select(Categoria).where(Categoria.id.in_(libro.categorias_ids))).all() # type: ignore
        nuevo_libro.categorias = categorias # type: ignore


    session.add(nuevo_libro)
    session.commit()
    session.refresh(nuevo_libro)

    return nuevo_libro

@router.get("/TodosLosLibros", response_model=list[LibroRead])
def listar_libros(session: SessionDep):
    libros = session.exec(select(Libro)).all()
    return libros

@router.delete("/BorrarLibro/{idLibro}")
def borrar_libro_id( idLibro : int , session: SessionDep):
    # Buscar el libro
    statement = select(Libro).where(Libro.id == idLibro)
    item = session.exec(statement).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    # Eliminarlo
    session.delete(item)
    session.commit()

    return {"mensaje": "Item con id "+str(idLibro)+" eliminado correctamente"}

@router.patch("/ActualizarLibro/{libro_id}", response_model=LibroRead)
def actualizar_libro(libro_id: int, nuevo_libro: LibroUpdate, session: SessionDep):
    # Buscar el libro existente
    statement = select(Libro).where(Libro.id == libro_id)
    libro_existente = session.exec(statement).first()

    if not libro_existente:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    # Actualizar campos simples
    if nuevo_libro.isbn is not None:
        libro_existente.isbn = nuevo_libro.isbn
    if nuevo_libro.titulo is not None:
        libro_existente.titulo = nuevo_libro.titulo
    if nuevo_libro.ano_publicacion is not None:
        libro_existente.ano_publicacion = nuevo_libro.ano_publicacion
    if nuevo_libro.paginas is not None:
        libro_existente.paginas = nuevo_libro.paginas
    if nuevo_libro.precio is not None:
        libro_existente.precio = nuevo_libro.precio
    if nuevo_libro.formato is not None:
        libro_existente.formato = nuevo_libro.formato
    if nuevo_libro.editorial_id is not None:
        libro_existente.editorial_id = nuevo_libro.editorial_id
    if nuevo_libro.publico_objetivo_id is not None:
        libro_existente.publico_objetivo_id = nuevo_libro.publico_objetivo_id
    if nuevo_libro.serie_id is not None:
        libro_existente.serie_id = nuevo_libro.serie_id

    # Actualizar autores
    if nuevo_libro.autores_ids is not None: 
        autores = session.exec(select(Autor).where(Autor.id.in_(nuevo_libro.autores_ids))).all() # type: ignore
        libro_existente.autores = autores # type: ignore

    # Actualizar categorias
    if nuevo_libro.categorias_ids is not None:
        categorias = session.exec(select(Categoria).where(Categoria.id.in_(nuevo_libro.categorias_ids))).all() # type: ignore
        libro_existente.categorias = categorias # type: ignore

    # Guardar cambios
    session.add(libro_existente)
    session.commit()
    session.refresh(libro_existente)

    return libro_existente