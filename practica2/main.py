from fastapi import FastAPI, HTTPException

app = FastAPI()

print("no hace nada esta cagada")

items = ['item1', 'item2']


#principal de la API
@app.get("/")
def root():
    return  {"API REST para la creacion de items dentro de una lista": "world"}


#ingresar items a la lista de items solicitud POST 
@app.post("/items")
def create_items(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str: 
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item no contrado")