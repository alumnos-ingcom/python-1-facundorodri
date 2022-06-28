################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
def signo(numero):
    if numero+0 == 0:
        sgn = 0
    elif numero+1 > 1:
        sgn = 1
    else:
        sgn = -1
    return(sgn)
        
def principal():
    numero = int(input("ingrese un numero"))
    signo_numero = signo(numero)
    if signo_numero == 0:
        print("es cero")
    elif signo_numero == 1:
        print("es positivo")
    else:
        print("es negativo")

"""
Esta función es la que se encarga de la parte 'interactiva' del ejercicio
(La entrada, la llamada al algoritmo y la salida)
"""

if __name__ == "__main__":
    principal()
                