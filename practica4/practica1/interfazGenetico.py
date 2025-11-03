#esta clase es la interfaz (blueprint) para todos los algoritmos geneticos
from abc import ABC, abstractmethod
class interfazGenetico(ABC):
    @abstractmethod
    def crear_poblacion_inicial():
        pass
    @abstractmethod
    def evaluar_generacion():
        pass
    @abstractmethod
    def torneo():
        pass
    @abstractmethod
    def cruzamiento ():
        pass
    @abstractmethod
    def mutacion(): 
        pass
    @abstractmethod
    def encontrar_mejor_individuo():
        pass

