"""
Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. 
La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla. 
"""

def crear_baraja():
    """
    Crea una lista por comprensión con los naipes de la baraja española.
    returns:
        list: Lista con los naipes de la baraja española.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    valores = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
    baraja = [f"{valor} {palo}" for palo in palos for valor in valores]
    return baraja

def main():
    baraja = crear_baraja()
    print("Baraja española:")
    print(baraja)

if __name__ == "__main__":
    main()