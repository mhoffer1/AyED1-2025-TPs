"""Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función."""

def validar_fechas(dia :int, mes: int, anio: int) -> bool:
    """
    Valida una fecha.
    - recibe: dia, mes y año como enteros
    - retorna: True si la fecha es valida, False en caso contrario
    """
    if anio < 0 or mes < 1 or mes > 12 or dia < 1:
        return False
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar si es año bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_por_mes[1] = 29
    
    if dia > dias_por_mes[mes - 1]:
        return False
    
    return True

def main():

    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if validar_fechas(dia, mes, anio):
        print("La fecha es valida")
    else:
        print("La fecha no es valida")

if __name__ == "__main__":
    main()

