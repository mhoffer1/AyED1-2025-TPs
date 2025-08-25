"""5. Escribir funciones lambda para:

   **a.** Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
   multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 × 3.

   **b.** Informar si un número es triangular. Un número se define como triangular si puede expresarse como la suma de un grupo de números naturales 
   consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular porque se obtiene sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven `True` o `False`. No se permite utilizar ayudas externas a las mismas."""


def main():

    #funcion oblongo
    es_oblongo = lambda n: int((4 * n + 1) ** 0.5) ** 2 == 4 * n + 1

    #funcion triangular
    es_triangular = lambda n: int((8 * n + 1) ** 0.5) ** 2 == 8 * n + 1

    numero = int(input("Ingrese un numero: "))
    print(f"El numero {numero} es oblongo? {es_oblongo(numero)}")
    print(f"El numero {numero} es triangular? {es_triangular(numero)}")

if __name__ == "__main__":
    main()

