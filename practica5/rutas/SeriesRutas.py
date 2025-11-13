from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Serie as SerieModelo
from schemas.librosEschema import  SerieBase , SerieRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/Serie",
    tags=["Series"]
)


@router.post("/RegistrarSerie", response_model=SerieRead)
def crear_Serie(SerieBase: SerieBase, session: SessionDep ):
    nuevoSerie = SerieModelo.from_orm(SerieBase)

    session.add(nuevoSerie)
    session.commit()
    session.refresh(nuevoSerie)
    return nuevoSerie


@router.get("/TodosLosSeriees", response_model=list[SerieRead])
def listar_Seriees(session: SessionDep):
    Seriees = session.exec(select(SerieModelo)).all()
    return Seriees


@router.delete("/BorrarSerie/{idSerie}")
def borrar_Serie_ID( idSerie : int , session: SessionDep):
    # Buscar el libro
    
    statement = select(SerieModelo).where(SerieModelo.id == idSerie)
    Serie = session.exec(statement).first()

    if not Serie:
        raise HTTPException(status_code=404, detail="Serie no encontrado o eliminado previamente")
    # Eliminarlo
    session.delete(Serie)
    session.commit()

    return {"mensaje": "Item con id "+str(idSerie)+" eliminado correctamente"}



@router.patch("/actualizarSerie/{idSerie}")
def actuazlizar_Series_id( idSerie : int , session: SessionDep , Serie_editado : SerieBase):
    # Buscar el libro
    statement = select(SerieModelo).where(SerieModelo.id == idSerie)
    Serie = session.exec(statement).first()

    if not Serie:
        raise HTTPException(status_code=404, detail="Serie no encontrado")
    
    
    if Serie_editado.descripcion_serie is not None:
            Serie.descripcion_serie = Serie_editado.descripcion_serie
    
    if Serie_editado.numeroDeSerie is not None:
        Serie.numeroDeSerie = Serie_editado.numeroDeSerie

    session.commit()
    session.refresh(Serie)
    return Serie