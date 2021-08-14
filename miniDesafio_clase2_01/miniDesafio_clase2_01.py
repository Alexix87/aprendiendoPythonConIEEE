'''Una función que convierta grados Celsius a grados Farenheit'''
'''Una función que convierta grados Celsius a grados Kelvin'''

def celsiusAfarenheit(celsius):
    if (celsius <= (-273.15)):
        print ("La temperatura es más baja que el cero absouluto!")
    else:    
        print(1.8*celsius + 32)

def celsiusAkelvin(celsius):
    if (celsius <= (-273.15)):
        print ("La temperatura es más baja que el cero absouluto!")
    else:    
        print(celsius + 273.15)

celsiusAkelvin(10)