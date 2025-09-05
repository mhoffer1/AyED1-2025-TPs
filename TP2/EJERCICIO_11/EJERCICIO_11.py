"""11. Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
    
    a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
    los pacientes atendidos por turno en el orden que llegaron a la clínica.
    
    b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
    atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
    que se ingrese -1 como número de afiliado.
"""

def atender_pacientes() -> tuple[list[int], list[int]]:
    """
    Atiende a los pacientes de la clinica.
    returns: tuple con dos listas, una con los pacientes atendidos por urgencia
    y otra con los pacientes atendidos por turno.
    """
    urgencias = []
    turnos = []
    while True:
        numero_afiliado = int(input("Ingrese el numero de afiliado (4 digitos) o -1 para finalizar: "))
        if numero_afiliado == -1:
            break
        if numero_afiliado < 1000 or numero_afiliado > 9999:
            print("Numero de afiliado invalido. Debe ser un numero entero de 4 digitos.")
            continue
        tipo_atencion = int(input("Ingrese 0 si es por urgencia o 1 si es con turno: "))
        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        elif tipo_atencion == 1:
            turnos.append(numero_afiliado)
        else:
            print("Tipo de atencion invalido. Debe ser 0 o 1.")
    return urgencias, turnos

def buscar_afiliado(urgencias:list[int], turnos:list[int]) -> None:
    """
    Busca un numero de afiliado e informa cuantas veces fue atendido por turno
    y cuantas por urgencia.
    args: urgencias list, turnos list
    returns: None
    """
    while True:
        numero_afiliado = int(input("Ingrese el numero de afiliado a buscar o -1 para finalizar: "))
        if numero_afiliado == -1:
            break
        atenciones_urgencia = urgencias.count(numero_afiliado)
        atenciones_turno = turnos.count(numero_afiliado)
        print(f"El afiliado {numero_afiliado} fue atendido {atenciones_urgencia} veces por urgencia y {atenciones_turno} veces con turno.")
def main():
    urgencias, turnos = atender_pacientes()
    print(f"Pacientes atendidos por urgencia: {urgencias}")
    print(f"Pacientes atendidos con turno: {turnos}")
    buscar_afiliado(urgencias, turnos)

if __name__ == "__main__":
    main()