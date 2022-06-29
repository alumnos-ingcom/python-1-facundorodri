################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos 
valores ordenados de menor a mayor. Y Viceversa.
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos:
        if dos > tres:
            tupla = (uno,dos,tres)
        elif tres > uno:
            tupla = (tres,uno,dos)
        else:
            tupla = (uno,tres,dos)
    elif uno > tres:
        tupla = (dos,uno,tres)
    elif dos > tres:
        tupla = (dos,tres,uno)
    else:
        tupla = (tres,dos,uno)
    return(tupla)
        
        

def ordenar_menor_a_mayor(uno, dos, tres):
    if uno > dos:
        if dos > tres:
            tupla = (tres,dos,uno)
        elif tres > uno:
            tupla = (dos,uno,tres)
        else:
            tupla = (dos,tres,uno)
    elif uno > tres:
        tupla = (tres,uno,dos)
    elif dos > tres:
        tupla = (uno,tres,dos)
    else:
        tupla = (uno,dos,tres)
    return(tupla)
        
        

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    uno = int(input("ingrese el primer numero"))
    dos = int(input("ingrese el segundo numero "))
    tres = int(input("ingrese el tercer numero"))
    
    print(f"los numeros ordenados de mayor a menor son: {ordenar_mayor_a_menor(uno, dos, tres)}")
    print(f"los numeros ordenados de menor a mayor son: {ordenar_menor_a_mayor(uno, dos, tres)}")


if __name__ == "__main__":
    principal()