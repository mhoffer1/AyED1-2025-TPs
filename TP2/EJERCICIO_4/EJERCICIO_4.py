"""4. Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

def eliminar_valores(lista: list[int], valores_a_eliminar: list[int]):
    """
    Elimina de la lista los valores que se encuentran en valores_a_eliminar.
    - args:
        - lista (list[int]): La lista de enteros de la cual se eliminaran los valores.
        - valores_a_eliminar (list[int]): La lista de valores a eliminar de la lista original.
    """
    for valor in valores_a_eliminar:
        while valor in lista:
            lista.remove(valor)

def main():
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    valores_a_eliminar = [2, 4, 6, 8, 10]

    print(f"Lista original: {lista_original}")
    print(f"Valores a eliminar: {valores_a_eliminar}")

    eliminar_valores(lista_original, valores_a_eliminar)

    print(f"Lista resultante: {lista_original}")

if __name__ == "__main__":
    main()
