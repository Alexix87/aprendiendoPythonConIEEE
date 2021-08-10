'''El número  e  tiene inmensa utilidad para el análisis y la estadística, es una de las super-estrellas de la matemática, y su utilidad radica en que la función  ex  es igual a su derivada, por definición de  e .

Gracias a las series de Taylor podemos obtener la siguiente definición del número  e :

e=1+1/1!+1/2!+1/3!+1/4!+1/5!+... 
Se pide obtener una aproximación del número  e  calculando la suma de los primeros  20  términos de esta sucesión infinita.'''

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)
        
cantidadTerminos = 20
e = 0

for i in range(0,cantidadTerminos):
    e += 1/factorial(i)

print("el valor aproximado de e es: ", e)
