"""Escribir un programa que permita ingresar un número entero N y genere un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado."""

def generar_tabla_multiplicar(n):
    tabla_multiplicar = {i: n * i for i in range(1, 13)}
    return tabla_multiplicar

if __name__ == "__main__":
    N = int(input("Ingrese un numero entero para generar su tabla de multiplicar: "))
    tabla = generar_tabla_multiplicar(N)
    
    print(f"Tabla de multiplicar del {N}:")
    for i in range(1, 13):
        print(f"{N} x {i} = {tabla[i]}")