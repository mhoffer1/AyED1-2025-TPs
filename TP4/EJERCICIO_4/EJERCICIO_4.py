"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?
"""

def entero_a_romano(num: int) -> str:
    """
    Convierte un numero entero en un numero romano.
    args:
        num (int): Numero entero entre 0 y 3999.
    returns:
        str: numero romano.
    """

    if not (0 < num < 4000):
        raise ValueError("El numero debe estar entre 1 y 3999.")
    
    conversiones = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    romano = ""
    for valor, simbolo in conversiones:
        cantidad, num = divmod(num, valor)
        romano += simbolo * cantidad
    return romano

def main():
    numero = int(input("Ingrese un numero entero entre 1 y 3999: "))
    try:
        romano = entero_a_romano(numero)
        print(f"El numero romano es: {romano}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()