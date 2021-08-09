'''Implementar un programa que reciba 2 números (A y B), 
y luego imprima en pantalla la secuencia de números enteros desde A hasta B. 
En el caso de que B sea menor que A, se debe repetir el pedido de B hasta que sea válido ( B  ≥  A ).'''

a = int (input("A: "))
b = int (input("B: "))

while (b<=a):
    a = int (input("A: "))
    b = int (input("B: "))

aux = a
print("Numeros:")
while (aux != b):
    print(aux,end=", " )
    aux+=1
print(aux)