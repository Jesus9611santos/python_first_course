# 🧩 EJERCICIO NUEVO (Tema 2 – ventana REAL)
# Substrings de tamaño K sin caracteres repetidos

# Dado un string s y un entero k, cuenta cuántas subcadenas de longitud k tienen todos sus caracteres distintos.

def funcion(s,k):
    contador = 0
    
    for i in range(len(s) -k +1):
        cadena = ""
        valid = True

        for j in s[i:i+k]:

            if j in cadena:
                valid = False
                break
                
            cadena += j

        if valid:
            contador += 1

    return contador

s = "abcabc"
#s = "abccde"
k = 3
print(funcion(s,k))