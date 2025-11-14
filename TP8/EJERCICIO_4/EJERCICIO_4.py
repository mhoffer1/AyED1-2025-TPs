""" Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio."""

def encajan(ficha1, ficha2):
    return bool(set(ficha1) & set(ficha2))

if __name__ == "__main__":
    ficha_a = (3, 4)
    ficha_b = (5, 4)
    if encajan(ficha_a, ficha_b):
        print(f"Las fichas {ficha_a} y {ficha_b} encajan.")
    else:
        print(f"Las fichas {ficha_a} y {ficha_b} no encajan.")