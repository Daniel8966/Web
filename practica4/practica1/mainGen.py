#Esta parte iria en el main del codigo basicamente 
from practica1.genetico import AlgoritmoGenetico
from practica1.geneticoModificable import AlgoritmoGeneticoModificado

"""
#necesitamos 4 entradas volumen total del camion, n cantidad de inidividuos, m generaciones 
Arreglo que contenga volumen y valor de cada objeto

"""

#Arreglo de los objetos con su volumen y su valor

#encontrar la cantidad de objeto para gnerar los slots de cada individuo [1|0|1|0|1|1...n] 

def resolver_algoritmo_genetico(n_Generaciones, n_Individuos, capacidad_Carga, items, porCentajeCruza, porcentajeMutacion):

    #Mismos metodos de la interfaz de algoritmo con diferentes comportamientos diferentes objetos
    cantidadObjetos = len(items)

    #el original es poblacionzila
    poblacionzila =  AlgoritmoGenetico()

    poblacion = poblacionzila.crear_poblacion_inicial(n_Individuos,cantidadObjetos)
    for i in range(n_Generaciones):
        poblacion, aptitud =poblacionzila.evaluar_generacion(poblacion,n_Individuos,cantidadObjetos,items,capacidad_Carga)
        ganadores = poblacionzila.torneo(n_Individuos, poblacion, aptitud)
        nuevaGeneracion = poblacionzila.cruzamiento(ganadores,cantidadObjetos,n_Individuos , porCentajeCruza)
        individuosMutados = poblacionzila.mutacion(cantidadObjetos,nuevaGeneracion,n_Individuos,porcentajeMutacion)
        poblacion = individuosMutados

    indice, aptitudFinal = poblacionzila.encontrar_mejor_individuo(individuosMutados,n_Individuos,cantidadObjetos,items,capacidad_Carga)


    return individuosMutados[indice] , aptitudFinal
