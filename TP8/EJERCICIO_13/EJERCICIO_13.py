"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic
cionario. Comprobar el comportamiento de la función mediante un programa apro
piado."""

def buscar_clave(diccionario, valor):
    claves_encontradas = [clave for clave, val in diccionario.items() if val == valor]
    return claves_encontradas

if __name__ == "__main__":
    dicc = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    valor_a_buscar = 2
    
    claves = buscar_clave(dicc, valor_a_buscar)
    
    if claves:
        print(f"Las claves que mapean al valor {valor_a_buscar} son: {claves}")
    else:
        print(f"No se encontraron claves que mapeen al valor {valor_a_buscar}.")
