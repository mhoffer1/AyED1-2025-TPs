"""
10. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso debera realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla.
"""

from random import randint

def generar_lista_azar(n:int) -> list[int]:
    """
    Genera una lista con n numeros al azar entre 1 y 100.
    args: n entero
    returns: list
    """
    return [randint(1, 100) for _ in range(n)]

def filtrar_impares(lista:list[int]) -> list[int]:
    """
    Filtra los numeros impares de una lista.
    args: lista list
    returns: list
    """
    return list(filter(lambda x: x % 2 != 0, lista))

def main():
    n = int(input("Ingrese la cantidad de numeros a generar: "))
    lista_azar = generar_lista_azar(n)
    lista_impares = filtrar_impares(lista_azar)
    print(f"Lista generada: {lista_azar}")
    print(f"Lista de impares: {lista_impares}")

if __name__ == "__main__":
    main()
