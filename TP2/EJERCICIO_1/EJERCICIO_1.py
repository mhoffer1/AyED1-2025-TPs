""" Desarrollar cada una de las siguientes funciones y escribir 
un programa que permita verificar su funcionamiento imprimiendo 
la lista luego de invocar a cada función:
    
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos 
    también será un número al azar de dos dígitos.
    
    b. Calcular y devolver el producto de todos los elementos de la lista anterior.
    
    c. Eliminar todas las apariciones de un valor en la lista anterior. 
    El valor a eliminar se ingresa desde el teclado y la función lo recibe 
    como parámetro. No utilizar listas auxiliares.

    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
    auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""


from random import randint

def cargar_lista_azar():
    """
    Carga una lista con numeros aleatorios de cuatro digitos.
    La cantidad de elementos tambien será un numero aleatorio de dos digitos.
    """
    lista = []
    cantidad = randint(10, 99)
    for _ in range(cantidad):
        lista.append(randint(1000, 9999))
    return lista

def calcular_producto(lista: list[int]) -> int:
    """
    Calcula el producto de todos los elementos de la lista.
    -args: lista (list[int]): La lista de enteros de la cual se calculara el producto.
    -returns: int: El producto de todos los elementos de la lista. 
    """

    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_apariciones(lista: list[int], valor: int):
    """
    Elimina todas las apariciones de un valor en la lista.
    -args: lista (list[int]): La lista de enteros de la cual se eliminaran las apariciones.
           valor (int): El valor a eliminar de la lista.
    """
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            del lista[i]
        else:
            i += 1

def es_capicua(lista: list[int]) -> bool:
    """
    Determina si la lista es capicua.
    -args: lista (list[int]): La lista de enteros a verificar.
    -returns: bool: True si la lista es capicua, False en caso contrario.
    """
    if lista == lista[::-1]:
        return True
    return False

def main():
    """
    Funcion principal que ejecuta el programa.
    """
    lista = cargar_lista_azar()
    print("Lista cargada:", lista)

    producto = calcular_producto(lista)
    print("Producto de los elementos:", producto)

    valor_a_eliminar = int(input("Ingrese un valor a eliminar: "))
    eliminar_apariciones(lista, valor_a_eliminar)
    print("Lista después de eliminar", valor_a_eliminar, ":", lista)

    if es_capicua(lista):
        print("La lista es capicua.")
    else:
        print("La lista no es capicua.")

if __name__ == "__main__":
    main()
