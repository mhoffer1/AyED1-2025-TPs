"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.
"""

def centrar_cadena(cadena):
    longitud = len(cadena)
    espacios = (80 - longitud) // 2
    print(" " * espacios + cadena)
    return

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    centrar_cadena(cadena)

if __name__ == "__main__":
    main()