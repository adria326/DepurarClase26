numeros = [-10, -20, -30, -5, -15]

if len(numeros) == 0:
    print("La lista está vacía")
else:
    maximo = numeros[0]

    for i in range(1, len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]

    print("El número máximo es:", maximo)