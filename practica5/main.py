from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database.SessionDep import *
from database.SessionDep import engine
from models.modelos import Libro
from models.modelos import Libro
from schemas.librosEschema import LibroCreate, LibroRead
from rutas import LibrosRutas, AutoresRutas, EditorialesRutas, PublicosObjetivoRutas, SeriesRutas, CategoriasRutas, busquedaLibros

app = FastAPI()
#Crear tablas al iniciar
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def home():
    return {"message": "Practica 5 definitivamente no entregue esto tarde consulte /docs"}

app.include_router(busquedaLibros.router)

app.include_router(LibrosRutas.router)
app.include_router(AutoresRutas.router)
app.include_router(EditorialesRutas.router)
app.include_router(PublicosObjetivoRutas.router)
app.include_router(SeriesRutas.router)
app.include_router(CategoriasRutas.router)