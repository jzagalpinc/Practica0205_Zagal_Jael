def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
   
    Args:
    radio (float): El radio del círculo.
   
    Returns:
    float: El área del círculo.
    """
    return 3.14159 * radio ** 2


def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.
   
    Args:
    radio (float): El radio del cilindro.
    altura (float): La altura del cilindro.
   
    Returns:
    float: El volumen del cilindro.
    """
    area_base = calcular_area_circulo(radio)
    return area_base * altura


if __name__ == "__main__":
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    altura_cilindro = float(input("Ingrese la altura del cilindro: "))


    area_circulo = calcular_area_circulo(radio_circulo)
    volumen_cilindro = calcular_volumen_cilindro(radio_circulo, altura_cilindro)


    print(f"El área del círculo es: {area_circulo:.2f}")
    print(f"El volumen del cilindro es: {volumen_cilindro:.2f}")


