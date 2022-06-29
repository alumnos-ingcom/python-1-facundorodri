################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def compara(numero, otro_numero):
"""
Realiza una resta y devuelve un número entero en relación con cual numero es mayor, menor o igual
-1 el primero es menor que el segundo
0 son iguales
1 el primero es mayor que el segundo
"""
    resta = numero - otro_numero
    if resta > 0:
        resultado = 1
    elif resta < 0:
        resultado = -1
    else:
        resultado = 0
    return(resultado)

def principal():
    numero = int(input("ingrese un numero"))
    otro_numero = int(input("ingrese otro numero"))
    compara_numero = compara(numero, otro_numero)
    if compara_numero == 1:
        print("el primer numero es mayor que el segundo")
    elif compara_numero == -1:
        print("el el segundo numero es mayor que el primero")
    else:
        print("son iguales")

"""
Esta función es la que se encarga de la parte 'interactiva' del ejercicio
(La entrada, la llamada al algoritmo y la salida)
"""

if __name__ == "__main__":
    principal()