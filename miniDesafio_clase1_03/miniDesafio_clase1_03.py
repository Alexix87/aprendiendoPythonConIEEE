'''Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F 
de acuerdo a la siguiente conversión:
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: 0–59'''

notaInt = int(input("Nota: "))
notaChar = 'X'

if(notaInt<60):
    notaChar = 'F'
elif(notaInt<70):
    notaChar = 'D'
elif(notaInt<80):
    notaChar = 'C'
elif(notaInt<90):
    notaChar = 'B'
elif(notaInt<=100):
    notaChar = 'A'
if(notaChar!='X'):
    print("La nota ",notaInt," se representa con una ", notaChar)
else:
    print("La nota está fuera de reango")