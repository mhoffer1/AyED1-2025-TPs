"""7. Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
"""

def intercalar_listas(a: list, b: list) -> list:

    for i in range(len(b)):
        a[2*i+1:2*i+1] = [b[i]]
    return a

def main():
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    intercalar_listas(lista1, lista2)
    print(lista1)

if __name__ == "__main__":
    main()
    