from typing import List

def crear_matriz(n: int) -> List[List[float]]:
    """
    Crea una matriz de tamaño n x n con ceros.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        List: Matriz de tamaño n x n con ceros.
    """
    return [[0] * n for _ in range(n)]
    
def imprimir_matriz(matriz: List[List[float]]) -> None:
    """
    Imprime la matriz en un formato legible.
    args:
        matriz (List[List[float]]): Matriz a imprimir.
    """
    for fila in matriz:
        print(fila)

# Definir el tamaño de la matriz
n = 3  # Puedes cambiar este valor

# Crear la matriz
matriz = crear_matriz(n)
nueva_matriz = crear_matriz(n)

num = 1
for i in range(n):
    for j in range(n):
        matriz[i][j] = num
        num += 1

resultado = []

while matriz:
    resultado += matriz.pop(0)
    matriz = (list(zip(*matriz)))[::-1]

num = 0
for i in range(n):
    for j in range(n):
        nueva_matriz[i][j] = resultado[num]
        num += 1

imprimir_matriz(nueva_matriz)