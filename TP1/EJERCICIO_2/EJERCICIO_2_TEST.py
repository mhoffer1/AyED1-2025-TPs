from EJERCICIO_2 import validar_fechas

def test_fechas_validas():
    assert validar_fechas(15, 6, 2023) == True
    assert validar_fechas(29, 2, 2024) == True
    assert validar_fechas(31, 12, 2023) == True
    assert validar_fechas(1, 1, 2000) == True

    print("Todas las fechas validas han pasado las pruebas.")

def test_fechas_invalidas():
    assert validar_fechas(32, 1, 2023) == False
    assert validar_fechas(29, 2, 2023) == False
    assert validar_fechas(31, 4, 2023) == False
    assert validar_fechas(0, 6, 2023) == False

    print("Todas las fechas invalidas pasaron las pruebas.")

if __name__ == "__main__":
    test_fechas_validas()
    test_fechas_invalidas()
    