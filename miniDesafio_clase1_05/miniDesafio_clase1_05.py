'''Implementar un programa que muestre la siguiente secuencia:

1, 2, 3, 4, 5, 4, 3, 2, 1, 0 '''

i = 1
j = 4
contador = 10

while (contador>1):
    if(contador>5):
        print (i,end=", ")
        i+=1
    else:
        print(j,end=", ")
        j-=1
    contador -= 1
print(j)