def decorador(funcion):
    def funcion_decorada(*args, **kwargs):
        import time
        print("Inicio")
        tiempo_inicio = time.time()
        resultado = funcion(*args, **kwargs)
        tiempo_fin = time.time()
        print("Fin")
        print("Tiempo de ejecución: {}".format(tiempo_fin - tiempo_inicio))
        return resultado

    return funcion_decorada


@decorador
def divisionNumeros(a, b):
    return a / b


valor = divisionNumeros(4, 2)
print('la division es:', valor)

valor = divisionNumeros(8, 3)
print('la division es:', valor)
