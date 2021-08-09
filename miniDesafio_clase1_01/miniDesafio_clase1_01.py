'''Diseñar un programa en el cual se definan exactamente 2 variables.

La primera se debe llamar nombre y debe contener tu nombre (entre comillas).
La segunda se debe llamar edad y debe contener tu edad (como un número simple, sin comillas).
Por último el programa debe mostrar en pantalla la siguiente frase en una sóla línea:

(nombre) tiene (edad) años

Por ejemplo:
Mati tiene 5 años '''

nombre = input("Nombre: ")
edad = int(input("Edad: "))

print (nombre, " tiene ",edad, "años.")