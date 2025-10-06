"""
3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2
), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
"""

from random import randint
import tabulate

def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz en un formato tabular.
    args:
        matriz (list[list[int]]): Matriz a imprimir.
    returns:
        None
    """
    print(tabulate.tabulate(matriz, tablefmt="grid"))
    print()

def cargar_matriz_azar(n: int) -> list[list[int]]:
    """
    Carga una matriz de tamaño n x n con numeros enteros al azar en el intervalo 0, n^2
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con numeros enteros al azar sin repetir.
    """
    matriz = []
    numeros_usados = set()
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                num = randint(0, n*n - 1)
                if num not in numeros_usados:
                    numeros_usados.add(num)
                    fila.append(num)
                    break
        matriz.append(fila)
    return matriz

def main():
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz = cargar_matriz_azar(n)
    print("Matriz generada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()