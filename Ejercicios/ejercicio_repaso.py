#debo devolver un array de sumas aplicando la siguiente formula
#b[i] = a[i - 1] + a[i] + a[i + 1]

def funcion(a):
    b = []
    for i in range(len(a)):
        suma = 0
        suma += a[i]
        
        if i != 0:
            suma += a[i - 1]

        if i != len(a) - 1:
            suma += a[i + 1]

        b.append(suma)

    return b


a = [4, 0, 1, -2, 3]
print(funcion(a))
