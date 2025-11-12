from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database.SessionDep import *
from database.SessionDep import engine
from models.modelos import Libro
from models.modelos import Libro
from schemas.librosEschema import LibroCreate, LibroRead

app = FastAPI()
#Crear tablas al iniciar
@app.on_event("startup")
def on_startup():
    create_db_and_tables()



def get_session():
    with Session(engine) as session:
        yield session


@app.post("/libros/", response_model=LibroRead)
def crear_libro(libro: LibroCreate, session: Session = Depends(get_session)):
    nuevo_libro = Libro.from_orm(libro)
    session.add(nuevo_libro)
    session.commit()
    session.refresh(nuevo_libro)
    return nuevo_libro


@app.get("/libros/", response_model=list[LibroRead])
def listar_libros(session: Session = Depends(get_session)):
    libros = session.exec(select(Libro)).all()
    
    if libros:
        return libros
    return "no se an registrado libros aun"
