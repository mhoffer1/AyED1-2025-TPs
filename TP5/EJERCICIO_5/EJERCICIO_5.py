"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo.
"""
from math import sqrt

def calcular_raiz_cuadrada():
    """Calcula la raiz cuadrada de un numero ingresado por el usuario."""
    try:
        entrada = input("Ingrese un numero para calcular su raiz cuadrada: ")
        numero = float(entrada)
        if numero < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
        raiz_cuadrada = sqrt(numero)
        print(f"La raiz cuadrada de {numero} es {raiz_cuadrada}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    calcular_raiz_cuadrada()

if __name__ == "__main__":
    main()
