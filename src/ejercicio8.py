################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.
"""

def es_primo(numero):
    """
    la funcion lo que hace es verificar si el resto de un numero dividido por dos da cero genera com salida un 0 
    (no es primo). Si esa condicion no se cumple la salida es un 1 (es primo)
    """

    if numero%2 == 0:
        return(0)
    else:
        return(1)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("ingrese un numero para verificar si es primo o no"))
    resultado = es_primo(numero)
    if resultado == 0:
        print(f"el numero {numero} no es primo")
    else:
        print(f"el numero {numero} es primo")


if __name__ == "__main__":
    principal()
    