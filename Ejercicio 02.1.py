#Solución bucles iterativo:
def factorial_iterativo(n):
    """
    Calcula el factorial de un número usando un bucle iterativo.
    
    Parámetros:
        n (int): Número entero positivo del cual calcular el factorial.
        
    Returns:
        int: Factorial del número n.
        
    Raises:
        ValueError: Si el número es negativo.
        
    Ejemplo:
        >>> factorial_iterativo(5)
        120
    """
    if n < 0:
        raise ValueError("El número debe ser positivo")
    
    if n == 0:
        return 1
        
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
        
    return resultado

print("Pruebas con bucle iterativo:")
print(f"Factorial de 5: {factorial_iterativo(5)}")  
print(f"Factorial de 0: {factorial_iterativo(0)}")  
print(f"Factorial de 3: {factorial_iterativo(3)}")  