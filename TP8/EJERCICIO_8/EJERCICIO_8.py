"""Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves."""

def generar_diccionario_cuadrados():
    diccionario_cuadrados = {num: num**2 for num in range(1, 21)}
    return diccionario_cuadrados

if __name__ == "__main__":
    diccionario = generar_diccionario_cuadrados()
    print("Diccionario de cuadrados del 1 al 20:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")