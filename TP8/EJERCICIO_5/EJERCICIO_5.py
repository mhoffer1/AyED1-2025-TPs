""" En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par orde
nado de números reales (x, y) llamados componentes. Para representarlos basta 
con unir el origen de coordenadas con el punto indicado en sus componentes:

Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 

A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
 Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor 
de verdad indicando si son ortogonales o no. Desarrollar también un programa que 
permita verificar el comportamiento de la función. """

def son_ortogonales(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    producto_escalar = x1 * x2 + y1 * y2
    return producto_escalar == 0

if __name__ == "__main__":
    vec1 = (2, 3)
    vec2 = (-3, 2)
    if son_ortogonales(vec1, vec2):
        print(f"Los vectores {vec1} y {vec2} son ortogonales.")
    else:
        print(f"Los vectores {vec1} y {vec2} no son ortogonales.")

    vec3 = (1, 2)
    vec4 = (2, 3)
    if son_ortogonales(vec3, vec4):
        print(f"Los vectores {vec3} y {vec4} son ortogonales.")
    else:
        print(f"Los vectores {vec3} y {vec4} no son ortogonales.")