from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Practica 2 
#Crear una aplicacion API para almacenar actualizar y borrar l a informacion 
#de los paquetes enviados utilizar metodos GET POST PATCH DELETE




app = FastAPI()

#meter algunos items por defecto 

items = ['item1', 'item2']

#clase items para la integridad de los datos 

class itemBase(BaseModel):
    ganancia:float
    peso:float

class item(itemBase):
    id:int

class itemUpdate(itemBase):
    ganancia: float|None = None
    peso: float|None = None

# Lista de items
items2: list[item] = []

# Agregar elementos 
items2.append(item(id=1, ganancia=50.0, peso=10.0))
items2.append(item(id=2, ganancia=80.5, peso=20.3))


idConteo = 2
#principal de la API
@app.get("/")
def root():
    return  {"API REST para la creacion de items dentro de una lista": "world"}

#Recuperar la lista de items TODOS los items
@app.get("/items", 
        response_description="Devuelve todos los items de la lista" \
        "ingresados hasta el momento",
        status_code=200,
        tags=["Items"],
        summary="Todos los items!!!",
        responses={
            404:{"description":"Recurso no encontrado"},
            200:{"description":"Recurso encontrado"}
        })
def get_items():
    return items2


#ingresar items a la lista de items solicitud POST 
@app.post("/items1")
def create_items1(item: str):
    items.append(item)
    return items2




@app.get("/items/{item_id}")
def get_item(item_id: int) -> str: 
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item no contrado")