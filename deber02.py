suma = []


if len(suma) == 0:
    print("La lista está vacía")
else:
    
    suma_total = 0

    for i in range(len(suma)):
        suma_total += suma[i]

    
    promedio = suma_total / len(suma)

    print("El promedio de los elementos es:", promedio)