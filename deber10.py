def factorial(n):
    resultado = 1
    
    if n < 0:
        return "El factorial no está definido para numeros negativos."
    
    for i in range(1, n + 1):
        resultado *= i  #
    
    return resultado

numeros = [0, 1, 5, 7]  
for numero in numeros:
    factorialn = factorial(numero)
    print(f"El factorial de {numero} es: {factorialn}")