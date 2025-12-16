"""algoritmo de PSO enjambre de particulas con los siguientes parametros
    n_particulas cantiddad n de particulas
    r1, r2 valores random       [0,1]
    w = inercia                 [0,1] 
    c_1 = nostalgia (cognitivo) [0,4]
    c_2 = influencia social     [0,4]

"""

import random , math
import copy


#parametros de configuracion
# tamaño del cumulo
n_particulas = input("ingrese la cantidad de particulas ")
n_particulas = int(n_particulas)

# Iteracioens 
iteracionMaxima = input("ingrese la cantidad maximca de iteraciones (generaciones)")
iteracionMaxima = int(iteracionMaxima)

limiteSuperior = 10
limiteInferior = 0
n_variables = 3
#inercia [0 ,1] 
w  = .4
# coeficientes 
c_1 = 2 # nostalgia (cognitivo) [0,4]
c_2 = 1.4 # influencia social     [0,4]


#1. incializar particulas (posiciones y velocidades)
def inicializarParticulas(nParticulas, nVariables, loweBracket, upperBracket):

    posiciones = []
    velocidades = [] 
    for i in range(nParticulas):
        nuevaPosicion = []
        nuevaVelocidad = [] 
        for j in range(nVariables):
            #Crear aleatorio para la posicion entre los limites 
        
            #nuevaParticula = loweBracket + random.uniform(loweBracket,upperBracket)
            #En caso de crear particulas estrictas 
            nuevaParticula =  loweBracket + random.random() * (upperBracket - loweBracket)
            
            # nuevaParticula =  random.uniform(loweBracket,upperBracket)

            #crear diferencias de -d a d siendo d el espacio entre las fronteras ls>li
            dj = upperBracket - loweBracket
            #Crear velocidades a partir de la -d 
            nuevaVelocidadParticula = -dj + 2 * random.random() * dj

            #nuevaVelocidadParticula = ( 2  * random.random() ) - dj 
            nuevaPosicion.append(nuevaParticula)
            nuevaVelocidad.append(nuevaVelocidadParticula)
        posiciones.append(nuevaPosicion)
        velocidades.append(nuevaVelocidad)

    return posiciones, velocidades 


#2 y 3 . Evaluar las posiciones de cada particula y asignar un pBest
def funcionObjetivo(variables):

    variables[0]
    # minf f(x) : 0.4*(x_1^0.67 * x_7^-0.67) + 0.4*(x_2^0.67 * x_8^-0.67) + 10 - x_1 - x_2  
    resultado =  (- variables[0]) + -variables[1] + -variables[2]

    return resultado

def penalizaParticulas(particulas):
    #Evaluacion es un numero Real entre los limites ordenar por indices
    evaluacion = particulas[2] * particulas[2] *10 
    return evaluacion


def evaluarParticulas(numeroParticulas, particulas):
    #Evaluacion es un numero Real entre los limites ordenar por indices
    evaluacion = []
    for i in range(numeroParticulas): 
        evaluacionParticula = funcionObjetivo(particulas[i])
        evaluacionParticula += penalizaParticulas(particulas[i])
        evaluacion.append(evaluacionParticula)

    return evaluacion




# 4 buscar la particula lider
def encontrar_particula_lider(particulas,particulasEvaluadas):

    mejorParticula = float("inf")
    indice = 0 
    for i in range(len(particulas)):
        if mejorParticula > particulasEvaluadas[i]:
            mejorParticula = particulasEvaluadas[i]
            indice = i 
    
    return particulas[indice] , indice

#5 Codigo para hacer la actualizacion 

#Entradas nParticulas, cantidad de variables, posiciones,  velocidad por particula, w = inercia, coeficiente nostalgia, coeficiente social, XpBest, XgBest 

def generarActualizaciones(nParticulas, nVariables, particulas_x, velocidades, inercia_w, cf_1, cfs_2, mejoresParticulas, particulaLider):

    for i in range(nParticulas):

        for j in range(nVariables):
            r1 , r2 = random.uniform(0,1), random.uniform(0,1)

            #V_i,j = w * V_i,j + cf_1 * r1(Xp_Best - X_i,j) + cf_2 * r2(XGbest- X_i,j)
            velocidades[i][j] = inercia_w * velocidades[i][j] + (cf_1 * r1 * (mejoresParticulas[i][j] - particulas_x[i][j])) + (cfs_2 * r2 * (particulaLider[j] - particulas_x[i][j]))
            particulas_x[i][j] = particulas_x[i][j] + velocidades[i][j]


    return particulas_x, velocidades 


# 6  Rectificar restricciones de dominio 

def rectificarRestricciones (nParticulas, nVariables, particulas, velocidades, limiteSuperior, limiteInferior):

    for i in range(nParticulas):

        for j in range(nVariables):
            # comprobar si la particula excede los limites 
            if particulas[i][j] > limiteSuperior or particulas[i][j] < limiteInferior:
                particulas[i][j] =  limiteInferior + random.random() * (limiteSuperior - limiteInferior)
                dj = limiteSuperior - limiteInferior
                velocidades[i][j] = -dj + 2 * random.random() * dj 

    return particulas, velocidades 

#7 evaluacion 

# Actualizar las mejores posiciones visitadas por particula 
def actualizarMejoresPosiciones(n_particulas, particulas, actitudParticulas, mejoresPosiciones, actitudMejoresPosiciones):

    for j in range(n_particulas):
        if actitudParticulas[j] < actitudMejoresPosiciones[j]:
            mejoresPosiciones[j] = copy.deepcopy(particulas[j])

            actitudMejoresPosiciones[j] = actitudParticulas[j]
    return mejoresPosiciones, actitudMejoresPosiciones



# 1 generar posiciones de cada particula y sus velocidades
posiciones, velocidades = inicializarParticulas(n_particulas, n_variables, limiteInferior, limiteSuperior)

# print("-----------------impresion de posiciones y velocidades originales ---------------")
# for posicion in posiciones: print(posicion)

# print("velocidades ")
# for vel in velocidades: print(vel)

# 2  a cada particula generada le corresponde su evaluacion 
evaluaciones = evaluarParticulas(n_particulas, posiciones)
#3 asignar a cada particula su mejor las mejores posiciones visitadas xpbes:particula se copia porque no se tiene una mejor
xpBest = copy.deepcopy(posiciones)

for i in range(iteracionMaxima):
    # 4 determinar la particula lider con las posiciones visitadas xpBest
    nuevasEvaluaciones = evaluarParticulas(n_particulas, xpBest)
    mejorParticula, indice  = encontrar_particula_lider(xpBest, nuevasEvaluaciones)
    # print("la mejor particula- >>> ", mejorParticula , " || indice: (" , indice, ")")
    # print("con evalucacion : ->>" , nuevasEvaluaciones[indice] )

    # 5 Actualizar la velocidad y posicion de las particulas
    nuevasParticulas_x , nuevasVelocidades_x = generarActualizaciones(n_particulas,n_variables,posiciones, velocidades, w, c_1, c_2, xpBest, mejorParticula)

    # print("las nuevas particulas son:")
    # for particula in nuevasParticulas_x : print(particula)

    # print("las nuevas velocidades son: ")
    # for velocidad in nuevasVelocidades_x: print(velocidad)

    # 6 rectificar las restricciones de dominio variables fuera de dominio se reinician 
    nuevasParticulas_R , nuevasVelocidades_R = rectificarRestricciones(n_particulas, n_variables, nuevasParticulas_x, nuevasVelocidades_x, limiteSuperior, limiteInferior )

    # print("----------particulas rectificadas:------")
    # for particula in nuevasParticulas_R : print(particula)

    # print("las nuevas velocidades rectificadas son: ")
    # for velocidad in nuevasVelocidades_R:  print(velocidad)

    # 7 Evaluacion de las nuevas posiciones de las particulas
    evaluacionesRectificadas = evaluarParticulas(n_particulas, nuevasParticulas_R)

    # 8 Actualizar mejores posiciones por particula (Xpbest[]) 1:1
    xpBest, mejoresAptitudesFinales = actualizarMejoresPosiciones(n_particulas, nuevasParticulas_R, evaluacionesRectificadas, xpBest, nuevasEvaluaciones)

    posiciones = nuevasParticulas_R
    velocidades = nuevasVelocidades_R

mejorParticula, indice  = encontrar_particula_lider(xpBest, nuevasEvaluaciones)
evaluacionMejorParticula = funcionObjetivo(mejorParticula)

print("la mejor particula- >>> ", mejorParticula , " || indice: (" , indice, ")")
print("con evalucacion objetivo : ->>" , evaluacionMejorParticula )
print("con evalucacion penalizada : ->>" , nuevasEvaluaciones[indice] )


solucionProblema =  [6.4747,2.234,0.6671,0.5957,5.9310,5.5271,1.0108,0.4004]
evaluacionSolucion = funcionObjetivo(solucionProblema)
print("particula solucion ===>>" , solucionProblema)
print("evaluacion solucion ===>> " , evaluacionSolucion)
    








