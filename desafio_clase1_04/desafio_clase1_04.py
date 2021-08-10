'''Escribir una función que recibe un número y devuelve True si el número es primo y False en caso contrario.

Mediante un for verificar la primalidad de los numeros del  1  al  20 , es decir, decidir si cada número es primo o no.

Tips:
Un número  N  es primo cuando tiene exactamente  2  divisores ( 1  y  N ).
Sin embargo, alcanza con verificar que no es múltiplo de ningún número entre  2  y  N−−√  (recordar que  N−−√=N0.5 )
El numero 1 NO es primo.'''

def esPrimo(n):
    if (n==1):
        return False
    limiteSuperior = round(n**(1/2))
    cantidadDivisores = 1
    for i in range(1,limiteSuperior+1):
        if (n%i==0):
            cantidadDivisores +=1
    
    if cantidadDivisores == 2:
        return True
    else:
        return False

for j in range(1,21):
    if (esPrimo(j)==True):
        msj = " es primo"
    else: 
        msj = " NO es primo"
    print(j, msj)
