import random
import math


def crearListaYGuardar(nombre_archivo):
    archivo = open(nombre_archivo, "w")
    cantidad = input("Ingrese la cantidad de numeros a almacenar: ")
    for i in range(int(cantidad)):
        numero = random.randint(1, 100)
        archivo.write(str(numero) + "\n")
    archivo.close()


def raizCuadradaNumeros(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lista = []
    for linea in archivo:
        lista.append(math.sqrt(int(linea)))
    archivo.close()

    archivo = open(nombre_archivo, "w")
    for i in lista:
        archivo.write(str(i) + "\n")
    archivo.close()
