""" Desarrollar un programa que utilice una función que reciba como parámetro una 
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía."""

def descomponer_email(email):
    partes = email.split('@')
    if len(partes) != 2:
        return ()
    usuario = partes[0]
    dominio_completo = partes[1]
    dominio_partes = dominio_completo.split('.')
    if len(dominio_partes) < 2:
        return ()
    return (usuario, *dominio_partes)

if __name__ == "__main__":
    email = "asd123@uade.edu.ar"
    partes = descomponer_email(email)
    if partes:
        print(f"Partes del email '{email}': {partes}")
    else:
        print(f"El email '{email}' es invalido.")