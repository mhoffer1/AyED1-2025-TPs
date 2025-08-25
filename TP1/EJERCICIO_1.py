"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def leer_positivo(texto: str) -> int:
    """
    Lee un numero entero positivo

    - recibe: un texto que se muestra al usuario para solicitar el numero
    - retorna: un numero entero positivo
    
    """
    n = -1
    while n < 0:
        n = int(input(texto))
        if n < 0:
            print("El numero debe ser positivo.")
        else:
            return n

def encontar_maximo(a: int, b: int, c: int) -> int:
    """
    Encuentra el maximo de tres numeros enteros.
    - recibe: tres numeros enteros
    - retorna: el maximo de los tres numeros o -1 si no hay un maximo unico
    """

    maximo = max(a, b, c)
    
    count = 0
    if a == maximo:
        count += 1
    if b == maximo:
        count += 1
    if c == maximo:
        count += 1
    if count == 1:
        return maximo
    else:
        return -1
    
def main():
    
    num1 = leer_positivo("Ingrese el primer numero: ")
    num2 = leer_positivo("Ingrese el segundo numero: ")
    num3 = leer_positivo("Ingrese el tercer numero: ")

    resultado = encontar_maximo(num1, num2, num3)

    if resultado == -1:
        print("No hay un maximo unico.")
    else:
        print(f"El maximo unico es: {resultado}")

if __name__ == "__main__":
    main()