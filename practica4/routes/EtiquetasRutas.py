from fastapi import APIRouter
from models.EtiquetasModel import Etiqueta
from schemas.EitquetaSchema import EtiquetaBase, EtiquetaCreate, EtiquetaRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión
from fastapi import HTTPException
from sqlmodel import  select



router = APIRouter(
    prefix="/etiquetas",
    tags=["Etiquetas"]
)

@router.post(
    "/json",
    response_description="Devuelve la lista de etiquetas actualizada después del ingreso del objeto JSON",
    status_code=200,
    summary="Ruta para insertar una Etiqueta con Objeto JSON",
    responses={404: {"description": "Recurso no encontrado"}},
)
def crear_etiqueta(etiqueta: EtiquetaCreate, session: SessionDep):
    db_etiqueta = Etiqueta(**etiqueta.model_dump())

    session.add(db_etiqueta)
    session.commit()
    session.refresh(db_etiqueta)

    return db_etiqueta

#Recuperar todas las estiquetas
@router.get("/items/", response_model=list[EtiquetaRead])
def get_items(session: SessionDep):
    statement = select(Etiqueta)
    results = session.exec(statement)
    items = results.all()
    return items


@router.delete("/etiquetaBorrar/", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        summary="Ruta para eliminar una sola etiqueta dado el ID!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def eliminarPorID(etiqueta_id: int, session: SessionDep):
    # Buscar la etiqueta por ID
    statement = select(Etiqueta).where(Etiqueta.id == etiqueta_id)
    etiqueta = session.exec(statement).first()

    if not etiqueta:
        raise HTTPException(status_code=404, detail=f"Etiqueta con id {etiqueta_id} no encontrada")

    # Desvincular relaciones con items (opcional pero recomendado)
    etiqueta.items = []

    # Eliminar la etiqueta
    session.delete(etiqueta)
    session.commit()

    return {"mensaje": f"Etiqueta con id {etiqueta_id} eliminada correctamente"}