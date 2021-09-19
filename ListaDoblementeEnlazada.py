from Nodo import *

class ListaDoblementeEnlazada:

    def __init__(self):
        self.inicio = None
        self.final = None
        self.contador = 0

    #Insertar Datos
    def insertar(self, dato):
        nodo = Nodo(dato)

        if self.inicio == None:
            self.inicio = nodo
            self.final = self.inicio
        else:
            nodo.anterior = self.final
            self.final.siguiente = nodo
            self.final = nodo

        self.contador += 1

    #interar entre la lista
    def iterar(self):
        actual = self.inicio

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    # Buscar el elemento atraves del dato digitado
    def buscar(self, dato):
        for datos in self.iterar():
            if dato == datos:
                print(f'El dato {dato} se encuenta en la lista')
                return True
        print('No se encuentra en la lista')
        return False

    #Mostrar todos los elementos de la lista
    def mostrar(self):
        for datos in self.iterar():
            print(datos)

    # Eliminar elemento atraves de dato digitado
    def eliminar(self, dato):

        actual = self.inicio
        eliminado = False

        if actual == None:
            eliminado = False
        elif actual.dato == dato:
            self.inicio = actual.siguiente
            self.inicio.anterior = None
            eliminado = True

        elif self.final.dato == dato:
            self.final = self.final.anterior
            self.final.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    print(f'El elemento {dato} de la lista ha sido eliminado')
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                else:
                    print(f'El elemento "{dato}" no ha sido eliminado, debido a que no se encuentra en la lista')
                    break
                actual = actual.siguiente

        if eliminado:
            self.contador -= 1

    #Obtener la informacion atraves de la posicion en la lista
    def __getitem__(self, posicion):
        if (posicion >= 0) and (posicion < self.contador):
            actual = self.inicio

            for _ in range(posicion - 1):
                actual = actual.siguiente

            return actual.dato
        else:
            raise Exception('Posicion no válido. Está por fuera del rango.')

    # Modificar la informacion atraves de la posicion en la lista
    def __setitem__(self, posicion, dato):
        if (posicion >= 0) and (posicion < self.contador):
            actual = self.inicio

            for _ in range(posicion - 1):
                actual = actual.siguiente

            actual.dato = dato
        else:
            raise Exception('Posicion no válido. Está por fuera del rango.')