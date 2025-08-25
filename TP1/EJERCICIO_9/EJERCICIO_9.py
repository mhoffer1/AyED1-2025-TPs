"""9. Resolver el siguiente problema utilizando funciones:

    Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.

    Además, se desea saber cuántos camiones se necesitan para transportar la cose
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo.
"""

from random import randint

CAPACIDAD_CAMION_G = 500_000      # 500 kg en gramos
UMBRAL_OCUPACION_G = int(0.8 * CAPACIDAD_CAMION_G)  # 400 kg en gramos

def simular_peso_naranjas(cantidad: int) -> list[int]:
    """Simula pesos enteros entre 150 y 350 g."""
    pesos = []

    for _ in range(cantidad):
        pesos.append(randint(150, 350))

    return pesos

def clasificar_naranjas(pesos: list[int]) -> dict:
    """
    Clasifica naranjas en aptas (200–300 g) y para jugo (resto).
    También calcula cajones llenos y sobrantes aptas.
    """
    aptas = []
    for p in pesos:
        if 200 <= p <= 300:
            aptas.append(p)
    
    jugo = len(pesos) - len(aptas)

    cajones_llenos = len(aptas) // 100
    sobrantes_aptas = len(aptas) % 100

    return {
        "aptas": aptas,                      # lista de pesos aptos
        "jugo": jugo,                        # cantidad para jugo
        "cajones": cajones_llenos,           # cajones completos (100 c/u)
        "sobrantes": sobrantes_aptas         # naranjas aptas que no completan cajon
    }

def calcular_camiones_para_cajones(pesos_aptos: list[int], cajones_llenos: int) -> tuple[int, int]:
    """
    Calcula camiones a despachar y el peso sobrante para el próximo reparto,
    respetando capacidad 500 kg y ocupación mínima 80%.
    Solo se considera el peso de naranjas que entran en cajones completos.
    Retorna (camiones, sobrante_en_gramos_para_proximo_reparto).
    """
    n_aptas_a_despachar = cajones_llenos * 100
    pesos_a_despachar = pesos_aptos[:n_aptas_a_despachar]  # cualquier 100*k sirven
    peso_total_g = sum(pesos_a_despachar)

    camiones_completos = peso_total_g // CAPACIDAD_CAMION_G
    resto_g = peso_total_g % CAPACIDAD_CAMION_G

    if resto_g >= UMBRAL_OCUPACION_G:
        # Se despacha un camión adicional por encima del 80%
        return camiones_completos + 1, 0
    else:
        # Ese remanente no se despacha; queda para el próximo reparto
        return camiones_completos, resto_g

def calcular_cajones_y_camiones(cantidad_naranjas: int) -> dict:
    pesos = simular_peso_naranjas(cantidad_naranjas)
    clasif = clasificar_naranjas(pesos)

    camiones, sobrante_camion_g = calcular_camiones_para_cajones(
        clasif["aptas"], clasif["cajones"]
    )

    return {
        "cajones": clasif["cajones"],
        "jugo": clasif["jugo"],
        "sobrantes_aptas": clasif["sobrantes"], # naranjas aptas sin cajón
        "camiones_a_despachar": camiones,
        "peso_sobrante_camion_g": sobrante_camion_g
    }

def main():
    cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    r = calcular_cajones_y_camiones(cantidad)

    print("\nResultados:")
    print(f"Cajones llenos: {r['cajones']}")
    print(f"Naranjas para jugo: {r['jugo']}")
    print(f"Naranjas aptas sobrantes (sin completar cajón): {r['sobrantes_aptas']}")
    print(f"Camiones a despachar (>=80% ocupación): {r['camiones_a_despachar']}")
    if r["peso_sobrante_camion_g"] > 0:
        kg = r["peso_sobrante_camion_g"] / 1000
        print(f"Peso sobrante para próximo reparto (no despachado por <80%): {kg:.2f} kg")

if __name__ == "__main__":
    main()
