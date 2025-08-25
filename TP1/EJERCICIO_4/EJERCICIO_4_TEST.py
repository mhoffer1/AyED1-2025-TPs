from EJERCICIO_4 import calcular_cambio, mostrar_cambio

def test_calcular_cambio():
    assert calcular_cambio(3170, 5000) == {'1000': 1, '500': 1, '200': 1, '100': 1, '10': 3}
    assert calcular_cambio(1000, 1000) == {"mensaje": "No hay vuelto"}
    assert calcular_cambio(5000, 4000) == {"error": "Dinero recibido insuficiente"}
    assert calcular_cambio(100, 1000) == {'500': 1, '200': 2}

    print("Todos los tests de calcular_cambio pasaron.")
    
if __name__ == "__main__":
    test_calcular_cambio()