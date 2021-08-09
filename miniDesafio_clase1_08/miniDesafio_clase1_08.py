'''Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.
Ejemplos:
contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)
contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)'''

def contarDivisores(n):
    contador = 0
    for i in range(1,n+1):
        if (n%i == 0):
            contador += 1
    return contador

valor = int (input("Valor: "))
print (valor, " tiene ",contarDivisores(valor)," divisores.")