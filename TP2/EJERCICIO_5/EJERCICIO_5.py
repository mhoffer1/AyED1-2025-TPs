"""5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. 
"""

def check_orden(lista: list) -> bool:
    """
    Verifica si la lista estaa ordenada en forma ascendente.
    - args:
        - lista (list): La lista a verificar.
    - return: True si la lista esta ordenada, False en caso contrario.
    """

    if lista == sorted(lista):
        return True
    return False

def check_orden_variante(lista: list) -> bool:
    """
    Verifica si la lista esta ordenada en forma ascendente.
    - args:
        - lista (list): La lista a verificar.
    - return: True si la lista esta ordenada, False en caso contrario.
    """

    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def main():
    listas = [
        [1, 2, 3],
        [3, 2, 1],
        ['a', 'b', 'c'],
        ['c', 'b', 'a'],
        [1, 2, 2, 3, 4]
    ]

    for lista in listas:
        print(f"Lista: {lista} - Ordenada: {check_orden(lista)}")
        print(f"Lista: {lista} - Ordenada Variante: {check_orden_variante(lista)}")

if __name__ == "__main__":
    main()