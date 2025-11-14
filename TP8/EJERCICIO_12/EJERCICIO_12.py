"""Una librería almacena su lista de precios en un diccionario. Diseñar un programa 
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un 
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio."""

def actualizar_precios_cuadernos(lista_precios):
    for item in lista_precios:
        if 'cuaderno' in item.lower():
            lista_precios[item] *= 1.15
    return lista_precios

if __name__ == "__main__":
    lista_precios = {
        'Cuaderno A4': 200.0,
        'Lápiz': 50.0,
        'Cuaderno de dibujo': 300.0,
        'Borrador': 30.0,
        'Mochila': 1500.0
    }
    
    lista_precios = actualizar_precios_cuadernos(lista_precios)
    
    print("Listado de precios actualizado:")
    for item, precio in lista_precios.items():
        print(f"{item}: ${precio:.2f}")
    
    item_mas_costoso = max(lista_precios, key=lista_precios.get)
    print(f"\nEl item mas costoso es '{item_mas_costoso}' con un precio de ${lista_precios[item_mas_costoso]:.2f}")