from ListaDoblementeEnlazada  import *
# Juan Carlos Choc Xol
# Ing. Sistemas
# 202041390

lista = ListaDoblementeEnlazada()

# Insertando datos
lista.insertar(2)
lista.insertar('Juan')
lista.insertar(36)
lista.insertar('Carlos')

print("".center(60,'-'))

# Mostrar datos ingresados
lista.mostrar()

print("".center(60,'-'))

# Buscar dato
dato = 2
print(lista.buscar(dato))

print("".center(60,'-'))

# Eliminar dato de la lista
print('Eliminación de datos:')
dato = 'Juan'
lista.eliminar(dato)
lista.mostrar()

print("".center(60,'-'))

# Modificar
posicion = 1
lista[posicion] = 'Universidad San Carlos De Guatemala'
print(f'La posicion {posicion} a sido modificado por -> {lista[posicion]}')
lista.mostrar()