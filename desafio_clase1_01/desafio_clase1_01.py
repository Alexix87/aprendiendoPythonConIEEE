'''Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

Si el número es par, se debe dividir por  2 .
Si el número es impar, se debe multiplicar por  3  y sumar  1 .
Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.'''

def lothar(n):
    if (n == 1):
        return 0

    if (n%2 == 0):
        return 1 + lothar(n/2)
    else:
        return 1 + lothar((n*3)+1)

valor = int(input("Valor: "))
print("El lothar de ", valor, " es: ",lothar(valor))