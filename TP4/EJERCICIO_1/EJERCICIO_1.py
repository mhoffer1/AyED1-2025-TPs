"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""

def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicua.
    - args: cadena (str): La cadena de caracteres a verificar.
    - returns: bool: True si la cadena es capicua, False en caso contrario.
    """
    largo = len(cadena)
    for i in range(largo // 2):
        if cadena[i] != cadena[- 1 - i]:
            return False
    return True

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    if es_capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")

if __name__ == "__main__":
    main()