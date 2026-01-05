# La recursividad es una función que se llama a sí misma para resolver un problema,
# dividiéndolo en problemas más pequeños hasta llegar a un caso base

#Factoriales
# 5! = 5*4*3*2*1
# 4! =   4*3*2*1
# 5! = 5*4!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
resultado = factorial(5)
print(resultado)

#Recursividad en la serie de fibonnaci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 3
print(fibonacci(number))

#Funcion para calcular la sumatoria de los numero naturales
#los numero naturales son numeros positivos

def sumatoria(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return "numero no natural"
    else:
        return n + sumatoria(n-1)
    
print(sumatoria(4))