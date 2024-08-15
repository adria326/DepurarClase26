def es_palindromo(palabra):
    palabra = palabra.lower()
    
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = "Radar"
resultado = es_palindromo(palabra)
if resultado:
    print(f"La palabra '{palabra}' es un palindromo.")
else:
    print(f"La palabra '{palabra}' no es un palindromo.")