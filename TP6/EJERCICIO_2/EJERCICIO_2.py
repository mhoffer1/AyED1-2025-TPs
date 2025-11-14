""" Escribir un programa que permita dividir un archivo de texto cualquiera en partes 
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se 
ingresa por teclado. Los nombres de los archivos generados deben respetar el 
nombre original con el agregado de un sufijo que indique de qué parte se trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria"""

def dividir_archivo(nombre_archivo, tamano_parte):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as a:
            parte_numero = 1
            parte_actual = ''
            for linea in a:
                if len(parte_actual) + len(linea) > tamano_parte:
                    if parte_actual:
                        with open(f"{nombre_archivo}_parte{parte_numero}.txt", 'w', encoding='utf-8') as parte_archivo:
                            parte_archivo.write(parte_actual)
                        parte_numero += 1
                        parte_actual = ''
                parte_actual += linea
            if parte_actual:
                with open(f"{nombre_archivo}_parte{parte_numero}.txt", 'w', encoding='utf-8') as parte_archivo:
                    parte_archivo.write(parte_actual)
        print("Archivo dividido coorrectamente.")
    except Exception as e:
        print(f"Error al dividir el archivo: {e}")

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo a dividir: ")
    tamano_parte = int(input("Ingrese el tamaño maximo de cada parte (en caracteres): "))
    dividir_archivo(nombre_archivo, tamano_parte)