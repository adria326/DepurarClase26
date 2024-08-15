import math

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  
    
    return True  

promedio = [0, -1, -3, 2, 3, 4, 5, 16, 23, -17]

for numero in promedio:
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no primo.")