""" 2. Escribir funciones para:
        a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
           a través del teclado.
        
        b. Recibir una lista como parámetro y devolver True si la misma contiene algún
           elemento repetido. La función no debe modificar la lista.

        c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
           únicos de la lista original, sin importar el orden.

   Combinar estas tres funciones en un mismo programa.
"""

from random import randint

def generar_lista_aleatoria(n: int) -> list[int]:
    """
    Genera una lista de n números aleatorios del 1 al 100.
    -args: n (int): La cantidad de números aleatorios a generar.
    -returns: list[int]: La lista de números aleatorios generados.
    """
    lista = []

    for _ in range(n):
        lista.append(randint(1, 100))

    return lista

def contiene_repetidos(lista: list[int]) -> bool:
    """
    Verifica si la lista contiene elementos repetidos.
    -args: lista (list[int]): La lista a verificar.
    -returns: bool: True si hay elementos repetidos, False en caso contrario.
    """
    return len(lista) != len(set(lista))

def elementos_unicos(lista: list[int]) -> list[int]:
    """
    Devuelve una nueva lista con los elementos unicos de la lista original.
    -args: lista (list[int]): La lista de entrada.
    -returns: list[int]: La lista de elementos unicos.
    """
    return list(set(lista))

def main():
    n = int(input("Ingrese la cantidad de elementos a generar: "))
    lista = generar_lista_aleatoria(n)
    print("Lista generada:", lista)

    if contiene_repetidos(lista):
        print("La lista contiene elementos repetidos.")
    else:
        print("La lista no contiene elementos repetidos.")

    lista_unicos = elementos_unicos(lista)
    print("Lista de elementos únicos:", lista_unicos)

if __name__ == "__main__":
    main()
