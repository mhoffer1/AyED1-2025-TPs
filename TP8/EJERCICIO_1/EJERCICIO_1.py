"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho
rarios, y luego escribir un programa que las vincule:
 a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
 b. Sumar N días a una fecha.
 c. Ingresar un horario desde teclado, verificando que sea correcto.
 d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas."""

def es_fecha_valida(fecha):
    dia, mes, anio = fecha
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return dia <= 29
        else:
            return dia <= 28
    return False

def sumar_dias(fecha, n):
    dia, mes, anio = fecha
    dias_en_mes = [31, 28 + (1 if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dia += n
    while dia > dias_en_mes[mes - 1]:
        dia -= dias_en_mes[mes - 1]
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
            dias_en_mes[1] = 28 + (1 if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 0)
    return (dia, mes, anio)

def es_horario_valido(horario):
    horas, minutos = horario
    return 0 <= horas < 24 and 0 <= minutos < 60

def diferencia_horarios(horario1, horario2):
    horas1, minutos1 = horario1
    horas2, minutos2 = horario2

    total_minutos1 = horas1 * 60 + minutos1
    total_minutos2 = horas2 * 60 + minutos2

    if total_minutos1 > total_minutos2:
        total_minutos2 += 24 * 60

    diferencia = total_minutos2 - total_minutos1
    horas_diferencia = diferencia // 60
    minutos_diferencia = diferencia % 60

    return (horas_diferencia, minutos_diferencia)

if __name__ == "__main__":
    fecha = (29, 2, 2020)
    print(f"Fecha {fecha} valida: {es_fecha_valida(fecha)}")
    nueva_fecha = sumar_dias(fecha, 3)
    print(f"Suma de 3 días a {fecha}: {nueva_fecha}")

    horario = (14, 30)
    print(f"Horario {horario} valido: {es_horario_valido(horario)}")
    horario1 = (23, 45)
    horario2 = (1, 15)
    diferencia = diferencia_horarios(horario1, horario2)
    print(f"Diferencia entre horarios {horario1} y {horario2}: {diferencia} horas y minutos")