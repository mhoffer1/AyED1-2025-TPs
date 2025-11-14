""" Escribir una función que reciba como parámetro una tupla conteniendo una fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos, los que serán interpretados según un año de corte definido dentro del 
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado."""

def fecha_en_formato_extendido(fecha, anio_corte=30):
    dia, mes, anio = fecha
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    if anio < 100:
        if anio > anio_corte:
            anio += 1900
        else:
            anio += 2000

    nombre_mes = meses[mes - 1]
    return f"{dia} de {nombre_mes} de {anio}"

if __name__ == "__main__":
    fecha = (12, 10, 30)
    print(fecha_en_formato_extendido(fecha))

    fecha = (25, 12, 31)
    print(fecha_en_formato_extendido(fecha))

    fecha = (5, 3, 2025)
    print(fecha_en_formato_extendido(fecha))