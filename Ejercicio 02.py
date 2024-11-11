#Solución bucles recursivo:
def factorial_recursivo(n):
    """
    Calcula el factorial de un número usando recursividad.
    
    Parámetros:
    Returns:
        n (int): Número entero positivo del cual calcular el factorial.
        
        int: Factorial del número n.
        
    Raises:
        ValueError: Si el número es negativo.
        
    Ejemplo:
        >>> factorial_recursivo(5)
    """
    if n < 0:
        raise ValueError("El número debe ser positivo")
    
    if n == 0:
        return 1
    
    return n * factorial_recursivo(n - 1)


n = int(input("Por favor ingrese un número entero positivo\n"))
print(f"El factorial de {n} es {factorial_recursivo(n)}")