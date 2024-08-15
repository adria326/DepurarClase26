def contar_palabras(oracion):
    palabras = oracion.split()

    numero_de_palabras = len(palabras)
    return numero_de_palabras

oracion = "Este es un ejemplo de una oracion."
promedio = contar_palabras(oracion)
print("Numero de palabras en la oracion:", promedio)