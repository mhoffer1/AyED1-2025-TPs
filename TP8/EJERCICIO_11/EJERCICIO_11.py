"""Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
resultados. Luego desarrollar un programa para leer una frase e invocar a la 
función por cada palabra que contenga la misma. Imprimir las palabras y la 
cantidad de vocales hallada."""

def contar_vocales(palabra):
    vocales = 'aeiouAEIOU'
    conteo = {v: 0 for v in vocales}
    
    for letra in palabra:
        if letra in vocales:
            conteo[letra] += 1
    
    conteo = {v: c for v, c in conteo.items() if c > 0}
    
    return conteo

if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    
    for palabra in palabras:
        resultado = contar_vocales(palabra)
        print(f"Palabra: '{palabra}' -> Vocales: {resultado}")
