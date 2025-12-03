from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Editorial
from schemas.librosEschema import  EditorialBase , EditorialBase, EditorialRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/Editorial",
    tags=["Editoriales"]
)


@router.post("/Registrareditorial", response_model=EditorialRead)
def crear_editorial(EditorialBase: EditorialBase, session: SessionDep ):
    nuevoeditorial = Editorial.from_orm(EditorialBase)

    session.add(nuevoeditorial)
    session.commit()
    session.refresh(nuevoeditorial)
    return nuevoeditorial


@router.get("/TodosLoseditoriales", response_model=list[EditorialRead])
def listar_editoriales(session: SessionDep):
    editoriales = session.exec(select(Editorial)).all()
    return editoriales


@router.delete("/Borrareditorial/{ideditorial}")
def borrar_editorial_ID( ideditorial : int , session: SessionDep):
    # Buscar el libro
    statement = select(Editorial).where(Editorial.id == ideditorial)
    editorial = session.exec(statement).first()

    if not editorial:
        raise HTTPException(status_code=404, detail="editorial no encontrado o eliminado previamente")
    # Eliminarlo
    session.delete(editorial)
    session.commit()

    return {"mensaje": "Item con id "+str(ideditorial)+" eliminado correctamente"}



@router.patch("/actualizareditorial/{ideditorial}")
def actuazlizar_editoriales_id( ideditorial : int , session: SessionDep , editorial_editado : EditorialBase):
    # Buscar el libro
    statement = select(Editorial).where(Editorial.id == ideditorial)
    editorial = session.exec(statement).first()

    if not editorial:
        raise HTTPException(status_code=404, detail="editorial no encontrado")
    
    
    if editorial_editado.nombre is not None:
        editorial.nombre = editorial_editado.nombre

    if editorial_editado.nombre is not None:
        editorial.direccion = editorial_editado.direccion
    
    session.commit()
    session.refresh(editorial)
    return editorial