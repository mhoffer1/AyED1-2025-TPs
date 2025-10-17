"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""
def es_capicua(s: str) -> bool:
    """
    Determina si una cadena de caracteres es capicua.
        args: s (str): La cadena a verificar.
        return: bool: True si la cadena es capicua, False en caso contrario.
    """
    s_limpia = s.strip().lower().replace(' ', '')
    
    n = len(s_limpia)
    
    for i in range(n // 2):
        if s_limpia[i] != s_limpia[ -1 - i ]:
            return False
    
    return True

def main():
    
    pruebas = ["anita lava la tina", "hola mundo", "1234321", "menem"]

    for prueba in pruebas:
        print(f"'{prueba}' es capicua? {'Si' if es_capicua(prueba) else 'No'}")

if __name__ == "__main__":
    main()