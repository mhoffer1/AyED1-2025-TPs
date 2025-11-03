"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.
"""


def obtener_nombre_mes(numero_mes: int) -> str:
    """Devuelve el nombre del mes correspondiente al numero recibido.

    Args:
        numero_mes (int): Numero del mes (1-12).

    Raises:
        ValueError: Si el numero del mes es invalido.
    Returns:
        str: Nombre del mes o cadena vacia si es invalido.
    """ 
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    try:
        if numero_mes < 1 or numero_mes > 12:
            raise ValueError("Numero de mes invalido. Debe estar entre 1 y 12.")
        return meses[numero_mes - 1]
    except ValueError as e:
        print(f"Error: {e}")
        return ""
    

def main():
    try:
        entrada = input("Ingrese el numero del mes (1-12): ")
        numero_mes = int(entrada)
        nombre_mes = obtener_nombre_mes(numero_mes)
        if nombre_mes:
            print(f"El nombre del mes es: {nombre_mes}")
        else:
            print("No se pudo obtener el nombre del mes debido a un numero invalido.")
    except ValueError:
        print("Error: La entrada debe ser un numero entero.")


if __name__ == "__main__":
    main()