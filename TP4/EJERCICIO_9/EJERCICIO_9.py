import re

"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final.
"""

def ordenar_palabras_por_longitud(cadena: str) -> str:
    """
    Ordena las palabras de una cadena segun su longitud.
    args:
        cadena (str): Cadena de caracteres con las palabras separadas por espacios.
    returns:
        str: Cadena con las palabras ordenadas por longitud.
    """
    def longitud_sin_puntuacion(palabra: str) -> int:
        # elimina los caracteres que no son letras ni numeros y devuelve la longitud
        return len(re.sub(r'\W', '', palabra))

    palabras = re.findall(r'\S+', cadena)
    palabras_ordenadas = sorted(palabras, key=longitud_sin_puntuacion)
    return ' '.join(palabras_ordenadas)

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    cadena_ordenada = ordenar_palabras_por_longitud(cadena)
    print(f"Cadena con las palabras ordenadas por longitud: '{cadena_ordenada}'")