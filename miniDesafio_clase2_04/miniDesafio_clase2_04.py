'''Realizar un programa que ordena nombres alfabéticamente. 
1) Primero debe pedir al usuario que ingrese un número: la cantidad de nombres que serán ingresados. 
2) Luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada. Los nombres se deben ir agregando a una lista. 
3) Por último, ordenar la lista alfabéticamente 
4) y mostrar en pantalla de a uno por vez los nombres ordenados (usando un for).'''

cantidadNombres = int(input("Cantidad de nombres: "))

lNombres = []
for i in range(0,cantidadNombres):
    nombre = input("Nombre: ")
    lNombres.append(nombre)

lNombres.sort()

for unNombre in lNombres:
    print(unNombre)