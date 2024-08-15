def combinar_cadenas(lista):
    
    cadena = ""
    

    for i in range(len(lista)):
        
        cadena += lista[i]
        
        if i < len(lista) - 1:
            cadena += " "
    
    return cadena

letras = ["Hola", "mundo", "esto", "es","python."]
promedio = combinar_cadenas(letras)
print("Cadena combinada:", promedio)