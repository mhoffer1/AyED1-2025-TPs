from EJERCICIO_1 import encontar_maximo

def test_casos_maximo_unico():

    assert encontar_maximo(1, 2, 3) == 3
    assert encontar_maximo(8, 2, 1) == 8
    assert encontar_maximo(1, 9, 1) == 9

    print("Todos los casos de maximo unico pasaron correctamente.")

def test_casos_sin_maximo_unico():

    assert encontar_maximo(1, 1, 1) == -1
    assert encontar_maximo(2, 2, 2) == -1
    assert encontar_maximo(3, 3, 3) == -1

    print("Todos los casos de maximo sin unico pasaron correctamente.")

if __name__ == "__main__":
    test_casos_maximo_unico()
    test_casos_sin_maximo_unico()
