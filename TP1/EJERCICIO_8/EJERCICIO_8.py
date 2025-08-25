"""8. La siguiente función permite averiguar el día de la semana para una fecha determinada. 
La fecha se suministra en forma de tres parámetros enteros y la función de vuelve 0 para domingo, 
1 para lunes, 2 para martes, etc. Escribir un programa para  imprimir por pantalla el calendario de un mes completo, 
correspondiente a un mes y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.

def diadelasemana(dia, mes, anio): 
    if mes < 3: 
        mes = mes + 10 
        anio = anio - 1 
    else: 
        mes = mes - 2 
    siglo = anio // 100 
    anio2 = anio % 100 
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7 
    if diasem < 0: 
        diasem = diasem + 7 
    return diasem
"""

def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """
    Devuelve el día de la semana para una fecha dada.
    - recibe: dia (int), mes (int), anio (int)
    - retorna: día de la semana (int)
    """
    if mes < 3: 
        mes = mes + 10 
        anio = anio - 1 
    else: 
        mes = mes - 2 
    siglo = anio // 100 
    anio2 = anio % 100 
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7 
    if diasem < 0: 
        diasem = diasem + 7 
    return diasem

def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.
    - recibe: anio (int)
    - retorna: True si es bisiesto, False en caso contrario
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días en un mes determinado.
    - recibe: mes (int), anio (int)
    - retorna: cantidad de días (int)
    """

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28

def nombre_mes(mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente.
    - recibe: mes (int)
    - retorna: nombre del mes (str)
    """
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if 1 <= mes <= 12:
        return meses[mes - 1]
    return "Mes inválido"

def imprimir_calendario(mes: int, anio: int):

    """
    Imprime el calendario de un mes y año determinados.
    - recibe: mes (int), anio (int)
    """

    primer_dia = diadelasemana(1, mes, anio)

    dia_del_mes = dias_en_mes(mes, anio)

    titulo = f"{nombre_mes(mes)} {anio}"
    print(f"\n{titulo}")
    print("=" * len(titulo))
    print("Dom Lun Mar Mie Jue Vie Sab")
    print("-" * 28)

    for i in range(primer_dia):
        print("   ", end=" ")

    for dia in range(1, dia_del_mes + 1):
        print(f"{dia:2d} ", end=" ")
        
        if (dia + primer_dia - 1) % 7 == 6:
            print()
    
    if (primer_dia + dia_del_mes - 1) % 7 != 6:
        print()
    
    print()

def main():

    # Solicitar mes y año al usuario
    mes = int(input("\nIngrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))
    
    # Validar entrada
    if mes < 1 or mes > 12:
        print("Error: El mes debe estar entre 1 y 12")
        return
    
    if año < 1:
        print("Error: El año debe ser positivo")
        return
    
    # Imprimir el calendario
    imprimir_calendario(mes, año)

if __name__ == "__main__":
    main()