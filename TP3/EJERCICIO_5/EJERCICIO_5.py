"""
Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar  las siguientes funciones y utilizarlas 
en un mismo programa:

    mostrar_butacas: Mostrara por pantalla el estado de cada una de las butacas 
    del cine. Esta función debera ser invocada antes de que se realice la reserva, y 
    se volvera a invocar luego de la misma con los estados actualizados.
 
    reservar: Debera recibir una matriz y la butaca seleccionada, y actualizara la 
    sala en caso de estar disponible dicha butaca. La función devolvera True/False 
    si logró o no reservar la butaca.
 
    cargar_sala: Recibira una matriz como parametro y la cargara con valores 
    aleatorios para simular una sala con butacas ya reservadas.
 
    butacas_libres: Recibira como parametro la matriz y retornara cuantas butacas 
    desocupadas hay en la sala.
    
    butacas_contiguas: Buscara la secuencia mas larga de butacas libres contiguas
    en una misma fila y devolvera las coordenadas de inicio de la misma.
"""

import random

def crear_matriz(n: int) -> list[list[int]]:
    """
    Crea una matriz de tamaño n x n con ceros.
    args:
        n (int): Tamaño de la matriz (n x n).
    returns:
        list: Matriz de tamaño n x n con ceros.
    """
    return [[0] * n for _ in range(n)]

def mostrar_butacas(sala: list[list[int]]) -> None:
    """
    Muestra por pantalla el estado de cada una de las butacas del cine.
    args:
        sala (list[list[int]]): Matriz que representa la sala de cine.
    """
    print("Estado de las butacas (0: libre, 1: ocupada):")
    print("    ", end="")
    for j in range(len(sala[0])):
        print(f"{ j+1:3}", end=" ")
    print()
    
    for i, fila in enumerate(sala):
        print(f"{i+1:2}: ", end="")
        for butaca in fila:
            print(f"{butaca:3}", end=" ")
        print()
    print()

def reservar(sala: list[list[int]], fila: int, butaca: int) -> bool:
    """
    Reserva una butaca en la sala si esta disponible.
    args:
        sala (list[list[int]]): Matriz que representa la sala de cine.
        fila (int): Fila de la butaca a reservar (0-indexed).
        butaca (int): Numero de la butaca a reservar (0-indexed).
    returns:
        bool: True si la reserva fue exitosa, False si la butaca ya estaba ocupada.
    """

    if fila < 0 or fila >= len(sala) or butaca < 0 or butaca >= len(sala[0]):
        return False
    
    if sala[fila][butaca] == 0:
        sala[fila][butaca] = 1
        return True
    else:
        return False
    
def cargar_sala(sala: list[list[int]]) -> None:
    """
    Carga la sala con valores aleatorios para simular butacas ya reservadas.
    args:
        sala (list[list[int]]): Matriz que representa la sala de cine.
    """
    for i in range(len(sala)):
        for j in range(len(sala[0])):
            sala[i][j] = random.choice([0, 1])

def butacas_libres(sala: list[list[int]]) -> int:
    """
    Cuenta cuantas butacas desocupadas hay en la sala.
    args:
        sala (list[list[int]]): Matriz que representa la sala de cine.
    returns:
        int: Numero de butacas libres.
    """
    return sum(butaca == 0 for fila in sala for butaca in fila)

def butacas_contiguas(sala: list[list[int]]) -> tuple[int, int] | None:
    """
    Busca la secuencia mas larga de butacas libres contiguas en una misma fila.
    args:
        sala (list[list[int]]): Matriz que representa la sala de cine.
    returns:
        tuple[int, int] | None: Coordenadas (fila, butaca_inicio) de la secuencia mas larga,
                                o None si no hay butacas libres.
    """
    max_longitud = 0
    coordenadas_inicio = None

    for i in range(len(sala)):
        longitud_actual = 0
        inicio_actual = None

        for j in range(len(sala[0])):
            if sala[i][j] == 0:  # Butaca libre
                if longitud_actual == 0:
                    inicio_actual = j
                longitud_actual += 1
            else:  # Butaca ocupada
                if longitud_actual > max_longitud:
                    max_longitud = longitud_actual
                    coordenadas_inicio = (i, inicio_actual)
                longitud_actual = 0

        # Verificar al final de la fila
        if longitud_actual > max_longitud:
            max_longitud = longitud_actual
            coordenadas_inicio = (i, inicio_actual)

    return coordenadas_inicio

def main():
    n = 5  
    m = 7  

    sala = crear_matriz(n, m)
    cargar_sala(sala)
    
    mostrar_butacas(sala)

    try:
        fila = int(input(f"Ingrese la fila para reservar (1-{n}): "))
        butaca = int(input(f"Ingrese el numero de butaca para reservar (1-{m}): "))

        if reservar(sala, fila - 1, butaca - 1):
            print("\n Butaca reservada con éxito.\n")
        else:
            print("\n La butaca ya esta ocupada o los indices son invalidos.\n")
    except ValueError:
        print("\n Error: debe ingresar numeros enteros.\n")
        return

    mostrar_butacas(sala)

    libres = butacas_libres(sala)
    print(f"Numero de butacas libres: {libres}")

    contiguas = butacas_contiguas(sala)
    if contiguas:
        max_seq_len = 0
        # Calcular longitud de la secuencia encontrada
        for j in range(contiguas[1], len(sala[0])):
            if sala[contiguas[0]][j] == 0:
                max_seq_len += 1
            else:
                break
        print(f"Secuencia mas larga de butacas libres ({max_seq_len} butacas): Fila {contiguas[0]+1}, Butaca {contiguas[1]+1}")
    else:
        print("No hay butacas libres.")

if __name__ == "__main__":
    main()