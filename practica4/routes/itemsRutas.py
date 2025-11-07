from fastapi import APIRouter
from models.EtiquetasModel import Item, Etiqueta
from schemas.ItemSchema import ItemCreate, ItemUpdate, ItemBase, ItemRead
from schemas.EitquetaSchema import EtiquetaBase, EtiquetaCreate, EtiquetaRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión
from fastapi import HTTPException
from sqlmodel import  select



router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post(
    "/json",
    response_description="Devuelve la lista de items actualizada después del ingreso del objeto JSON",
    status_code=200,
    summary="Ruta para insertar un item con Objeto JSON!!",
    responses={404: {"description": "Recurso no encontrado"}},
)
def crear_item(item: ItemCreate, session: SessionDep):

    db_item = Item(
        ganancia=item.ganancia,
        peso=item.peso,

    )

    if item.etiquetas_ids:
        etiquetas = session.query(Etiqueta).filter(Etiqueta.id.in_(item.etiquetas_ids)).all() # type: ignore
        if not etiquetas:
            raise HTTPException(status_code=404, detail="Algunas etiquetas no existen")
        db_item.etiquetas = etiquetas


    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return ItemRead.from_orm(db_item)



#Recuperar de todos los items
@router.get("/items/", response_model=list[ItemRead])
def get_items(session: SessionDep):
    statement = select(Item)
    results = session.exec(statement)
    items = results.all()
    return items


#Recuperar un solo item por id
@router.get("/itemsId/{item_id}", response_model=ItemRead,
        response_description="Devuelve un solo item del {item_id}",
        status_code=200,
        tags=["Items"],
        summary="Ruta para recuperar un solo item dado ID_item!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def get_item(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    results = session.exec(statement).first()
    if not results:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    return results

#Item actualizar TODOOO el item (PUT) 
@router.put("/itemsActualizar/{item_id}", response_model=ItemRead,
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para cambiar toda la informacion de un item dada un ID",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def actualizarPorID(item_id: int, nuevo_item: ItemUpdate, session: SessionDep):

    statement = select(Item).where(Item.id == item_id)
    item_existente = session.exec(statement).first()


    if not item_existente:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    if nuevo_item.ganancia is not None:
        item_existente.ganancia = nuevo_item.ganancia
    if nuevo_item.peso is not None:
        item_existente.peso = nuevo_item.peso


    if nuevo_item.etiquetas_ids is not None:
        etiquetas = session.query(Etiqueta).filter(Etiqueta.id.in_(nuevo_item.etiquetas_ids)).all() # type: ignore
        item_existente.etiquetas = etiquetas
    session.commit()
    session.refresh(item_existente)

    return item_existente

@router.patch("/actItem/", response_model=ItemRead,
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para actualizar algunos campos de un item",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def actualizarItem(item_id: int, nuevo_item: ItemUpdate, session: SessionDep):

    statement = select(Item).where(Item.id == item_id)
    item_existente = session.exec(statement).first()

    if not item_existente:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    if nuevo_item.ganancia is not None:
        item_existente.ganancia = nuevo_item.ganancia
    if nuevo_item.peso is not None:
        item_existente.peso = nuevo_item.peso

    if nuevo_item.etiquetas_ids:
        etiquetas = session.query(Etiqueta).filter(
            Etiqueta.id.in_(nuevo_item.etiquetas_ids) # type: ignore
        ).all()

        if len(etiquetas) != len(nuevo_item.etiquetas_ids):
            raise HTTPException(status_code=404, detail="Algunas etiquetas no existen")

        item_existente.etiquetas = etiquetas

    session.commit()
    session.refresh(item_existente)
    return item_existente

@router.delete("/itemsId/{item_id}", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para eliminar un solo item dado el ID!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def eliminarPorID(item_id: int, session: SessionDep):
    # Buscar el item
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    # Eliminarlo
    session.delete(item)
    session.commit()

    return {"mensaje": "Item con id "+str(item_id)+" eliminado correctamente"}