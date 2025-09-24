#Esta parte iria en el main del codigo basicamente 
from genetico import AlgoritmoGenetico
from geneticoModificable import AlgoritmoGeneticoModificado

"""
#necesitamos 4 entradas volumen total del camion, n cantidad de inidividuos, m generaciones 
Arreglo que contenga volumen y valor de cada objeto

"""
n = input('ingrese la cantidad n de individuos (posibles soluciones) \n ')
generaciones = int(input('ingrese la cantidad de generaciones que necesite'))
n = int(n)

#Arreglo de los objetos con su volumen y su valor
objetosVolumenValor =((1,2),(2,2),(6,3),(1,5),(8,1),(2,7)) 

#definir la cantidad v de volumen total del camion
vTotal = 15

#encontrar la cantidad de objeto para gnerar los slots de cada individuo [1|0|1|0|1|1...n] 
cantidadObjetos = len(objetosVolumenValor)

#Mismos metodos de la interfaz de algoritmo con diferentes comportamientos diferentes objetos

#el original es poblacionzila
poblacionzila =  AlgoritmoGenetico()

#poblacion modificada aqui se puede modificar los metodos 
poblacionModificada = AlgoritmoGeneticoModificado()

poblacion = poblacionzila.crear_poblacion_inicial(n,cantidadObjetos)
for i in range(generaciones):
    poblacion, aptitud =poblacionzila.evaluar_generacion(poblacion,n,cantidadObjetos,objetosVolumenValor,vTotal)
    #ganadores = poblacionModificada.torneo(n, poblacion, aptitud) #aqui se modifica las metodologias en la otra clase (geneticoModificable)
    ganadores = poblacionzila.torneo(n, poblacion, aptitud)
    nuevaGeneracion = poblacionzila.cruzamiento(ganadores,cantidadObjetos,n)
    individuosMutados = poblacionzila.mutacion(cantidadObjetos,nuevaGeneracion,n)
    poblacion = individuosMutados


print("impimiendo ultima generacion de individuos (despues de cruzas y mutaciones)")
print(individuosMutados)
indice, aptitudFinal = poblacionzila.encontrar_mejor_individuo(individuosMutados,n,cantidadObjetos,objetosVolumenValor,vTotal)
print("la mejor solucion se encuentra en:" + str(indice))
print("imprimiendo mejor individuo:"+ str(individuosMutados[indice]))
print("con aptitud de:" + str(aptitudFinal))

print("aaa")