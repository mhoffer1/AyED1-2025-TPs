"""
3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2
), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
"""

from random import randint
import tabulate

def imprimir_matriz(matriz):
    print(tabulate.tabulate(matriz, tablefmt="grid"))
    print()

def cargar_matriz_azar(n):
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

n = int(input("Ingrese el tamaño de la matriz (N): "))
matriz = cargar_matriz_azar(n)
print("Matriz generada:")
imprimir_matriz(matriz)