""" El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def cargar_lista_enteros() -> list:
    """Carga una lista con numeros enteros ingresados por el usuario hasta -1.

    Returns:
        list: Lista de numeros enteros ingresados.
    """
    lista = []
    while True:
        try:
            entrada = input("Ingrese un numero entero (-1 para terminar): ")
            numero = int(entrada)
            if numero == -1:
                break
            lista.append(numero)
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")
    return lista


def buscar_elementos_en_lista(lista: list):
    """Permite al usuario buscar elementos en la lista e imprime su posicion.

    Args:
        lista (list): Lista de numeros enteros donde se buscara.
    """
    errores = 0
    while errores < 3:
        try:
            entrada = input("Ingrese un numero para buscar en la lista: ")
            numero_a_buscar = int(entrada)
            posicion = lista.index(numero_a_buscar)
            print(f"El numero {numero_a_buscar} se encuentra en la posicion {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: El numero {numero_a_buscar} no se encuentra en la lista. Intentos restantes: {3 - errores}")
    if errores == 3:
        print("Se han alcanzado el maximo de errores. Proceso abortado.")


def main():
    lista_enteros = cargar_lista_enteros()
    buscar_elementos_en_lista(lista_enteros)


if __name__ == "__main__":
    main()