"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto. Ejemplo:
 Arslanian, Gustavo–> ARMENIA.TXT
 Rossini, Giuseppe–> ITALIA.TXT
 Pérez, Juan
 Smith, John–> ESPAÑA.TXT–> descartar
 El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor. """

def separar_apellidos():
    try:
        with open("apellidos.txt", "r", encoding="utf-8") as a:
            armenia = open("ARMENIA.TXT", "w", encoding="utf-8")
            italia = open("ITALIA.TXT", "w", encoding="utf-8")
            espana = open("ESPAÑA.TXT", "w", encoding="utf-8")

            for linea in a:
                apellido_nombre = linea.strip()
                if apellido_nombre.endswith("IAN"):
                    armenia.write(apellido_nombre + "\n")
                elif apellido_nombre.endswith("INI"):
                    italia.write(apellido_nombre + "\n")
                elif apellido_nombre.endswith("EZ"):
                    espana.write(apellido_nombre + "\n")

            armenia.close()
            italia.close()
            espana.close()

    except FileNotFoundError:
        print("El archivo 'apellidos.txt' no fue encontrado.")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    separar_apellidos()
