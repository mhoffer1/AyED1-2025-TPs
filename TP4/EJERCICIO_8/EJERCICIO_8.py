"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos N caracteres de una cadena dada.
    args:
        cadena (str): Cadena de caracteres.
        n (int): Cantidad de caracteres a devolver.
    returns:
        str: Subcadena con los últimos N caracteres.
    """
    if n <= 0:
        return ""
    if n > len(cadena):
        return cadena
    resultado = ""
    for i in range(len(cadena) - n, len(cadena)):
        resultado += cadena[i]
    return resultado

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    n = int(input("Ingrese la cantidad de caracteres a devolver: "))

    subcadena = ultimos_n_caracteres(cadena, n)
    print(f"Subcadena con los últimos {n} caracteres: '{subcadena}'")

if __name__ == "__main__":
    main()