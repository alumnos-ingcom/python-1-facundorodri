################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados*1.8 +32)
    return(fahrenheit)

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit-32)/1.8
    return(centigrados)

def principal():
    opcion = float(input("ingrese 1 si desea pasar una temperatura de grados centigrados a Fahrenheit. Ingrese otro numero si desea realizar la conversion de forma viceversa"))
    temperatura = float(input("ingrese la temperatura que desea realizarle el pasaje"))
    if opcion == 1:
        print(f"la temperatura en Fahrenheit es {convertir_a_fahrenheit(temperatura)}")
    else:
        print(f"la temperatura en Fahrenheit es {convertir_a_centigrados(temperatura)}")

"""
Esta función es la que se encarga de la parte 'interactiva' del ejercicio
(La entrada, la llamada al algoritmo y la salida)
"""

if __name__ == "__main__":
    principal()


