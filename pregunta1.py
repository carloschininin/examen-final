import random


def almacenNumerosAleatorios(cantidad: 10):
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(0, 10))
    return lista


def numerosNoRepetidos(lista: list):
    listaNoRepetidos = []
    for item in lista:
        if item not in listaNoRepetidos:
            listaNoRepetidos.append(item)
    return listaNoRepetidos


def determinarNumeroMayor(lista: list):
    numeroMayor = 0
    for item in lista:
        if item > numeroMayor:
            numeroMayor = item
    return numeroMayor


listaObtenida = almacenNumerosAleatorios(10)
listaNoRepetida = numerosNoRepetidos(listaObtenida)
listaOrdenadaMayorAMenor = sorted(listaNoRepetida, reverse=True)
listaOrdenadaMenorAMayor = sorted(listaNoRepetida)
numeroMayorObtenido = determinarNumeroMayor(listaNoRepetida)
print('lista: ', listaObtenida)
print('lista de no repetidos: ', listaNoRepetida)
print('lista de mayor a menor: ', listaOrdenadaMayorAMenor)
print('lista de menor a mayor: ', listaOrdenadaMenorAMayor)
print('numero mayor: ', numeroMayorObtenido)
