# 🧩 Ejercicio #11 — commonCharacterCount
# 📌 Problema

# Dadas dos cadenas s1 y s2, encuentra el número total de caracteres en común entre ambas.

# 👉 Cada carácter solo puede contarse tantas veces como aparezca en ambas cadenas.

# 🧪 Ejemplo
# s1 = "aabcc"
# s2 = "adcaa"


# Explicación:
# 'a' aparece 2 veces en ambas → cuenta 2
# 'c' aparece 1 vez en ambas → cuenta 1
# 👉 Resultado:
# 3

def commonCharacterCount(s1, s2):

    #Primero cuento cuántas veces aparece cada carácter en la primera cadena usando un diccionario.
    counts = {}
    for i in s1:
        counts[i] = counts.get(i, 0) + 1

    #Luego hago lo mismo con la segunda cadena.
    counts2 = {}
    for i in s2:
        counts2[i] = counts2.get(i, 0) + 1

    #Establecemos una variable para ir sumando el total
    total = 0
    #recorremos el primer diccionario para sacar las letras
    for char in counts:
        #Luego verificamos si el caracter actual existe en la coleccion para que no de error cuando intentemos indexar
        if char in counts2:
            #min es una funcion en python que te da el minimo y le pasamos los 2 numeros
            #sumamos el resultado al total
            total += min(counts[char], counts2[char])
        
    return total

s1 = "aabcc"
s2 = "adcaa"
response = commonCharacterCount(s1,s2)
print(response)