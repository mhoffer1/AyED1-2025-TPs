"""3. Una persona desea llevar el control de los gastos realizados al viajar en el 
subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de 
tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que 
reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total 
gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

| Cantidad de viajes | Valor del pasaje |
|-------------------|------------------|
| 1 a 20 | Averiguar en Internet el valor actualizado |
| 21 a 30 | 20% de descuento sobre tarifa máxima |
| 31 a 40 | 30% de descuento sobre tarifa máxima |
| Más de 40 | 40% de descuento sobre tarifa máxima |
"""

def calcular_gasto_subte(cantidad_viajes: int, precio_base: float) -> float:
    """
    Calcula el gasto total en viajes de subte.
    - cantidad_viajes: cantidad de viajes realizados
    - precio_base: precio base del viaje
    - retorna: gasto total
    """
    if cantidad_viajes < 1:
        return 0

    if cantidad_viajes <= 20:
        return cantidad_viajes * precio_base
    else:
        # primeros 20 viajes
        gasto_total = 20 * precio_base
        viajes_restantes = cantidad_viajes - 20

        # viaje 21 al 30 con 20% de descuento
        if viajes_restantes <= 10:
            gasto_total += viajes_restantes * precio_base * 0.8
        else:
            gasto_total += 10 * precio_base * 0.8
            viajes_restantes -= 10

            # viaje 31 al 40 con 30% de descuento
            if viajes_restantes <= 10:
                gasto_total += viajes_restantes * precio_base * 0.7
            else:
                gasto_total += 10 * precio_base * 0.7
                viajes_restantes -= 10

                # viaje 41 en adelante con 40% de descuento
                gasto_total += viajes_restantes * precio_base * 0.6

        return gasto_total

def main():

    precio = float(input("Ingrese el precio base del viaje en subte: "))
    viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))

    gasto_total = calcular_gasto_subte(viajes, precio)
    print(f"El gasto total en subte es: {gasto_total}")