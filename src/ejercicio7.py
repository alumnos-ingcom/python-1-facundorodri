################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a
segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    la funcion realiza cuentas aritmeticas y de conversion para pasar horas y minutos a segundos y luego sumar todo para tener la cantidade de segundos
    """
    horas = horas*3600
    minutos = minutos*60
    segundos = horas + minutos + segundos
    return(segundos)
    
def decimal_a_sexadecimal(numero):
    """
    la funcion realiza cuentas artimeticas y de conversion para pasar segundos a grados, minutos y segundos.
    """
    segundos = numero%60
    minutos = (numero//60)%60
    grados = numero//3600
    tupla = (grados,minutos,segundos)
    return tupla

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    opcion = int(input("elija 1 si desea realizar la conversion sexadecimal a decimal, o elija otra opcion si desea pasar de decimal a sexadecimal"))
    if opcion == 1:
        horas = int(input("ingrese horas/grados"))
        minutos = int(input("ingrese minutos"))
        segundos = int(input("ingrese segundos"))
        print(f"{horas} grados, {minutos} minutos, {segundos} segundos son {sexadecimal_a_decimal(horas, minutos, segundos)} segundos")
    else:
        numero = int(input("ingrese segundos"))
        print(f"{numero} segundos son: {decimal_a_sexadecimal(numero)}")


if __name__ == "__main__":
    principal()
    