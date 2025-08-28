"""3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 
"""
def main():
    lista = []
    n = int(input("Ingrese un numero entero positivo N: "))

    for i in range(1, n + 1):
        lista.append(i ** 2)

    print("Los ultimos 10 valores de la lista son:")
    for valor in lista[-10:]:
        print(valor)

if __name__ == "__main__":
    main()