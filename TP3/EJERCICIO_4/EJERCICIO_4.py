"""
Una fabrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re
presenta el dia de la semana y cada fila a una de sus fabricas. Ejemplo:

+----------------+--------+---------+-----------+---------+--------+----------+
|                | Lunes  | Martes  | Miércoles | Jueves  | Viernes| Sabado   |
|                |   0    |    1    |     2     |    3    |   4    |    5     |
+----------------+--------+---------+-----------+---------+--------+----------+
| (Fabrica 1) 0  |   23   |   150   |    20     |   120   |   25   |   150    |
| (Fabrica 2) 1  |   40   |    75   |    80     |    0    |   80   |    35    |
| (... )         |  ...   |   ...   |   ...     |   ...   |  ...   |   ...    |
| (Fabrica n) 3  |   80   |    80   |    80     |    80   |   80   |    80    |
+----------------+--------+---------+-----------+---------+--------+----------+

a. Crear una matriz con datos generados al azar para N fabricas durante una 
   semana, considerando que la capacidad maxima de fabricacion es de 150 
   unidades por dia y puede suceder que en ciertos dias no se fabrique ninguna. 
    
b. Mostrar la cantidad total de bicicletas fabricadas por cada fabrica. 
    
c. Cual es la fabrica que mas produjo en un solo dia (detallar dia y fabrica).
    
d. Cual es el dia mas productivo, considerando todas las fabricas combinadas.
    
e. Crear una lista por comprension que contenga la menor cantidad fabricada 
   por cada fabrica.
"""

import random
import tabulate

def crear_matriz_azar(fabricas: int, dias: int, max_produccion: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño fabricas x dias con datos generados al azar.
    args:
        fabricas (int): Numero de fabricas (filas).
        dias (int): Numero de dias (columnas).
        max_produccion (int): Capacidad maxima de fabricacion por dia.
    returns:
        list: Matriz de tamaño fabricas x dias con datos generados al azar.
    """
    return [[random.randint(0, max_produccion) for _ in range(dias)] for _ in range(fabricas)]

def total_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Calcula la cantidad total de bicicletas fabricadas por cada fabrica.
    args:
        matriz (list[list[int]]): Matriz de produccion.
    returns:
        list: Lista con la cantidad total de bicicletas por fabrica.
    """
    return [sum(fabrica) for fabrica in matriz]

def fabrica_mas_produccion_dia(matriz: list[list[int]]) -> tuple[int, int, int]:
    """
    Encuentra la fabrica que mas produjo en un solo dia.
    args:
        matriz (list[list[int]]): Matriz de produccion.
    returns:
        tuple: (fabrica, dia, cantidad) que mas produjo en un solo dia.
    """
    max_produccion = -1
    fabrica_max = -1
    dia_max = -1
    for i, fabrica in enumerate(matriz):
        for j, produccion in enumerate(fabrica):
            if produccion > max_produccion:
                max_produccion = produccion
                fabrica_max = i
                dia_max = j
    return (fabrica_max, dia_max, max_produccion)

def dia_mas_productivo(matriz: list[list[int]]) -> tuple[int, int]:
    """
    Encuentra el dia mas productivo considerando todas las fabricas combinadas.
    args:
        matriz (list[list[int]]): Matriz de produccion.
    returns:
        tuple: (dia, cantidad total) que fue el mas productivo.
    """
    dias = len(matriz[0])
    max_produccion_dia = -1
    dia_max = -1
    for j in range(dias):
        produccion_dia = sum(matriz[i][j] for i in range(len(matriz)))
        if produccion_dia > max_produccion_dia:
            max_produccion_dia = produccion_dia
            dia_max = j
    return (dia_max, max_produccion_dia)

def menor_cantidad_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Crea una lista con la menor cantidad fabricada por cada fabrica.
    args:
        matriz (list[list[int]]): Matriz de produccion.
    returns:
        list: Lista con la menor cantidad fabricada por cada fabrica.
    """
    return [min(fabrica) for fabrica in matriz]

def imprimir_datos(matriz: list[list[int]], nombres_fabricas: list[str], dias_semana: list[str]) -> None:
    """
    Imprime los datos de produccion de las fabricas.
    args:
        matriz (list[list[int]]): Matriz de produccion.
        nombres_fabricas (list[str]): Nombres de las fabricas.
        dias_semana (list[str]): Nombres de los dias de la semana.
    """
    print("Datos de Produccion:")
    print(tabulate.tabulate(matriz, headers=dias_semana, showindex=nombres_fabricas, tablefmt="grid"))
    print()


# Parametros
num_fabricas = 4
num_dias = 6
max_produccion = 150
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]
nombres_fabricas = [f"Fabrica {i+1}" for i in range(num_fabricas)]

# Crear matriz de produccion
matriz_produccion = crear_matriz_azar(num_fabricas, num_dias, max_produccion)
imprimir_datos(matriz_produccion, nombres_fabricas, dias_semana)

# Cantidad total por fabrica
totales = total_por_fabrica(matriz_produccion)
for i, total in enumerate(totales):
    print(f"{nombres_fabricas[i]} produjo un total de {total} bicicletas.")
print()

# Fabrica que mas produjo en un solo dia
fabrica_max, dia_max, cantidad_max = fabrica_mas_produccion_dia(matriz_produccion)
print(f"La {nombres_fabricas[fabrica_max]} fue la que mas produjo en un solo dia: {cantidad_max} bicicletas el dia {dias_semana[dia_max]}.")
print()

# Dia mas productivo
dia_productivo, cantidad_productiva = dia_mas_productivo(matriz_produccion)
print(f"El dia mas productivo fue el {dias_semana[dia_productivo]} con un total de {cantidad_productiva} bicicletas producidas.")
for i in range(num_fabricas):
    print(f"La menor cantidad producida por {nombres_fabricas[i]} es: {menor_cantidad_por_fabrica(matriz_produccion)[i]}")