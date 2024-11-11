def calcular_media(numeros):
    """
    Calcula la media de una lista de números.
   
    Esta función toma una lista de números y devuelve su media aritmética.
   
    Parámetros:
        numeros (list): Lista de números (enteros o decimales)
   
    Retorna:
        float: La media de los números en la lista
    """
    suma_total = sum(numeros)
   
    cantidad_numeros = len(numeros)
   
    media = suma_total / cantidad_numeros
   
    return media

numeros_enteros = [1, 2, 3, 4, 5]
media_enteros = calcular_media(numeros_enteros)
print(f"La media de {numeros_enteros} es: {media_enteros}")
