"""
a) Escribir una funcion llamada map_, que reciba una función y una lista y devuelva 
la lista que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.

b) Escribir una función llamada filter_, que reciba una función y una lista. 
Debe devolver una lista con los elementos, de la lista recibida, para los cuales 
la función recibida devuelve un valor verdadero.
"""

lista = [x for x in range(25)]

print(lista)

mapped_list = list(map(lambda x: x*2, lista))
filtered = [x for x in mapped_list if not x%3]
print(filtered) 
print(mapped_list)
print(list(filter(lambda x: x%3 == 0, mapped_list)))

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']

print(list(map(lambda x: x, lista)))