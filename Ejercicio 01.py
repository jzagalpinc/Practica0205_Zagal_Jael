def saludo(nombre):
    """
    Función que crea un saludo personalizado y lo retorna.


    Parámetros:
        - nombre: Una cadena de texto con el nombre de la persona a saludar.


    Salida:
        - Una cadena de texto con el saludo personalizado.
    """
    return f"¡Hola {nombre}!, ¿Qué tal el solcito?"


nombre = input("Ingresa tu nombre por favor\n")
mensaje = saludo(nombre)
print(mensaje)

