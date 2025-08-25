""" 7. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el dia siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
 a. Sumar N dias a una fecha.
 b. Calcular la cantidad de dias existentes entre dos fechas cualesquiera."""

def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días en un mes dado de un año específico.
    - recibe: mes (int), anio (int)
    - retorna: cantidad de días en el mes (int)
    """
    if mes < 1 or mes > 12:
        return 0
    dias_en_mes = [31, 28 + es_bisiesto(anio), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Valida una fecha.
    - recibe: dia (int), mes (int), anio (int)
    - retorna: True si la fecha es válida, False en caso contrario
    """
    if anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, anio):
        return False
    return True

def diasiguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    Calcula el dia siguiente a una fecha dada.
    - recibe: dia (int), mes (int), anio (int)
    - retorna: una tupla con el dia siguiente (dia, mes, anio)
    """
    dia += 1
    if dia > dias_en_mes(mes, anio):
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1

    return dia, mes, anio

def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.
    - recibe: anio (int)
    - retorna: True si es bisiesto, False en caso contrario
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def sumar_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """
    Suma n dias a una fecha dada usando la función diasiguiente.
    recibe: dia (int), mes (int), anio (int), n (int)
    retorna: una tupla con la nueva fecha (dia, mes, anio)
    """
    for _ in range(n):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return dia, mes, anio

def dias_entre_fechas(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> int:
    """
    Calcula la cantidad de dias entre dos fechas cualesquiera.

    recibe: d1 (int), m1 (int), a1 (int), d2 (int), m2 (int), a2 (int)
    retorna: la cantidad de dias entre las dos fechas
    """
    if (a1, m1, d1) > (a2, m2, d2):
        d1, m1, a1, d2, m2, a2 = d2, m2, a2, d1, m1, a1

    contador = 0
    while (d1, m1, a1) != (d2, m2, a2):
        d1, m1, a1 = diasiguiente(d1, m1, a1)
        contador += 1
    return contador

def main():
    """
    Muestra el menu de opciones y llama a las funciones correspondientes.
    """
    opcion = 0

    while opcion != 3:
        print("Seleccione una opción:")
        print("1. Sumar dias a una fecha")
        print("2. Calcular dias entre fechas")
        print("3. Salir")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            if not validar_fecha(dia, mes, anio):
                print("Fecha invalida.")
                continue
            n = int(input("Ingrese la cantidad de dias a sumar: "))
            nueva_fecha = sumar_dias(dia, mes, anio, n)
            print(f"Nueva fecha: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")
        elif opcion == 2:
            d1 = int(input("Ingrese el dia de la primera fecha: "))
            m1 = int(input("Ingrese el mes de la primera fecha: "))
            a1 = int(input("Ingrese el año de la primera fecha: "))
            if not validar_fecha(d1, m1, a1):
                print("Fecha invalida.")
                continue
            d2 = int(input("Ingrese el dia de la segunda fecha: "))
            m2 = int(input("Ingrese el mes de la segunda fecha: "))
            a2 = int(input("Ingrese el año de la segunda fecha: "))
            if not validar_fecha(d2, m2, a2):
                print("Fecha invalida.")
                continue
            dias = dias_entre_fechas(d1, m1, a1, d2, m2, a2)
            print(f"dias entre fechas: {dias}")
        elif opcion == 3:
            print("Saliendo")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()
