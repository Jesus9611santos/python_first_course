# 🧩 EJERCICIO – String Parsing + Ventana + Concatenación
# Revertir solo las letras de cada ventana K

# Dado un string s y un entero k, construye un nuevo string donde:

# Se toma el string en bloques de tamaño k

# En cada bloque:

# solo las letras se invierten

# los números y símbolos se quedan en su posición

# El resultado se concatena y se regresa

# 🧠 Ejemplo 1
# s = "ab1c2d"
# k = 3

# Bloques:
# "ab1" → letras: a b → "ba1"
# "c2d" → letras: c d → "d2c"

# Resultado → "ba1d2c"
def funcion(s,k):
    cadena = ""
    for i in range(0,len(s),k):
        subcadena = s[i:i+k]
        numbers = set()
        sub = []
        for j in range(len(subcadena)):
            if 'a' <= subcadena[j] <= 'z' or 'A' <= subcadena[j] <= 'Z':
                sub.append(subcadena[j])
            else:
                numbers.add((j,subcadena[j]))
            
        left = 0
        right = len(sub) - 1
        while left < right:
            sub[left], sub[right] = sub[right], sub[left]
                
            left += 1
            right -= 1
        
        for key, value in numbers:
            sub.insert(key, value)

        for i in sub:
            cadena += i        


    return cadena
                  
s = "ab1c2d"
k = 3
s = "A1b2C3"
k = 2
print(funcion(s,k))