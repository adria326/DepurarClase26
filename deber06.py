def invertir_cadena(cadena):
    
    cadena_invertida = cadena[::-1]
    return cadena_invertida

cadena = "python"
promedio = invertir_cadena(cadena)
print("Cadena correcta:", cadena)
print("Cadena invertida:", promedio)