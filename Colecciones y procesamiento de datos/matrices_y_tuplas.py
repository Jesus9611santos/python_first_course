#Las matrices tienen las mismas propiedades que la listas
#se puede añadir informacion, eliminar o modificarla
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2][2])

new_matrix = [
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ],
]

print(new_matrix[1][0][1])

#las tuplas son clases inmutables donde no se pueden hacer modificaciones
numbers = (1,2,3,4,5)
numbers = 1,2,3,4,5 #tambien asi se reconocen las tuplas podemos elegir utilizar los parentesis
print(numbers)
print(type(numbers))#python sabe que la clase es tipo tuple
print(numbers[0])#accedemos igual con indexacion

#del numbers[-1]#aqui nos da error porque las tuplas no se pueden modificar, ni eliminar

numbers[0] = "unos"#al igual que aqui a esto se le llama inmutable que no puede sufrir cambios

print(numbers)