"""1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
    
    a. Cargar numeros enteros en una matriz de N x N, ingresando los datos desde
        teclado.
    b. Ordenar en forma ascendente cada una de las filas de la matriz.
    c. Intercambiar dos filas, cuyos numeros se reciben como parámetro.
    d. Intercambiar dos columnas dadas, cuyos numeros se reciben como parámetro.
    e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
    f. Calcular el promedio de los elementos de una fila, cuyo numero se recibe como
        parámetro.
    g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo numero se recibe como parámetro.
    h. Determinar si la matriz es simetrica con respecto a su diagonal principal.
    i. Determinar si la matriz es simetrica con respecto a su diagonal secundaria.
    j. Determinar que columnas de la matriz son palindromos (capicuas), devolviendo
        una lista con los numeros de las mismas.

NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado"""

def cargar_matriz(n: int) -> list[list[int]]:
    """
    Carga una matriz de tamaño n x n con numeros enteros ingresados por el usuario.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list[list[int]]: Matriz cargada con numeros enteros.
    """
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            num = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def ordenar_filas(matriz: list[list[int]]) -> list[list[int]]:
    """
    Ordena en forma ascendente cada una de las filas de la matriz.
    args:
        matriz (list[list[int]]): Matriz a ordenar.
    returns:
        list[list[int]]: Matriz con filas ordenadas.
    """
    for fila in matriz:
        fila.sort()
    return matriz

def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> list[list[int]]:
    """
    Intercambia dos filas de la matriz.
    args:
        matriz (list[list[int]]): Matriz en la que se intercambian las filas.
        fila1 (int): Numero de la primera fila a intercambiar.
        fila2 (int): Numero de la segunda fila a intercambiar.
    returns:
        list[list[int]]: Matriz con las filas intercambiadas.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> list[list[int]]:
    """
    Intercambia dos columnas de la matriz.
    args:
        matriz (list[list[int]]): Matriz en la que se intercambian las columnas
        col1 (int): Numero de la primera columna a intercambiar.
        col2 (int): Numero de la segunda columna a intercambiar.
    returns:
        list[list[int]]: Matriz con las columnas intercambiadas.
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

def trasponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    Traspone la matriz sobre si misma (intercambia cada elemento).
    args:
        matriz (list[list[int]]): Matriz a trasponer."""
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila.
    args:
        matriz (list[list[int]]): Matriz de la cual se calcula el promedio.
        fila (int): Numero de la fila para calcular el promedio.
    returns:
        float: Promedio de los elementos en la fila especificada.
    """
    return sum(matriz[fila]) / len(matriz[fila])

def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:
    """
    Calcula el porcentaje de elementos con valor impar en una columna.
    args:
        matriz (list[list[int]]): Matriz de la cual se calcula el porcentaje.
        columna (int): Numero de la columna para calcular el porcentaje de impares.
    returns:
        float: Porcentaje de elementos impares en la columna especificada.
    """
    total = len(matriz)
    impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
    return (impares / total) * 100

def es_simetrica_diagonal_principal(matriz: list[list[int]]) -> bool:
    """
    Determina si la matriz es simetrica con respecto a su diagonal principal.
    args:
        matriz (list[list[int]]): Matriz a verificar.
    returns:
        bool: True si la matriz es simetrica, False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_simetrica_diagonal_secundaria(matriz: list[list[int]]) -> bool:
    """
    determina si la matriz es simetrica con respecto a su diagonal secundaria.
    args:
        matriz (list[list[int]]): Matriz a verificar.
    returns:
        bool: True si la matriz es simetrica, False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n - i - 1):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return False
    return True

def columnas_palindromos(matriz: list[list[int]]) -> list[int]:
    """
    Determina que columnas de la matriz son palindromos (capicuas).
    args:
        matriz (list[list[int]]): Matriz a verificar.
    returns:
        list[int]: Lista con los numeros de las columnas que son palindromos.
    """
    palindromos = []
    n = len(matriz)
    for col in range(n):
        columna = [matriz[fila][col] for fila in range(n)]
        if columna == columna[::-1]:
            palindromos.append(col)
    return palindromos

def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz en un formato legible.
    args:
        matriz (list[list[int]]): Matriz a imprimir.
    """
    for fila in matriz:
        print(fila)

def main():
    n = int(input("Ingrese el tamaño de la matriz N x N: "))
    matriz = cargar_matriz(n)
    print("Matriz cargada:")
    imprimir_matriz(matriz)

    matriz = ordenar_filas(matriz)
    print("Matriz con filas ordenadas:")
    imprimir_matriz(matriz)

    fila1 = int(input("Ingrese el numero de la primera fila a intercambiar: "))
    fila2 = int(input("Ingrese el numero de la segunda fila a intercambiar: "))
    matriz = intercambiar_filas(matriz, fila1, fila2)
    print("Matriz despues de intercambiar filas:")
    imprimir_matriz(matriz)

    col1 = int(input("Ingrese el numero de la primera columna a intercambiar: "))
    col2 = int(input("Ingrese el numero de la segunda columna a intercambiar: "))
    matriz = intercambiar_columnas(matriz, col1, col2)
    print("Matriz despues de intercambiar columnas:")
    imprimir_matriz(matriz)

    matriz = trasponer_matriz(matriz)
    print("Matriz traspuesta:")
    imprimir_matriz(matriz)

    fila = int(input("Ingrese el numero de la fila para calcular el promedio: "))
    promedio = promedio_fila(matriz, fila)
    print(f"Promedio de los elementos en la fila {fila}: {promedio}")

    columna = int(input("Ingrese el numero de la columna para calcular el porcentaje de impares: "))
    porcentaje = porcentaje_impares_columna(matriz, columna)
    print(f"Porcentaje de elementos impares en la columna {columna}: {porcentaje}%")

    if es_simetrica_diagonal_principal(matriz):
        print("La matriz es simetrica con respecto a su diagonal principal.")
    else:
        print("La matriz no es simetrica con respecto a su diagonal principal.")

    if es_simetrica_diagonal_secundaria(matriz):
        print("La matriz es simetrica con respecto a su diagonal secundaria.")
    else:
        print("La matriz no es simetrica con respecto a su diagonal secundaria.")

    palindromos = columnas_palindromos(matriz)
    print(f"Columnas que son palindromos: {palindromos}")
