# Question 1: Array Manipulation
# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

# Example

# For a = [4, 0, 1, -2, 3]: 
# – b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# – b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# – b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# – b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# – b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

# So, the output should be solution(a) = [4, 5, -1, 2, 1].

#ok the rules
#giveme array a and i make array b
#array a and b has the samen lenght 
#the problem has de formula a[i - 1] + a[i] + a[i + 1]
#ok lets go

def array_manipulation(a):
    #guardamos el tamaño del arreglo en una variable
    n = len(a)
    #creamos un segundo arreglo de puros 0 de la misma longitud
    b = [0 for _ in range(n)]
    #recorremos las pociiones
    for i in range(n):
        #le asignamos al valor a la posicion de b igual que en a si se sale de los rangos
        #cuando la posision no existe a[i - 1] y a[i + 1] simplemente cumple a[i]
        b[i] = a[i]
        #la posicion es mayor a 0 para que no intente acceder a un a[0 - 1] ya que no existe
        if i > 0:
            #ahora la posicion es 1 mayor a 0
            #b[i] = 0 + a[1-1] la posicion 0 es 4 en el segundo loop
            b[i] += a[i - 1]
        #la posicion es menor que el final del arreglo - 1 para que no se desborde
        if i < n - 1:
            #b[i] = 4 + a[0 + 1] la posicion 1 es 0 en el primero loop
            #en el segundo loop vulve a entrar aca por eso se manejan 2 ifs y no un if else para completar la formula
            #b[i] = 0 + 4 + a[1 + 1] la posision es 2 y el valor 1
            b[i] += a[i + 1]
    return b
        

a = [4, 0, 1, -2, 3]
print(array_manipulation(a))