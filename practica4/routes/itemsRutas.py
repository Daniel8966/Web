from fastapi import APIRouter, Depends
from models.ItemModel import *
from schemas.ItemSchema import ItemCreate, ItemUpdate, ItemBase, ItemRead
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
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item



#Recuperar de todos los items
@router.get("/items/", response_model=list[ItemRead])
def get_items(session: SessionDep):
    statement = select(Item)
    results = session.exec(statement)
    items = results.all()
    return items



#Recuperar un solo item por id
@router.get("/itemsId/{item_id}", 
        response_description="Devuelve un solo item del {item_id}",
        status_code=200,
        tags=["Items"],
        summary="Ruta para recuperar un solo item dado ID_item!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def get_item(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    return results

#Item actualizar TODOOO el item (PUT) 
@router.put("/itemsActualizar/{item_id}", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para cambiar toda la informacion de un item dada un ID",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def actualizarPorID(item_id: int, nuevo_item: ItemBase, session: SessionDep):
    # Buscar el item existente
    statement = select(Item).where(Item.id == item_id)
    item_existente = session.exec(statement).first()

    if not item_existente:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    # Actualizar los campos (solo los que cambian)
    item_existente.ganancia = nuevo_item.ganancia
    item_existente.peso = nuevo_item.peso

    # Guardar cambios
    #metodo de session.add para actualizar el item el id esta implicito
    session.add(item_existente)
    session.commit()
    session.refresh(item_existente)

    return item_existente

@router.patch("/actItem/", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para actualizar algunos campos de un item",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def actualizarItem(item_id: int, nuevo_item : ItemUpdate, session : SessionDep) : 
    
    statement = select(Item).where(Item.id == item_id)
    item_existente = session.exec(statement).first()

    if item_existente :
        if nuevo_item.peso!= None: item_existente.peso = nuevo_item.peso
        if nuevo_item.ganancia != None: item_existente.ganancia = nuevo_item.ganancia
        session.add(item_existente)
        session.commit()
        session.refresh(item_existente)

    else:
        raise HTTPException(status_code=404, detail="item no contrado")
    
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