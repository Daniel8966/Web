from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Libro, PublicoObjetivo
from schemas.librosEschema import  PublicoObjetivoRead , PublicoObjetivoBase
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/PublicoObjetivo",
    tags=["PublicoObjetivo"]
)


@router.post("/RegistrarPublico", response_model=PublicoObjetivoRead)
def crear_Publico(PublicoBase: PublicoObjetivoBase, session: SessionDep ):
    nuevoPublico = PublicoObjetivo.from_orm(PublicoBase)

    session.add(nuevoPublico)
    session.commit()
    session.refresh(nuevoPublico)
    return nuevoPublico


@router.get("/TodosLosPublicoes", response_model=list[PublicoObjetivoRead])
def listar_Publicoes(session: SessionDep):
    Publicoes = session.exec(select(PublicoObjetivo)).all()
    return Publicoes


@router.delete("/BorrarPublico/{idPublico}")
def borrar_Publico_ID( idPublico : int , session: SessionDep):
    # Buscar el libro
    statement = select(PublicoObjetivo).where(PublicoObjetivo.id == idPublico)
    Publico = session.exec(statement).first()

    if not Publico:
        raise HTTPException(status_code=404, detail="Publico no encontrado o eliminado previamente")
    # Eliminarlo
    session.delete(Publico)
    session.commit()

    return {"mensaje": "Item con id "+str(idPublico)+" eliminado correctamente"}



@router.patch("/actualizarPublico/{idPublico}")
def actuazlizar_Publicoes_id( idPublico : int , session: SessionDep , Publico_editado : PublicoObjetivoBase):
    # Buscar el libro
    statement = select(PublicoObjetivo).where(PublicoObjetivo.id == idPublico)
    Publico = session.exec(statement).first()

    if not Publico:
        raise HTTPException(status_code=404, detail="Publico no encontrado")
    
    
    if Publico_editado.descripcion is not None:
            Publico.descripcion = Publico_editado.descripcion
            
    
    session.commit()
    session.refresh(Publico)

    return Publico