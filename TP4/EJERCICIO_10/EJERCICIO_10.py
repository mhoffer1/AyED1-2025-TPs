import re

"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función.
"""


def reemplazar_palabra(cadena, palabra_buscar, palabra_reemplazo):
    """
    Reemplaza todas las apariciones de una palabra completa por otra en una cadena.

    Args:
        cadena (str): La cadena de caracteres original.
        palabra_buscar (str): La palabra completa a buscar.
        palabra_reemplazo (str): La palabra por la que se reemplazará.

    Returns:
        tuple: Una tupla conteniendo la nueva cadena (str) y la cantidad 
               de reemplazos realizados (int).
    """
    patron = r'\b' + re.escape(palabra_buscar) + r'\b'
    
    nueva_cadena, cantidad = re.subn(patron, palabra_reemplazo, cadena)
    
    return nueva_cadena, cantidad

if __name__ == "__main__":
    texto_original = input("Introduce el texto original: ")
    palabra_a_buscar = input("Introduce la palabra a buscar: ")
    palabra_de_reemplazo = input("Introduce la palabra de reemplazo: ")

    print("-" * 30)

    texto_modificado, reemplazos_hechos = reemplazar_palabra(texto_original, palabra_a_buscar, palabra_de_reemplazo)

    print(f"Texto modificado: '{texto_modificado}'")
    print(f"Cantidad de reemplazos realizados: {reemplazos_hechos}")
