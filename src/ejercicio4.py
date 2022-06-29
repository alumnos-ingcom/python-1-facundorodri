################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. 
Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
def suma_lenta(numero, otro_numero):
    """
    Esta funcion primero guarda en la variable suma el primer numero ingresado por el usuario. Luego mediante el lazo indefinido while 
    va sumando el segundo numero de a 1 vez en la variable suma. Por ultimo, envia el resultado mediante un return
    """
    suma = abs(numero)
    otro_numero = abs(otro_numero)
    while otro_numero > 0:
        suma = suma + 1
        otro_numero = otro_numero -1
    return(suma)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("ingrese un numero"))
    otro_numero = int(input("ingrese otro numero"))
    resultado = suma_lenta(numero, otro_numero)
    print(f"el resultado de la suma lenta es {resultado}")

if __name__ == "__main__":
    principal()
                