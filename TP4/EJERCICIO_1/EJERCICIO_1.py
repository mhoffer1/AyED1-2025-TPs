"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""

def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicua.
    args:
        cadena (str): Cadena a verificar.
    returns:
        bool: True si la cadena es capicua, False en caso contrario.
    """

    for i in range(len(cadena) // 2):
        if cadena[i] != cadena[- 1 - i]:
            return False
    return True

def main():
    cadena = input("Ingrese una cadena de caracteres: ")

    if es_capicua(cadena):
        print("La cadena es capicua.")
    else:
        print("La cadena no es capicua.")

if __name__ == "__main__":
    main()
