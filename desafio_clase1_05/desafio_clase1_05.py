'''Imprima  n  números de la sucesión de Fibonacci.'''

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n>2:
        return fibo(n-1)+fibo(n-2)

cantidadFibo = 20

for i in range(1,cantidadFibo):
    print(fibo(i),end=", ")
print(fibo(20))