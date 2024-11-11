def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.
   
    Esta función toma un texto y devuelve un diccionario donde las
    claves son las palabras y los valores son el número de veces
    que aparecen en el texto.
   
    Parámetros:
        texto (str): El texto a analizar
   
    Retorna:
        dict: Diccionario con la frecuencia de cada palabra
    """
    texto = texto.lower()
   
    palabras = texto.split()
   
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
   
    return frecuencias


def palabra_mas_frecuente(frecuencias):
    """
    Encuentra la palabra más frecuente en un diccionario de frecuencias.
   
    Esta función toma un diccionario de frecuencias de palabras y devuelve
    una tupla con la palabra más frecuente y su número de apariciones.
   
    Parámetros:
        frecuencias (dict): Diccionario con palabras y sus frecuencias
   
    Retorna:
        tuple: Tupla con la palabra más frecuente y su frecuencia
    """
    palabra_max = max(frecuencias, key=frecuencias.get)
    frecuencia_max = frecuencias[palabra_max]
   
    return (palabra_max, frecuencia_max)


texto1 = "Hola señores. Hola mundo. Adios chicos. Hola chiquito"
frecuencias1 = contar_palabras(texto1)
print(f"Frecuencias en el texto: {frecuencias1}")
mas_frecuente1 = palabra_mas_frecuente(frecuencias1)
print(f"La palabra más frecuente es '{mas_frecuente1[0]}' (aparece {mas_frecuente1[1]} veces)")



