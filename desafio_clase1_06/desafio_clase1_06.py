'''Ustedes pensarán en un número secreto (para este ejercicio consideremos que el número es menor a 10.000), 
luego el programa intenta adivinarlo. 
El usuario debe responder con el símbolo >, < ó =. 
En el caso de ser igual, el programa termina e imprime la cantidad de intentos que tardó, 
caso contrario, debe volver a intentar adivinar el número y se repite el procedimiento.'''

valorInicial = 1
valorFinal = 10000
contador = 0
opcion = 'x'
while(opcion != '='):
    contador += 1
    valorCentral = round((valorInicial + valorFinal)/2)
    print("valor = ", valorCentral, "? (>,<,=): ",end=" ")
    opcion = input()
    if (opcion == '<'):
        valorFinal = valorCentral-1
    else:
        valorInicial = valorCentral+1

print("La cantidad de intentos fue: ",contador)