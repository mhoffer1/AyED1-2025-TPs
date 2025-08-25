"""6. Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase."""

def leer_positivo(texto: str) -> str:
    """
    Lee un numero entero positivo desde la entrada estandar.
    - recibe: texto (str) que se muestra al usuario
    - retorna: el numero ingresado como string
    """
    n = -1
    while n < 0:
        n = int(input(texto))
        if n < 0:
            print("El numero debe ser positivo.")
        else:
            return n
        
def concatenar(a: int, b: int) -> int:
    """
    Concatenar dos numeros enteros.
    - recibe: dos numeros enteros
    - retorna: la concatenacion de los dos numeros
    """
    return a * 10 ** len(str(b)) + b

def main():

    num1 = leer_positivo("Ingrese el primer numero: ")
    num2 = leer_positivo("Ingrese el segundo numero: ")

    resultado = concatenar(num1, num2)
    print(f"El resultado de la concatenacion es: {resultado}")

if __name__ == "__main__":
    main()