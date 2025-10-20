"""
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
 Cadena:
 Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
 Sub-cadena: UADE
 Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
 Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

def contar_subcadena_no_consecutiva(cadena, subcadena):
    """
    Cuenta cuantas veces aparece una subcadena no consecutiva en una cadena.

    Args:
        cadena (str): La cadena principal donde buscar.
        subcadena (str): La subcadena a encontrar.

    Returns:
        int: El numero de veces que la subcadena se encuentra en la cadena.
    """
    cadena_lower = cadena.lower()
    subcadena_lower = subcadena.lower()
    
    len_cadena = len(cadena_lower)
    len_subcadena = len(subcadena_lower)

    def buscar(idx_cadena, idx_subcadena):
        if idx_subcadena == len_subcadena:
            return 1
        
        if idx_cadena == len_cadena:
            return 0

        total = 0
        char_a_buscar = subcadena_lower[idx_subcadena]

        for i in range(idx_cadena, len_cadena):
            if cadena_lower[i] == char_a_buscar:
                total += buscar(i + 1, idx_subcadena + 1)
        
        return total

    return buscar(0, 0)

def main():

    cadena_principal = input("Ingrese la cadena principal: ")
    subcadena_a_buscar = input("Ingrese la subcadena a buscar: ")

    cantidad = contar_subcadena_no_consecutiva(cadena_principal, subcadena_a_buscar)

    print(f"\nCadena: {cadena_principal}")
    print(f"Sub-cadena: {subcadena_a_buscar}")
    print(f"Cantidad encontrada: {cantidad}")

if __name__ == "__main__":
    main()
