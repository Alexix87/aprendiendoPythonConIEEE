''' Mini-desafío: Listas
1) Crear una lista con los números pares menores a 50 ¿Hay diferentes formas de lograr esto?

2) Crear un programa en el cual el usuario ingresa un string y dos índices numéricos. 
El programa debe crear una lista a partir de las letras del string, 
luego intercambiar dos letras de lugar a partir de los índices indicados por el usuario. 
Por último debe combinar las letras de la lista nuevamente en un string e imprimir el resultado. 
Si los índices son inválidos mostrar un mensaje de error.'''

# 1)
x = [2*i for i in range(1,25)]

# 2)

def indicesInvalidos(indiceMenor,indiceMayor,tamanioDeCadena):
    if (indiceMayor < indiceMenor) or (indiceMenor < 0) or (indiceMayor+1 > tamanioDeCadena ): 
        return True
    else:
        return False

sCadena = input("string: ")
indiceMenor = int(input("IndiceMenor: "))
indiceMayor = int(input("IndiceMayor: "))
while (indicesInvalidos(indiceMenor,indiceMayor,len(sCadena))):
    print("Indices invalidos, ingrese nuevamente los indices")
    indiceMenor = int(input("IndiceMenor: "))
    indiceMayor = int(input("IndiceMayor: "))

lCadena = list(sCadena)
lCadena[indiceMenor],lCadena[indiceMayor] = lCadena[indiceMayor],lCadena[indiceMenor]
sCadena = "".join(lCadena)
print(sCadena)