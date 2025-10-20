import re

"""
Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo 
usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar.  
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos
trar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""

def validar_y_extraer_dominio(email):
    """
    Valida un email usando una expresion regular y extrae el dominio si es valido.
    args:
        email (str): Direccion de correo electrónico a validar.
    """
    patron = r"^[a-zA-Z0-9]+@(.+\.com(\.ar)?)$"
    
    coincidencia = re.match(patron, email, re.IGNORECASE)
    
    if coincidencia:
        return coincidencia.group(1)
    return None

def main():
    """Funcion principal del programa."""
    dominios_unicos = set()

    while True:
        email_ingresado = input("Ingrese una direccion de correo (o presione Enter para finalizar): ")
        
        if not email_ingresado:
            break
            
        dominio = validar_y_extraer_dominio(email_ingresado)
        
        if dominio:
            print(f"'{email_ingresado}' es una direccion valida.")
            dominios_unicos.add(dominio.lower())
        else:
            print(f"'{email_ingresado}' no es una direccion valida.")

    if dominios_unicos:
        print("\n--- Dominios Validos (sin repetir y ordenados) ---")
        for dominio in sorted(list(dominios_unicos)):
            print(dominio)
    else:
        print("\nNo se ingresaron dominios validos.")

if __name__ == "__main__":
    main()