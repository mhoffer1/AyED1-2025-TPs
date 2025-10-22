"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""

def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicua de forma recursiva.
    - args: cadena (str): La cadena de caracteres a verificar.
    - returns: bool: True si la cadena es capicua, False en caso contrario.
    """
    def chequear(i: int) -> bool:

        largo = len(cadena)

        if i >= largo // 2:
            return True
        if cadena[i] != cadena[- 1 - i]:
            return False
        return chequear(i + 1)

    return chequear(0)

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    if es_capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")

if __name__ == "__main__":
    main()