"""Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
que incluya las siguientes funciones:
 GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
 <Deporte 1>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 <Deporte 2>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
promedio deben grabarse en líneas diferentes. Ejemplo:
 <Deporte 1>
 <Promedio de alturas deporte 1>
 <Deporte 2>
 <Promedio de alturas deporte 2>
 < . . . >
 MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo."""

def grabar_rango_alturas():
    with open("alturas.txt", "w") as a:
        while True:
            deporte = input("Ingrese el nombre del deporte (o 'fin' para terminar): ")
            if deporte.lower() == 'fin':
                break
            a.write(deporte + "\n")
            while True:
                altura = input("Ingrese la altura del atleta en cm (o 'fin' para terminar este deporte): ")
                if altura.lower() == 'fin':
                    break
                a.write(altura + "\n")

def grabar_promedio():
    with open("alturas.txt", "r") as archivo_lectura, open("promedios.txt", "w") as archivo_promedios:
        while True:
            deporte = archivo_lectura.readline().strip()
            if not deporte:
                break
            total_altura = 0
            contador = 0
            while True:
                linea = archivo_lectura.readline().strip()
                if not linea or not linea.isdigit():
                    break
                total_altura += int(linea)
                contador += 1
            promedio = total_altura / contador if contador > 0 else 0
            archivo_promedios.write(deporte + "\n")
            archivo_promedios.write(f"{promedio}\n")

def mostrar_mas_altos():
    total_general = 0
    contador_general = 0
    promedios_disciplina = {}

    with open("promedios.txt", "r") as archivo_promedios:
        while True:
            deporte = archivo_promedios.readline().strip()
            if not deporte:
                break
            promedio = float(archivo_promedios.readline().strip())
            promedios_disciplina[deporte] = promedio
            total_general += promedio
            contador_general += 1

    promedio_general = total_general / contador_general if contador_general > 0 else 0

    print(f"Promedio general de alturas: {promedio_general:.2f} cm")
    print("Disciplinas con promedios superiores al promedio general:")
    for deporte, promedio in promedios_disciplina.items():
        if promedio > promedio_general:
            print(f"{deporte}: {promedio:.2f} cm")

if __name__ == "__main__":
    grabar_rango_alturas()
    grabar_promedio()
    mostrar_mas_altos()