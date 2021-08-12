def factorial(n):
  return 1 if n<=1 else n*factorial(n-1)

def unoSobrePi(cantidadTerminos):
    sumatoria = 0
    for k in range (0,cantidadTerminos+1):
        numerador = factorial(4*k)*(1103+26390*k)
        denominador = (factorial(k)**4)*(396**(4*k))
        sumatoria += numerador/denominador
    return sumatoria*((2*(2**(1/2)))/9801)

print(1/unoSobrePi(120))

