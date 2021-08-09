'''Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado. 
Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. 
Luego, para cada producto, se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo. 
Posteriormente el programa imprimirá dicho código.'''

productosDiferentes = int(input("Ingrese cantidad de productos diferentes: "))

for cantidadProductosDiferentes in range(1,productosDiferentes+1):
    codigo = input("Ingrese codigo: ")
    cantidad = int(input("Ingrese cantidad con ese codigo: "))
    for cantidadCodigos in range(1,cantidad+1):
        print(codigo)

        