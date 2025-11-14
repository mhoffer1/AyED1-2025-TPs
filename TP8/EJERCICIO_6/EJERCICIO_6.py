"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas según su longitud. Los signos de puntuación no deben afectar el 
proceso."""
import string

def eliminar_palabras_repetidas_y_ordenar(frase):
    # eliminar signos de puntuacion y convertir a minusculas
    traductor = str.maketrans('', '', string.punctuation)
    frase_limpia = frase.translate(traductor).lower()
    
    # dividir la frase en palabras y eliminar duplicados usando un conjunto
    palabras = frase_limpia.split()
    conjunto_palabras = set(palabras)
    
    # ordenar las palabras segun longitud
    palabras_ordenadas = sorted(conjunto_palabras, key=len)
    
    return palabras_ordenadas

if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    resultado = eliminar_palabras_repetidas_y_ordenar(frase)
    print("Palabras sin repetir y ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)