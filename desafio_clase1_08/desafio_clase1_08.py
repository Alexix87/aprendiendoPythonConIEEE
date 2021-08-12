'''Se debe programar la función integral(f, a, b, dx) 
en la cual f sea la función a integrar (la función f debe recibir como parámetro un número x, debe entregar el resultado usando return), 
a y b sean los límites de integración, 
dx sea el ancho de los rectángulos.'''

def f(x):
    return (2*x)+1

def integral(f,a,b,dx):
    aux = a
    acumulador = 0
    while aux < b:
        acumulador = acumulador + f(aux)*dx
        aux = aux + dx
    return acumulador

print(integral(f,0,1,0.0001))