from fastapi import APIRouter
from models.EtiquetasModel import Etiqueta
from models.ItemModel import Item
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
def usarAlgoritmoGenetico(session: SessionDep, items : list[int]):
    #Arreglo de los objetos con su volumen y su valor
    

    objetosVolumenValor1 = [] 
    for i in items:
        statement = select(Item).where(Item.id == items[i])
        results = session.exec(statement).all()
        objetosVolumenValor1.append(results)
        if not results:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        
    
        print(objetosVolumenValor1)
    
    
    objetosVolumenValor =((1,2),(2,2),(6,3))
    
    individuosSolucion, _  = resolver_algoritmo_genetico(200, 50, 15, objetosVolumenValor, .9, .01)
    print(individuosSolucion)

    return individuosSolucion
