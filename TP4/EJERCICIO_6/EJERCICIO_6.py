"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
como valor de retorno. Escribir también un programa para verificar el comporta-
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
"""

def extraer_con_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena utilizando rebanadas.
    args:
        cadena (str): Cadena de caracteres.
        posicion (int): Posicion inicial de la subcadena.
        cantidad (int): Cantidad de caracteres a extraer.
    returns:
        str: Subcadena extraida.
    """
    return cadena[posicion:posicion + cantidad]

def extraer_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena sin utilizar rebanadas.
    args:
        cadena (str): Cadena de caracteres.
        posicion (int): Posicion inicial de la subcadena.
        cantidad (int): Cantidad de caracteres a extraer.
    returns:
        str: Subcadena extraida.
    """
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        if i < len(cadena):
            subcadena += cadena[i]
        else:
            break
    return subcadena

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion = int(input("Ingrese la posicion inicial de la subcadena: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a extraer: "))

    subcadena_rebanadas = extraer_con_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraida con rebanadas: {subcadena_rebanadas}")

    subcadena_sin_rebanadas = extraer_sin_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraida sin rebanadas: {subcadena_sin_rebanadas}")

if __name__ == "__main__":
    main()