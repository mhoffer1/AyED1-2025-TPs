"""
Las siguientes matrices responden distintos patrones de relleno. 
Desarrollar funciones que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. 
El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.

a: 1 0 0 0, 0 3 0 0, 0 0 5 0, 0 0 0 7 
b: 0 0 0 27, 0 0 9 0, 0 3 0 0, 1 0 0 0 
c: 4 0 0 0, 3 3 0 0, 2 2 2 0, 1 1 1 1
d: 8 8 8 8, 4 4 4 4, 2 2 2 2, 1 1 1 1
e: 0 1 0 2, 3 0 4 0, 0 5 0 6, 7 0 8 0
f: 0 0 0 1, 0 0 3 2, 0 6 5 4, 10 9 8 7
g: 1 2 3 4, 12 13 14 5, 11 16 15 6, 10 9 8 7
h: 1 2 4 7, 3 5 8 11, 6 9 12 14, 10 13 15 16
i: 1 2 6 7, 3 5 8 13, 4 9 12 14, 10 15 11 16
"""
def crear_matriz(n: int) -> list:
    return [[0] * n for _ in range(n)]

def matriz_a(n: int) -> list:
    matriz = crear_matriz(n)
    for i in range(n):
        matriz[i][i] = 2 * i + 1
    return matriz

def matriz_b(n: int) -> list:
    matriz = crear_matriz(n)
    for i in range(n):
        matriz[i][n - 1 - i] = 3 ** i
    return matriz

def matriz_c(n: int) -> list:
    matriz = crear_matriz(n)
    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = n - i
    return matriz

def main():
    n = int(input("Ingrese el tamaño de la matriz (N x N): "))

    print("Matriz A:")
    matriz = matriz_a(n)
    for fila in matriz:
        print(fila)
    print()
    print("Matriz B:")
    matriz = matriz_b(n)
    for fila in matriz:
        print(fila)
    print()
    print("Matriz C:")
    matriz = matriz_c(n)
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()