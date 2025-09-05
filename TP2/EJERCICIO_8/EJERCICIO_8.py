"""8. Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200."""

lista = [x for x in range(100, 201) if x % 2 != 0]
print(lista)
