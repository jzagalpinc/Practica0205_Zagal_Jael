def cuadrados(numeros):
    """
    Calcula el cuadrado de cada número en una lista.
   
    Esta función toma una lista de números y devuelve una nueva lista
    donde cada número ha sido elevado al cuadrado.
   
    Parámetros:
        numeros (list): Lista de números (enteros o decimales)
   
    Retorna:
        list: Una nueva lista con los cuadrados de los números originales
    """
    cuadrados = []
    for numero in numeros:
        cuadrados.append(numero ** 2)
   
    return cuadrados

numeros_decimales = [1.5, 2.0, 2.5, 3.0, 3.5]
cuadrados_decimales = cuadrados(numeros_decimales)
print(f"\nNúmeros originales: {numeros_decimales}")
print(f"Números al cuadrado: {cuadrados_decimales}")
