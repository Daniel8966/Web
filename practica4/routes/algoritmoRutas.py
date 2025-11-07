from fastapi import APIRouter
from models.EtiquetasModel import Etiqueta, Item, Envio
from schemas.EitquetaSchema import EtiquetaBase, EtiquetaCreate, EtiquetaRead
from schemas.ItemSchema import ItemBase
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión
from fastapi import HTTPException
from sqlmodel import  select
from practica1.mainGen import resolver_algoritmo_genetico 


router = APIRouter(
    prefix="/algoritmoGenetico",
    tags=["algoritmoGenetico"]
)

@router.post(
    "/json",
    response_description="Devuelve la mejor combinacion de objetos para transportar",
    status_code=200,
    summary="Ruta para escojer los mejores objetos a transportar",
    responses={404: {"description": "Recurso no encontrado"}},
)

def usarAlgoritmoGenetico(session: SessionDep, capacidadCarga : int , generaciones: int, individuos: int, porcentajeCruza: float , porcentajeMutacion: float , descripcion_envio: str ):
    #Arreglo de los objetos con su volumen y su valor
    
    statement = (select(Item).where(Item.envio_final_id == None))

    result = session.exec(statement).all()

    if not result:
            raise HTTPException(status_code=404, detail=f"Item con ID no encontrado o ya asignado a un envío")

    objetosVolumenValor1 = []

    # insertar los elementos dentro del arreglo para el algoritmo genetico 
    for i in range(len(result)):
        objetosVolumenValor1.append((result[i].peso, result[i].ganancia , result[i].id))

    if len(objetosVolumenValor1) < 3 : 
         return "ingrese mas elementos para ser enviados"
         
    individuosSolucion, aptitudFinal  = resolver_algoritmo_genetico(generaciones, individuos, capacidadCarga, objetosVolumenValor1, porcentajeCruza, porcentajeMutacion)
    respuestaFianl = []
    i = 0 
    peso = 0
    for  individuo in individuosSolucion:
        if individuo == 1 : 
            respuestaFianl.append(result[i])
            peso+= result[i].peso
        i += 1 

    nuevo_envio = Envio(descripcion=descripcion_envio)
    session.add(nuevo_envio)
    session.commit()
    session.refresh(nuevo_envio)  # Para obtener el ID generado

    for item in respuestaFianl:
        item.envio_final_id = nuevo_envio.id
        item.envio_final = nuevo_envio
        session.add(item)

    session.commit()

    return {
        "envio_id": nuevo_envio.id,
        "descripcion": nuevo_envio.descripcion,
        "peso_total": peso,
        "ganancia_total": aptitudFinal,
        "items_asignados": [item.id for item in respuestaFianl]
    }


 

@router.post(
    "/geneticoAutomatico",
    response_description="Devuelve la mejor combinacion de objetos para transportar",
    status_code=200,
    summary="Ruta para escojer los mejores objetos a transportar de manera automatica 200 gen 50 individuos .9 cruza .01mutacion ",
    responses={404: {"description": "Recurso no encontrado"}}, 
)
def usarAlgoritmoGeneticoAutomatico(session: SessionDep, capacidadCarga: int ,descripcion_envio: str):
    #Arreglo de los objetos con su volumen y su valor
    
    statement = (select(Item).where(Item.envio_final_id == None))

    result = session.exec(statement).all()

    if not result:
            raise HTTPException(status_code=404, detail=f"Item con ID no encontrado o ya asignado a un envío")

    objetosVolumenValor1 = []

    # insertar los elementos dentro del arreglo para el algoritmo genetico 
    for i in range(len(result)):
        objetosVolumenValor1.append((result[i].peso, result[i].ganancia , result[i].id))

    if len(objetosVolumenValor1) < 3 : 
         return "ingrese mas elementos para ser enviados"
         
    individuosSolucion, aptitudFinal  = resolver_algoritmo_genetico(200, 50, capacidadCarga, objetosVolumenValor1, .9, .01)

    respuestaFianl = []
    i = 0 
    peso = 0
    for  individuo in individuosSolucion:
        if individuo == 1 : 
            respuestaFianl.append(result[i])
            peso+= result[i].peso
        i += 1 

    nuevo_envio = Envio(descripcion=descripcion_envio)
    session.add(nuevo_envio)
    session.commit()
    session.refresh(nuevo_envio)  # Para obtener el ID generado

    for item in respuestaFianl:
        item.envio_final_id = nuevo_envio.id
        item.envio_final = nuevo_envio
        session.add(item)

    session.commit()

    return {
        "envio_id": nuevo_envio.id,
        "descripcion": nuevo_envio.descripcion,
        "peso_total": peso,
        "ganancia_total": aptitudFinal,
        "items_asignados": [item.id for item in respuestaFianl]
    }

