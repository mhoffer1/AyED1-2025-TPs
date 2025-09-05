"""9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""

def generar_lista(a:int, b:int) -> list[int]:
    """
    Genera una lista entre A y B con los multiplos de 7 que no
    sean multiplos de 5.
    args: a entero, b entero
    returns: list
    """
    return [x for x in range(a, b) if x % 7 == 0 and x % 5 != 0]

def main():
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    lista = generar_lista(a, b + 1)
    print(f"Lista generada: {lista}")

if __name__ == "__main__":
    main()
