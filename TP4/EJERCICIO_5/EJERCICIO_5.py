"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""

def filtrar_palabras(cadena: str, n: int) -> str:
    """
    Filtra las palabras de la cadena que tienen N o mas caracteres utilizando ciclos normales.
    args:
        cadena (str): Cadena de caracteres con la frase original.
        n (int): Numero mínimo de caracteres.
    returns:
        str: Cadena con las palabras filtradas.
    """
    palabras = cadena.split()
    resultado = ""
    for palabra in palabras:
        if len(palabra) >= n:
            resultado += palabra + " "
    return resultado.strip()

def filtrar_palabras_comprension(cadena: str, n: int) -> str:
    """
    Filtra las palabras de la cadena que tienen N o mas caracteres utilizando listas por comprension.
    args:
        cadena (str): Cadena de caracteres con la frase original.
        n (int): Numero minimo de caracteres.
    returns:
        str: Cadena con las palabras filtradas.
    """
    palabras = cadena.split()
    resultado = " ".join([palabra for palabra in palabras if len(palabra) >= n])
    return resultado

def filtrar_palabras_filter(cadena: str, n: int) -> str:
    """
    Filtra las palabras de la cadena que tienen N o mas caracteres utilizando la funcion filter.
    args:
        cadena (str): Cadena de caracteres con la frase original.
        n (int): Numero minimo de caracteres.
    returns:
        str: Cadena con las palabras filtradas.
    """
    palabras = cadena.split()
    resultado = " ".join(filter(lambda palabra: len(palabra) >= n, palabras))
    return resultado

def main():
    cadena = input("Ingrese una frase: ")
    n = int(input("Ingrese el numero minimo de caracteres: "))

    print("Filtrado utilizando ciclos normales:")
    print(filtrar_palabras(cadena, n))

    print("Filtrado utilizando listas por comprension:")
    print(filtrar_palabras_comprension(cadena, n))

    print("Filtrado utilizando la funcion filter:")
    print(filtrar_palabras_filter(cadena, n))

if __name__ == "__main__":
    main()