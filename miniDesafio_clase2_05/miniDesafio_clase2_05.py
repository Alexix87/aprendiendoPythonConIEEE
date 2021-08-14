'''Encontrar la cantidad de ocurrencias de la palabras "cráter" y "que" en el texto de la noticia.'''

archivo = open("noticia.txt", encoding="utf8")
lineas = archivo.readlines()

contadorCrater = 0
contadorQue = 0
crater = "CRÁTER"
que = "QUE"

no_deseado = ['\n', '"', ',', '.']

for linea in lineas:
    
    # eliminamos los distintos carácteres no deseados uno por uno
    for caracter in no_deseado:
      linea = linea.replace(caracter,'')

    palabras_linea = linea.split(' ')
    for palabra in palabras_linea:
        aux = palabra.upper()
        if (aux == crater ):
            contadorCrater += 1
        if (aux == que):
            contadorQue += 1

print("Cantidad de palabras: ")
print (f"Cráter = {contadorCrater} \tQue = {contadorQue}")
archivo.close()