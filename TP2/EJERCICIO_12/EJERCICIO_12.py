"""12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
    
    a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
    aparecer una sola vez en el informe.
    
    b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
    ingresos. Mostrar los registros de entrada al club antes y después de
    eliminarlo. Informar cuántos ingresos se eliminaron."""


def cargar_socios():
    "funcion que carga los socios en una lista hasta ingresar un 0"
    socios = []
    while True:
        socio = int(input("Ingrese el numero de socio (5 digitos) o 0 para finalizar: "))
        if socio == 0:
            break
        elif 10000 <= socio <= 99999:
            socios.append(socio)
        else:
            print("Numero de socio invalido. Debe tener 5 digitos.")
    return socios

def contar_ingresos(socios: list) -> dict:
    "funcion que cuenta los ingresos de cada socio y devuelve un diccionario"
    ingresos = {}
    for socio in socios:
        if socio in ingresos:
            ingresos[socio] += 1
        else:
            ingresos[socio] = 1
    return ingresos

def eliminar_socio(socios, socio_a_eliminar):
    "funcion que elimina todos los ingresos de un socio y devuelve la cantidad eliminada"
    cantidad_eliminada = socios.count(socio_a_eliminar)
    socios = [socio for socio in socios if socio != socio_a_eliminar]
    return socios, cantidad_eliminada

def main():
    socios = cargar_socios()
    
    print("Registros de ingresos al club:")
    ingresos = contar_ingresos(socios)
    for socio, cantidad in ingresos.items():
        print(f"Socio {socio}: {cantidad} ingresos")
    
    socio_a_eliminar = int(input("Ingrese el numero de socio a eliminar: "))
    if socio_a_eliminar in ingresos:
        socios, cantidad_eliminada = eliminar_socio(socios, socio_a_eliminar)
        print(f"Se eliminaron {cantidad_eliminada} ingresos del socio {socio_a_eliminar}.")
        
        print("Registros de ingresos al club despues de eliminar:")
        ingresos = contar_ingresos(socios)
        for socio, cantidad in ingresos.items():
            print(f"Socio {socio}: {cantidad} ingresos")
    else:
        print(f"El socio {socio_a_eliminar} no se encuentra en los registros.")

if __name__ == "__main__":
    main()

