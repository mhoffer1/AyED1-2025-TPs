"""Realizar una función que reciba como parámetros dos cadenas de caracteres con
teniendo números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error.
"""

def sumar_cadenas_numericas(cadena1: str, cadena2: str) -> float:
    """Suma dos cadenas que representan numeros reales.

    Args:
        cadena1 (str): Primera cadena con un numero real.
        cadena2 (str): Segunda cadena con un numero real.

    Returns:
        float: La suma de los dos numeros reales, o -1 si alguna cadena no es valida.
    """
    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        return numero1 + numero2
    except ValueError:
        return -1

    
def main():
    cadena1 = input("Ingrese la primera cadena con un numero real: ")
    cadena2 = input("Ingrese la segunda cadena con un numero real: ")
    resultado = sumar_cadenas_numericas(cadena1, cadena2)
    if resultado == -1:
        print("Error: Alguna de las cadenas no contiene un numero valido.")
    else:
        print(f"La suma de los numeros es: {resultado}")


if __name__ == "__main__":
    main()