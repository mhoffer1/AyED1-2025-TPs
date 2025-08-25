from EJERCICIO_3 import calcular_gasto_subte

def test_calcular_gasto_subte():
    assert calcular_gasto_subte(10, 1000) == 10000.0
    assert calcular_gasto_subte(25, 1000) == 24000.0
    assert calcular_gasto_subte(35, 1000) == 31500.0
    assert calcular_gasto_subte(50, 1000) == 41000.0

    print("Todos los tests pasaron correctamente.")

if __name__ == "__main__":
    test_calcular_gasto_subte()