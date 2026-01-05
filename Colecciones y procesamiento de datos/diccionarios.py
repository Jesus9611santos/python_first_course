#los diccionarios tienen clave y valor
numbers = {
    1:"uno",
    2:"dos",
    3:"tres"
}

print(numbers)

#si queremos obtener un dato tenemos que hacer referencia a la llave y no a la pocision
print(numbers[1])
print(numbers[2])
print(numbers[3])

information = {
    "Nombre":"Jesus",
    "Apellido":"Reyes",
    "Edad":29,
    "Altura":1.64
}

print(information)

del information["Edad"]
print(information)

#metodo keys() nos muestra las llaves de nuestro diccionario
print(information.keys())

#metodo values() muestra los valores
print(information.values())

#metodo items() devuelve la clave y valor en tuplas
print(information.items())

#los diccionarios pueden tener multiples colecciones de datos

contacts = {
    "Jesus":{
        "Nombre":"Jesus",
        "Apellido":"Reyes",
        "Edad":29,
        "Altura":1.64
    },
    "Jany":{
        "Nombre":"Jany",
        "Apellido":"Santos",
        "Edad":27,
        "Altura":1.50
    }
}

print(contacts)
print(contacts["Jany"])