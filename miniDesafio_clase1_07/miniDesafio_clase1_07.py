'''Escribir una función que chequee los siguientes usuarios y contraseñas:
Usuario: Juan
Contraseña: 12345_
Usuario: Pablo
Contraseña: xDcFvGbHn
La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.'''


def chequeoContrasenia(usuario,contrasenia):
    if (usuario == "Juan" and contrasenia=="12345_") or (usuario=="Pablo" and contrasenia=="xDcFvGbHn"):
        return True
    else:
        return False

usuario = input("Usuario: ")
contrasenia = input("Contrasenia: ")

if (chequeoContrasenia(usuario,contrasenia)):
    print("Ingreso correctamente :) ")
else:
    print("No ingreso correctamente :( ")