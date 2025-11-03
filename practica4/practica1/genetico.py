

import random
from interfazGenetico import interfazGenetico

class AlgoritmoGenetico(interfazGenetico):

    #Crear las poblacion de solucion de tamaño cantidad de objetos n individuos 

    def crear_poblacion_inicial(self, n,cantidadObjetos):
        poblacion = []
        for i in range(n):
            nueva_lista = []
            for j in range(cantidadObjetos): 
                binario = random.choice([0, 1])
                nueva_lista.append(binario)
            poblacion.append(nueva_lista)
        return poblacion



    #hacer la evaluacion de los individuos Objetos ingresados al camion utilidad y su volumen
    #maximizar utilidad minimizar el volumen guardar en una matriz de utilidad (aptitud)

    def evaluar_generacion(self,poblacion,n,cantidadObjetos,objetosVolumenValor,vTotal):
        aptitud = []
        n = int(n)
        for i in range(n):
            volumen = 0 
            utilidad = 0
            for j in range(cantidadObjetos): 
                if poblacion[i][j] == 1 :
                    volumen+= objetosVolumenValor[j][0]
                    utilidad += objetosVolumenValor[j][1]

                    #comparar si la suma de los volumenes es mayor a el volumen total 
                if volumen >= vTotal:
                    poblacion[i][j] = 0 
                    #print('individuo ['  + str(i)+  ']excedio la carga descartando las demas soluciones soluciones')
                    faltan = cantidadObjetos -j 
                    for z in range(faltan): 
                        poblacion[i][j+z] = 0 
                    break
            aptitud.append((volumen, utilidad)) 
        return poblacion, aptitud

    #print(poblacion)
    #print(aptitud)


    # primer torneo para seleccionar padres
    #comparar dos individuos el ganador sera padre 
    #conformacion de torneo con permutaciones aleatorias (emparejar mitades) dos padres dan a dos hijos

    def torneo(self, n, poblacion, aptitud):

        random_lista = random.sample(range(n), n)
        random_lista2 = random.sample(range(n), n)


        ganadores = []
        for i in range(0, int(n)):
            if(aptitud[random_lista[i]][1] > aptitud[random_lista2[i]][1]):
                ganadores.append(poblacion[random_lista[i]])
            else:
                ganadores.append(poblacion[random_lista2[i]])
        return ganadores


    
    def cruzamiento(self, ganadores, longitudIndividuo, n, probabilidadCruzamiento):
        #print("-----------------------comenzando cruza -------------------------")
        nuevaGeneracion = []

        corte1 = random.randint(1, longitudIndividuo - 2) 
        corte2 = random.randint(corte1 + 1, longitudIndividuo - 1)

        #Cruza de 2 en 2
        for i in range(0 ,len(ganadores) , 2):
            if random.random() < probabilidadCruzamiento:
                hijo1 = []
                hijo2 = []
                segmento1 = ganadores[i][0:corte1]
                segmento2 = ganadores[i][corte1:corte2]
                segmento3 = ganadores[i][corte2:longitudIndividuo]
                segmento_1 = ganadores[i+1][0:corte1]
                segmento_2 = ganadores[i+1][corte1:corte2]
                segmento_3 = ganadores[i+1][corte2:longitudIndividuo]
                hijo1.extend(segmento1)
                hijo1.extend(segmento_2)
                hijo1.extend(segmento3)
                hijo2.extend(segmento_1)
                hijo2.extend(segmento2)
                hijo2.extend(segmento_3)      
                nuevaGeneracion.append(hijo1)
                nuevaGeneracion.append(hijo2)
            else: 
                hijo1 = ganadores[i][0:longitudIndividuo]
                hijo2 = ganadores[i+1][0:longitudIndividuo]
                nuevaGeneracion.append(hijo1)
                nuevaGeneracion.append(hijo2)

        return nuevaGeneracion



    def mutacion(self, cantidadObjetos, nuevaGeneracion, n , porcentajeMutacion): 
        #print("-----------------------------comenzando mutacion: CUCHAO---------------")
        for i in range(n):
            for j in range(cantidadObjetos):
                mutacion = porcentajeMutacion
                #mutacion = 1 / L  
                if (mutacion == 1):
                    #print("mutacion ocurrio en:" + str(i) + "," + str(j))
                    if(nuevaGeneracion[i][j] == 1):
                        nuevaGeneracion[i][j] = 0 
                    else:
                        nuevaGeneracion[i][j] = 1
        return nuevaGeneracion

    def encontrar_mejor_individuo(self, poblacion,n,cantidadObjetos,objetosVolumenValor,vTotal):
        busqueda = AlgoritmoGenetico()
        utilidad = []
        _, utilidad = busqueda.evaluar_generacion(poblacion,n,cantidadObjetos,objetosVolumenValor,vTotal)
        mejorUtilidad = 0 
        indice = 0 
        for i in range(int(n)):
            if utilidad[i][1] > mejorUtilidad:
                mejorUtilidad = utilidad[i][1]
                indice = i 
        return indice, mejorUtilidad

