def principal():
    convertir_a_fahrenheit(1)
    convertir_a_centigrados(2)

"""
Esta función es la que se encarga de la parte 'interactiva' del ejercicio
(La entrada, la llamada al algoritmo y la salida)
"""
def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados*1.8 +32)
    return(fahrenheit)

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit-32)/1.8
    return(centigrados)

if __name__ == "__main__":
    principal()


