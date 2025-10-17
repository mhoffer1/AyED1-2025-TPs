"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
"""

def eliminar_con_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena utilizando rebanadas.
    args:
        cadena (str): Cadena de caracteres.
        posicion (int): Posicion inicial de la subcadena a eliminar.
        cantidad (int): Cantidad de caracteres a eliminar.
    returns:
        str: Cadena resultante.
    """
    return cadena[:posicion] + cadena[posicion + cantidad:]

def eliminar_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena sin utilizar rebanadas.
    args:
        cadena (str): Cadena de caracteres.
        posicion (int): Posicion inicial de la subcadena a eliminar.
        cantidad (int): Cantidad de caracteres a eliminar.
    returns:
        str: Cadena resultante.
    """
    resultado = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]
    return resultado

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion = int(input("Ingrese la posicion inicial de la subcadena a eliminar: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))

    cadena_rebanadas = eliminar_con_rebanadas(cadena, posicion, cantidad)
    print(f"Cadena resultante con rebanadas: {cadena_rebanadas}")

    cadena_sin_rebanadas = eliminar_sin_rebanadas(cadena, posicion, cantidad)
    print(f"Cadena resultante sin rebanadas: {cadena_sin_rebanadas}")

if __name__ == "__main__":
    main()