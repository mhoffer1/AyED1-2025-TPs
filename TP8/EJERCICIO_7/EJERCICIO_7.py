"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
inexistentes."""

def eliminar_numeros_del_conjunto():
    conjunto_numeros = set(range(10))
    print("Conjunto inicial:", conjunto_numeros)
    
    while True:
        try:
            valor = int(input("Ingrese un numero entre 0 y 9 para eliminar (-1 para finalizar): "))
            if valor == -1:
                print("Proceso finalizado.")
                break
            conjunto_numeros.remove(valor)
            print("Conjunto despues de la eliminacion:", conjunto_numeros)
        except ValueError:
            print("Por favor, ingrese un numero entero valido.")
        except KeyError:
            print(f"El numero {valor} no esta en el conjunto.")

if __name__ == "__main__":
    eliminar_numeros_del_conjunto()