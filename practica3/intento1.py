from typing import Annotated, Optional
from fastapi import Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select

from fastapi import FastAPI

# ---------- BASE DE DATOS ----------

sql_url = "sqlite:///database.db"
engine = create_engine(sql_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# ---------- SESIONES Y DEPENDENCIAS ----------

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

# ---------- MODELOS ----------
class ItemBase(SQLModel):
    ganancia: float
    peso: float

class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
# class Item(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     nombre: str
#     descripcion: str | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(SQLModel):
    ganancia: Optional[float] = None
    peso: Optional[float] = None

#---------aplicacion---------

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {"message": "Pachuca es un estado legitimo API fundada a base de pastes"}

#Recuperar de todos los items
@app.get("/items/", response_model=list[Item])
def get_items(session: Session = Depends(get_session)):
    statement = select(Item)
    results = session.exec(statement)
    items = results.all()
    return items

#Ruta para insertar items JSON 

@app.post("/itemsPOST_Json", 
        response_description="Devuelve la lista de items actualizada despues del ingreso obj JSON" \
        "ingresados hasta el momento",
        status_code=200,
        tags=["Items"],
        summary="Ruta para insertar un item con Objeto JSON!!",
        responses={
            404:{"description":"Recurso no encontrado"},
            
        })
def crear_item(item: ItemCreate, session: SessionDep):
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

#Recuperar un solo item por id
@app.get("/itemsId/{item_id}", 
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
@app.put("/itemsActualizar/{item_id}", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para cambiar toda la informacion de un item dada un ID",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def actualizarPorID(item_id: int, nuevo_item: ItemBase, session: Session = Depends(get_session)):
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

@app.patch("/actItem/", 
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
        if nuevo_item.peso: item_existente.peso = nuevo_item.peso
        if nuevo_item.peso: item_existente.ganancia = nuevo_item.ganancia
        session.add(item_existente)
        session.commit()
        session.refresh(item_existente)

    else:
        raise HTTPException(status_code=404, detail="item no contrado")
    
    return item_existente


@app.delete("/itemsId/{item_id}", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para eliminar un solo item dado el ID!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def eliminarPorID(item_id: int, session: Session = Depends(get_session)):
    # Buscar el item
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    # Eliminarlo
    session.delete(item)
    session.commit()

    return {"mensaje": "Item con id "+str(item_id)+" eliminado correctamente"}