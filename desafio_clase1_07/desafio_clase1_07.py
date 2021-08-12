'''
* Escribir una función que calcule la cantidad de fichas para un juego de dominó completo con fichas que contienen hasta el número  n. 
Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2. ¡Observar que en el dominó hay fichas con valor 0!

*  Escribir una función que muestre todas las fichas para un juego de dominó como el anterior, en cualquier orden.
   mostrarFichas(3)

*  Escribir una función que, dada una cantidad de fichas, calcule cuál es el  n  (valor máximo) de las fichas. 
Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar -1.
'''

def cantidadFichas(n):
    contador = 0
    for i in range (0,n+1):
        for j in range(i,n+1):
            contador += 1
    return contador

def mostrarFichas(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            print(i," - ",j)

def factorial(n):
    if n==0:
        return 1
    else: 
        return n*factorial(n-1)

def variacionDeTomados(n,x):
    if n<x :
        return -1
    elif n==x: 
        return 1        
    else: 
        return int((factorial(n+x-1)/(factorial(x)*factorial(n-1))))

def valorMaximoDeFicha(cantidadDeFichas):
    valorMaximo = 0
    encontrado = False

    variacion = variacionDeTomados(valorMaximo,2)
    while ( variacion < cantidadDeFichas):
        valorMaximo += 1
        variacion = variacionDeTomados(valorMaximo,2)

    if (variacion == cantidadDeFichas):
        return valorMaximo-1
    else:
        return 0

for i in range(10,16):
    print("Para ",i," fichas => ", valorMaximoDeFicha(i))