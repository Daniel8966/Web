import array

import random
from practica1.interfazGenetico import interfazGenetico

class AlgoritmoGeneticoModificado(interfazGenetico):
     
    def crear_poblacion_inicial():
        pass
    
    def evaluar_generacion():
        pass
    
    #voy a redifinir el metodo torneo para haerlo por ruleta en lugar de competencia
    def torneo(self, n, poblacion, aptitud):
        print("aplicando torneo por ruleta")
        #encontrar la suma de todas las utilidades 
        aptitudTotal = 0
        probabilidades = [] 
        ganadores = []
        for i in range(0, int(n)):
            aptitudTotal+=aptitud[i][1]
        
        for i in range(0, int(n)):
            porcentaje =aptitud[i][1] / aptitudTotal
            probabilidades.append(porcentaje)

        for i in range (0, int(n)): 
            numero = random.random()
            nuevoPorcetnaje = 0 
            while(nuevoPorcetnaje < numero):
                nuevoPorcetnaje += probabilidades[i]
            ganadores.append(poblacion[i])
        return ganadores

    def cruzamiento ():
        pass
    
    #mutacion aleatoria
    def mutacion(): 
        pass
    
    def encontrar_mejor_individuo():
        pass

