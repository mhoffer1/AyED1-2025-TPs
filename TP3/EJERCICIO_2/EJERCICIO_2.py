"""
Las siguientes matrices responden distintos patrones de relleno. 
Desarrollar funciones que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. 
El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.

a: 01 00 00 00  b: 00 00 00 27   c: 04 00 00 00 
   00 03 00 00     00 00 09 00      03 03 00 00 
   00 00 05 00     00 03 00 00      02 02 02 00 
   00 00 00 07     01 00 00 00      01 01 01 01

d: 08 08 08 08  e: 00 01 00 02   f: 00 00 00 01 
   04 04 04 04     03 00 04 00      00 00 03 02 
   02 02 02 02     00 05 00 06      00 06 05 04 
   01 01 01 01     07 00 08 00      10 09 08 07

g: 01 02 03 04  h: 01 02 04 07   i: 01 02 06 07
   12 13 14 05     03 05 08 11      03 05 08 13
   11 16 15 06     06 09 12 14      04 09 12 14
   10 09 08 07     10 13 15 16      10 11 15 16

"""
import tabulate

def crear_matriz(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con ceros.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con ceros.
    """
    return [[0] * n for _ in range(n)]

def imprimir_matriz(matriz: list[list[int]], matriz_nombre: str) -> None:
    """
    Imprime la matriz en un formato legible.
    args:
        matriz (list[list[int]]): Matriz a imprimir.
        matriz_nombre (str): Nombre de la matriz a imprimir.
    """
    print(f"Matriz {matriz_nombre}:")
    print(tabulate.tabulate(matriz, tablefmt="plain"))
    print()

def matriz_a(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz a.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz a.
    """
    matriz = crear_matriz(n)
    for i in range(n):
        matriz[i][i] = 2 * i + 1
    return matriz

def matriz_b(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz b.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz b.
    """
    matriz = crear_matriz(n)
    for i in range(n):
        matriz[i][n - 1 - i] = 3 ** i
    return matriz

def matriz_c(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz c.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz c.
    """
    matriz = crear_matriz(n)    
    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = n - i
    return matriz

def matriz_d(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz d.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz d.
    """
    matriz = crear_matriz(n)
    
    val = n ** 2
    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(val / 2)
        val = val / 2
    return matriz

def matriz_e(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz e.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz e.
    """
    matriz = crear_matriz(n)
    contador = 1

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                matriz[i][j] = contador
                contador += 1
    return matriz

def matriz_f(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz f.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz f.
    """
    matriz = crear_matriz(n)
    for i in range( 1, n + 1 ):             
        triangular_i = i * ( i + 1 ) // 2  #triangular de i 
        for j in range( 1, n + 1 ): 
            if i + j > n:
                matriz[ i - 1 ][ j - 1 ] = triangular_i - ( i + j - ( n + 1 )) #triangular de i - (i + j - (n + 1))
    return matriz


def matriz_g(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz g.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz g.
    """
    matriz = crear_matriz(n)
    
    superior = 0
    inferior = n - 1
    izquierda = 0
    derecha = n - 1
    
    num = 1
    
    while superior <= inferior and izquierda <= derecha:

        # Rellenar la fila superior
        for col in range(izquierda, derecha + 1):
            matriz[superior][col] = num
            num += 1
        superior += 1
        
        # Rellenar la columna derecha
        for fila in range(superior, inferior + 1):
            matriz[fila][derecha] = num
            num += 1
        derecha -= 1
        
        # Rellenar la fila inferior
        if superior <= inferior:
            for col in range(derecha, izquierda - 1, -1):
                matriz[inferior][col] = num
                num += 1
            inferior -= 1
        
        # Rellenar la columna izquierda
        if izquierda <= derecha:
            for fila in range(inferior, superior - 1, -1):
                matriz[fila][izquierda] = num
                num += 1
            izquierda += 1
    
    return matriz

def matriz_h(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz h.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz h.
    """
    matriz = crear_matriz(n)
    # num = 1
    # for k in range(n * 2 - 1):
    #     for i in range(k + 1):
    #         j = k - i
    #         if i < n and j < n:
    #             matriz[i][j] = num
    #             num += 1
    # return matriz

    num = 1
    for s in range( 2*n - 1):              
        i_min = max(0, s - (n - 1))
        i_max = min(n - 1, s)
        for i in range(i_min, i_max + 1):
            j = s - i
            matriz[i][j] = num
            num += 1
    return matriz

def matriz_i(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con los valores de la matriz i.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con los valores de la matriz i.
    """
    matriz = crear_matriz(n)
    num = 1
    
    for diag in range(n * 2 - 1):
        coords = []
        
        for i in range(diag + 1):
            j = diag - i
            if i < n and j < n:
                coords.append((i, j))
        
        # Si la diagonal es impar, invertir el orden
        if diag % 2 == 1:
            coords.reverse()

        for i, j in coords:
            matriz[i][j] = num
            num += 1
    
    return matriz
    

def main():
    n = int(input("Ingrese el tamaño de la matriz (N x N): "))

    imprimir_matriz(matriz_a(n), 'A')
    imprimir_matriz(matriz_b(n), 'B')
    imprimir_matriz(matriz_c(n), 'C')
    imprimir_matriz(matriz_d(n), 'D')
    imprimir_matriz(matriz_e(n), 'E')
    imprimir_matriz(matriz_f(n), 'F')
    imprimir_matriz(matriz_g(n), 'G')
    imprimir_matriz(matriz_h(n), 'H')
    imprimir_matriz(matriz_i(n), 'I')

if __name__ == "__main__":
    main()