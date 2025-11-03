"""Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más.
"""

import random

def jugar_adivinar_numero():
    """Juega al juego de adivinar un numero con el usuario."""
    numero_a_adivinar = random.randint(1, 500)
    intentos = 0
    print("numero entre 1 y 500 seleccionado. podes adivinar cual es?")
    
    while True:
        entrada = input("Introduci tu respuesta: ")
        intentos += 1
        try:
            intento = int(entrada)
            if intento < 1 or intento > 500:
                print("Por favor, ingresa un nUmero entre 1 y 500.")
                continue
            if intento < numero_a_adivinar:
                print("El nUmero a adivinar es mayor.")
            elif intento > numero_a_adivinar:
                print("El nUmero a adivinar es menor.")
            else:
                print(f"Has adivinado el nUmero {numero_a_adivinar} en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada invalida. Por favor, ingresa un numero entero.")

def main():
    jugar_adivinar_numero()

if __name__ == "__main__":
    main()