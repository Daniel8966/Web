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
@app.post("/items/")
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
def actualizarPorID(item_id: int, nuevo_item : ItemBase) : 
    
    return "jaja nose" + str(item_id)
   