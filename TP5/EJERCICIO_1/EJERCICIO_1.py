"""Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funciona
miento de la misma.
"""
def ingresar_numero_natural() -> int:
    """Solicita al usuario ingresar un numero natural y valida la entrada.
    
    Raises:
        ValueError: Si la entrada no es un numero, no es entero o no es mayor que 0.
    
    Returns:
        int: El numero natural ingresado por el usuario.
    """
    while True:
        try:
            entrada = input("Ingrese un numero natural (entero mayor que 0): ")
            numero = float(entrada)
            if not numero.is_integer():
                raise ValueError("El numero ingresado no es un entero.")
            numero = int(numero)
            if numero <= 0:
                raise ValueError("El numero ingresado no es mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}")

def main():
    numero_natural = ingresar_numero_natural()
    print(f"Numero natural ingresado correctamente: {numero_natural}")

if __name__ == "__main__":
    main()
    

