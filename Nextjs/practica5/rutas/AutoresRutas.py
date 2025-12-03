from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Libro, Autor
from schemas.librosEschema import LibroCreate, LibroRead , AutorBase , AutorRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/Autores",
    tags=["Autores"]
)


@router.post("/RegistrarAutor", response_model=AutorRead)
def crear_Autor(autorBase: AutorBase, session: SessionDep ):
    nuevoAutor = Autor.from_orm(autorBase)

    session.add(nuevoAutor)
    session.commit()
    session.refresh(nuevoAutor)
    return nuevoAutor


@router.get("/TodosLosAutores", response_model=list[AutorRead])
def listar_Autores(session: SessionDep):
    autores = session.exec(select(Autor)).all()
    return autores


@router.delete("/BorrarAutor/{idAutor}")
def borrar_Autor_ID( idAutor : int , session: SessionDep):
    # Buscar el libro
    statement = select(Autor).where(Autor.id == idAutor)
    autor = session.exec(statement).first()

    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado o eliminado previamente")
    # Eliminarlo
    session.delete(autor)
    session.commit()

    return {"mensaje": "Item con id "+str(idAutor)+" eliminado correctamente"}



@router.patch("/actualizarAutor/{idAutor}")
def actuazlizar_autores_id( idAutor : int , session: SessionDep , autor_editado : AutorBase):
    # Buscar el libro
    statement = select(Autor).where(Autor.id == idAutor)
    autor = session.exec(statement).first()

    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    
    
    if autor_editado.nombre is not None:
            autor.nombre = autor_editado.nombre
            session.commit()
            session.refresh(autor)

    return autor