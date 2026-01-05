#primera regla poner la formula para cada elemento
#No es “fórmula” en sentido matemático estricto, es una expresión.
#segunda definimos el for para recorrer el arreglo
#en este caso range es la coleccion de datos
squares = [x**2 for x in range(1,11)]
#print("Los cuadrados son:", squares)

#transformar grados celsius a fahrenheit

#primera regla la formula °F=(9/5*°C) * 32
#No es “fórmula” en sentido matemático estricto, es una expresión.
#segunda definimos el for para recorrer el arreglo
#en este caso celsius es la coleccion de datos
celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)

#Ejercicion numeros pares incluyendo if
#[ EXPRESIÓN for ELEMENTO in ITERABLE if CONDICIÓN ]
evens = [x for x in range(1,21) if x%2 == 0]
#print(evens)

#La transpuesta de una matriz es voltear la matriz por su diagonal.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)

print(transposed)
