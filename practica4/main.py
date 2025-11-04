from fastapi import FastAPI
from database.SessionDep import create_db_and_tables 
from routes import itemsRutas, EtiquetasRutas, algoritmoRutas

app = FastAPI(title="Mi API modular")

#Crear tablas al iniciar
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Incluir las rutas
app.include_router(itemsRutas.router)
app.include_router(EtiquetasRutas.router)
app.include_router(algoritmoRutas.router)

@app.get("/")
def home():
    return {"message": "Practica 4 relacion de items a etiquetas (m:m) o algo asi consulte /docs"}
