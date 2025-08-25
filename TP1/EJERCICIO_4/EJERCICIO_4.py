"""4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10."""

def calcular_cambio(total_compra: float, dinero_recibido: float) -> dict:
    """
    Calcula el cambio que se debe devolver al cliente.

    args:
    - total_compra: El total de la compra.
    - dinero_recibido: El dinero recibido por el cliente.

    returns:
    - Un diccionario con la cantidad de billetes de cada denominación que se deben devolver como cambio.
    """
    if dinero_recibido < total_compra:
        return {"error": "Dinero recibido insuficiente"}
    
    vuelto = dinero_recibido - total_compra
    if vuelto == 0:
        return {"mensaje": "No hay vuelto"}

    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]
    billetes = {}

    for denom in denominaciones:
        if vuelto >= denom:
            cantidad, vuelto = divmod(vuelto, denom)
            if cantidad > 0:
                billetes[f"{denom}"] = int(cantidad)

    # si no se puede entregar el cambio exacto
    if vuelto > 0:
        return {"error": f"No se puede entregar el cambio exacto. Sobran ${vuelto}"}

    return billetes

def mostrar_cambio(total_compra: float, dinero_recibido: float):
    """
    Muestra el cambio que se debe devolver al cliente.
    args:
    - total_compra: El total de la compra.
    - dinero_recibido: El dinero recibido por el cliente.
    """

    resultado = calcular_cambio(total_compra, dinero_recibido)

    print(f"Total de la compra: ${total_compra}")
    print(f"Dinero recibido: ${dinero_recibido}")
    print(f"Vuelto a entregar: ${dinero_recibido - total_compra}")

    if "error" in resultado:
        print(resultado["error"])
    elif "mensaje" in resultado:
        print(resultado["mensaje"])
    else:
        print("El cambio a entregar es:")
        for denom, cantidad in resultado.items():
            print(f"{cantidad} billete(s) de ${denom}")

def main():
    
    intentos = 0

    while intentos < 3:
        total_compra = float(input("Ingrese el total de la compra: $"))
        dinero_recibido = float(input("Ingrese el dinero recibido: $"))

        if total_compra < 0 or dinero_recibido < 0:
            print("Error: Los valores ingresados deben ser positivos.")
            intentos += 1
            continue

        if dinero_recibido < total_compra:
            print("Error: El dinero recibido no puede ser menor al total de la compra.")
            intentos += 1
            continue
    

        mostrar_cambio(total_compra, dinero_recibido)
        return
    else:
        print("Se han agotado los intentos.")
        
if __name__ == "__main__":
    main()
