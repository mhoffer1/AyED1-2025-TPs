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
        for col in range(izquierda, derecha + 1):
            matriz[superior][col] = num
            num += 1
        superior += 1
        
        for row in range(superior, inferior + 1):
            matriz[row][derecha] = num
            num += 1
        derecha -= 1
        
        if superior <= inferior:
            for col in range(derecha, izquierda - 1, -1):
                matriz[inferior][col] = num
                num += 1
            inferior -= 1
        
        if izquierda <= derecha:
            for row in range(inferior, superior - 1, -1):
                matriz[row][izquierda] = num
                num += 1
            izquierda += 1
    
    return matriz