import array

import random
from interfazGenetico import interfazGenetico

class AlgoritmoGenetico(interfazGenetico):

    #Crear las poblacion de solucion de tamaño cantidad de objetos n individuos 

    def crear_poblacion_inicial(self, n,cantidadObjetos):
        print(n)
        poblacion = []
                #poblacion.append([1,1,1,1,1,1])
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

        #print("Permutaciones a evaluar")
        #print(random_lista)
        #print(random_lista2)

        #print("-------------------------Comenzando torneo---------------------")
        ganadores = []
        for i in range(0, int(n)):
            #print("tomando dos padres: VOLUMEN / UTILIDA")
            #print(aptitud[random_lista[i]])
            #print(aptitud[random_lista2[i]])
            if(aptitud[random_lista[i]][1] > aptitud[random_lista2[i]][1]):
                #print("ganador :"+ str([random_lista[i]]))
                ganadores.append(poblacion[random_lista[i]])
            else:
                #print("ganador :"+ str([random_lista2[i]]))
                ganadores.append(poblacion[random_lista2[i]])

        ##print("-----------------------comenzando ruleta Aleatoria---------60/40----------------")
        ##print("-----------------------comenzando torneo aleatorio-------------------------")
        return ganadores

    #print("Imprimiendo lista de Ganadores:")
    #print(ganadores)

    def cruzamiento (self, ganadores, cantidadObjetos, n):
        #print("-----------------------comenzando cruza -------------------------")
        nuevaGeneracion = []
        corte_random = (random.randint(1,cantidadObjetos))
        #print("punto de corte: " + str(corte_random))
        for i in range(0, n, 2): 
            #determinar un punto aleatorio de corte

            hijo1 = [0,0,0,0,0,0]
            hijo2 = [0,0,0,0,0,0]
            for j in range(corte_random):
                hijo1[j] = ganadores[i][j]
                hijo2[j] = ganadores[i+1][j]
            for l in range(corte_random, cantidadObjetos):
                hijo2[l] = ganadores[i][l]
                hijo1[l] = ganadores[i+1][l]

            nuevaGeneracion.append(hijo1)
            nuevaGeneracion.append(hijo2)

        return nuevaGeneracion

    #print(nuevaGeneracion)

    def mutacion(self, cantidadObjetos, nuevaGeneracion, n): 
        #print("-----------------------------comenzando mutacion: CUCHAO---------------")
        for i in range(n):
            for j in range(cantidadObjetos):
                mutacion = random.randint(0,9)
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

    #print("Nueva generacion individuos  mutados") 
    #print("Reevaluar generacion para generar nuevos padres:")
    # ruleta para seleccionar los padres