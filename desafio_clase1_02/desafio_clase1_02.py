'''
1) Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
2) Reescribir la función anterior modificándola para asignar una importancia
    al primer examen de 20%, 
    al segundo de 50% y 
    al tercero de 30%.
Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, 
si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).'''


def promedio(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3

def promedioPonderado(nota1,nota2,nota3):
    return (nota1*0.2 + nota2*0.5 + nota3*0.3)/3


print("El promedio de las notas: 8,6,7 es: ", promedio(8,6,7))
print("El promedio ponderado de: 8,6,7 es: ", promedioPonderado(10,10,10))