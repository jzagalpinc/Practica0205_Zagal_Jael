def to_binary(decimal):
    """
    Convierte un número decimal a su representación binaria.
   
    Esta función toma un número decimal (entero) y devuelve
    su equivalente en formato binario como una cadena de texto.
   
    Parámetros:
        decimal (int): Número decimal a convertir
   
    Retorna:
        str: Representación binaria del número decimal
    """
    binario = ""
   
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
   
    if not binario:
        binario = "0"
   
    return binario


def from_binary(binario):
    """
    Convierte un número binario a su representación decimal.
   
    Esta función toma una cadena que representa un número binario
    y devuelve su equivalente en formato decimal.
   
    Parámetros:
        binario (str): Cadena con el número binario
   
    Retorna:
        int: Número decimal equivalente al binario
    """
    decimal = 0
   
    for posicion, bit in enumerate(reversed(binario)):
        decimal += int(bit) * 2 ** posicion
   
    return decimal

# Conversión de decimal a binario
numeros_decimales = [0, 1, 2, 5, 10, 15, 20, 50]
for num_decimal in numeros_decimales:
    binario = to_binary(num_decimal)
    print(f"{num_decimal} en binario es: {binario}")


# Conversión de binario a decimal
numeros_binarios = ["0", "1", "10", "101", "1010", "1111", "10100"]
for num_binario in numeros_binarios:
    decimal = from_binary(num_binario)
    print(f"{num_binario} en decimal es: {decimal}")
