from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Practica 2 
#Crear una aplicacion API para almacenar actualizar y borrar l a informacion 
#de los paquetes enviados utilizar metodos GET POST PATCH DELETE

#uvicorn main:app --reload


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
@app.get("/" ,response_description="descripcion de app",)
def root():
    return  {"API REST para la creacion de items dentro de una lista": "world"}

#Recuperar la lista de items TODOS los items
@app.get("/items", 
        response_description="Lista de todos los items disponibles ",
        status_code=200,
        tags=["Items"],
        summary="Todos los items!!!",
        responses={
            404:{"description":"Recurso no encontrado"},
           
        })
def get_items():
    return items2


@app.post("/itemsPOST_Parametros", 
        response_description="Devuelve la lista de items actualizada despues del ingreso obj por parametros",
        status_code=200,
        tags=["Items"],
        summary="Ruta para insertar un item!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def post_item( gananciaParametro: float, pesoParametro: float):
    nuevoItem = item(
        id=len (items2) +1 , 
        ganancia=gananciaParametro, 
        peso=pesoParametro)
    items2.append(nuevoItem)

    return items2

@app.post("/itemsPOST_Json", 
        response_description="Devuelve la lista de items actualizada despues del ingreso obj JSON" \
        "ingresados hasta el momento",
        status_code=200,
        tags=["Items"],
        summary="Ruta para insertar un item con Objeto JSON!!",
        responses={
            404:{"description":"Recurso no encontrado"},
            
        })
def post_items(nuevo_item: itemBase):
    nuevo = item(
        id=len(items2) + 1,
        ganancia=nuevo_item.ganancia,
        peso=nuevo_item.peso
    )
    items2.append(nuevo)
    return items2

@app.get("/itemsId/{item_id}", 
        response_description="Devuelve un solo item del {item_id}",
        status_code=200,
        tags=["Items"],
        summary="Ruta para recuperar un solo item dado ID_item!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def get_item(item_id: int) : 
    for itemEncontrado in items2:
        if itemEncontrado.id == item_id:
            return itemEncontrado
    else:
        raise HTTPException(status_code=404, detail="item no contrado")


@app.delete("/itemsId/{item_id}", 
        response_description="devuelve la lista actualizada",
        status_code=200,
        tags=["Items"],
        summary="Ruta para recuperar un solo item dado ID_item!!",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def delete_item(item_id: int) : 
    for itemEncontrado in items2:
        if itemEncontrado.id == item_id:
            items2.remove(itemEncontrado)
            return items2
    else:
        raise HTTPException(status_code=404, detail="item no contrado")