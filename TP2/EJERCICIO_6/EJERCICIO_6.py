"""6. Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones 
relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

def normalizar(lista: list) -> list:
    """
    Normaliza una lista de numeros enteros.
    - args:
        - lista (list): La lista a normalizar.
    - return: La lista normalizada.
    """
    lista_normalizada = []
    total = sum(lista)
    
    if total == 0:
        for i in range(len(lista)):
            lista_normalizada.append(0.0)
        return lista_normalizada

    for x in lista:
        lista_normalizada.append(x / total)
    return lista_normalizada

def main():
    listas = [
        [1, 1, 2],
        [2, 2, 2],
        [1, 0, 0],
        [0, 0, 0]
    ]

    for lista in listas:
        print(f"Lista original: {lista} - Lista normalizada: {normalizar(lista)}")

if __name__ == "__main__":
    main()