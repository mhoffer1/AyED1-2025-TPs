"""Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y una lista de claves. La función debe eliminar del diccionario todas las claves 
contenidas en la lista, devolviendo el diccionario modificado y un número entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento."""

def eliminar_claves(diccionario, lista_claves):
    contador = 0
    for clave in lista_claves:
        if clave in diccionario:
            del diccionario[clave]
            contador += 1
    return diccionario, contador

if __name__ == "__main__":
    dicc = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    claves_a_eliminar = ['b', 'd', 'e']
    
    dicc_modificado, cantidad_eliminadas = eliminar_claves(dicc, claves_a_eliminar)
    
    print(f"Diccionario modificado: {dicc_modificado}")
    print(f"Cantidad de claves eliminadas: {cantidad_eliminadas}")