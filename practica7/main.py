from PSOFinal import algoritmoParticulas
from fastapi import FastAPI, HTTPException


app = FastAPI()

#principal de la API
@app.get("/" ,response_description="descripcion de app",)
def root():
    return  {"API para uso de PSO resolucion de problema matematico  :"}



@app.get("/PSOSimple/", 
        response_description="Devuelve una posible solucion dado el probelma planteado en clase",
        status_code=200,
        tags=["PSO"],
        summary="Devuelve una posible solucion dado el probelma planteado en clase",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def get_solucion(numeroParticulas: int, numeroGeneraciones: int ):
    
    mejorParticula, evaluacion , historial= algoritmoParticulas(numeroParticulas, numeroGeneraciones, .4, 1.5, 1.4, 1000)
    return {"mejorParticula": mejorParticula, "Evaluacion_particula":  evaluacion, "Historial": historial}



@app.get("/PsoParametros/", 
        response_description="Devuelve una posible solucion dado el probelma planteado en clase ajusta tus parametros",
        status_code=200,
        tags=["PSO"],
        summary="Devuelve una posible solucion dado el probelma planteado en clase",
        responses={
            404:{"description":"Recurso no encontrado"},
        })
def get_solucion_avanzada(numeroParticulas: int, numeroGeneraciones: int , inercia: float , factorNostalgia: float , factorSocial: float , penalizacion : float):
    
    mejorParticula, evaluacion , historial= algoritmoParticulas(numeroParticulas, numeroGeneraciones, inercia, factorNostalgia,  factorSocial, penalizacion)
    return {"mejorParticula": mejorParticula, "Evaluacion_particula":  evaluacion, "Historial": historial}