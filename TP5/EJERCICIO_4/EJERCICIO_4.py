"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

def imprimir_numeros_hasta_100000():
    """Imprime numeros enteros del 1 al 100000, solicitando confirmacion para detenerse."""
    try:
        for numero in range(1, 100_001):
            print(numero)
    except KeyboardInterrupt:
        confirmar = input("\nDesea detener la ejecucion? (s/n): ").strip().lower()
        if confirmar == 's':
            print("Ejecucion detenida por el usuario.")
        else:
            imprimir_numeros_hasta_100000()


def main():
    imprimir_numeros_hasta_100000()


if __name__ == "__main__":
    main()
