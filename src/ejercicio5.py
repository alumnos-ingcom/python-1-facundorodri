################
# Nombre - @facundorodri
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
def division_lenta(dividendo, divisor):
"""
def division_lenta(dividendo, divisor):
    """
    mientras el cociente(inicializado en cero) sea mayor que el el dividendo se ejecuta el lazo, dentro del lazo cada
    vez que se cumple la condicion se le va a restar al dividendo, una vez el divisor. ademas se va a contar cuantas 
    veces pasa por el lazo con la variable cociente, que sera la salida.
    """
    cociente = 0
    while cociente < dividendo:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    return(cociente)
def resto(dividendo,divisor):
    """
    mientras el cociente(inicializado en cero) sea mayor que el el dividendo se ejecuta el lazo, dentro del lazo cada
    vez que se cumple la condicion se le va a restar al dividendo, una vez el divisor. ademas se va a contar cuantas 
    veces pasa por el lazo con la variable cociente. cuando finaliza el lazo, si el dividendo es menor que cero se 
    suma al dividendo una vez más al divisor para que el resto no de negativo y sea el correcto. si es mayor o igual que
    cero, la salida seria el dividendo sin modificar(que corresponde al resto de la division)
    """
    cociente = 0
    while dividendo > 1:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    if dividendo < 0: 
        dividendo = dividendo + divisor
        return(dividendo)
    else:
        return(dividendo)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input("ingrese numero dividendo"))
    divisor = int(input("ingrese numero divisor"))
    cociente = division_lenta(dividendo, divisor)
    print(f"el cociente es {cociente}")
    print(f"el resto es {resto(dividendo,divisor)}")


if __name__ == "__main__":
    principal()
            