# 🧪 Ejercicio #10 – validAnagram

# Problema
# Dado s y t, regresa True si son anagramas, si no False.

# Ejemplo:

# s = "anagram"
# t = "nagaram"
# # True

# Un anagrama es una palabra o frase que se forma reordenando las letras de otra palabra o frase, usando exactamente las mismas letras y la misma cantidad, sin agregar ni quitar ninguna.
# Ejemplos simples
# amor → roma
# perro → ropre ❌ (este no cuenta porque no es una palabra válida)
# listen → silent

# 🔑 Punto CLAVE (esto es lo que debes quedarte)
# ❌ No es requisito que se forme otra palabra “con sentido”
# ✅ Sí es requisito que las letras coincidan exactamente

def valid_anagram(s,t):
    #Primero si la cadena no tiene la misma longitud si ni no es un anagrama
    if len(s) != len(t):
        return False
    
    #Segundo contamos las veces que cada letra aparece en la cadena y las guardamos en un diccionario
    count={}
    for i in s:
        count[i] = count.get(i, 0) + 1
    
    #Recorremos la segunda cadena
    for i in t:
        #Si el caracter actual en el loop no esta en la collecion ya no es un anagrama
        if i not in count:
            return False
        #aqui es como si tuvieramos una bolsa de letras en count[i] le quitamos la actual para verificar que existe
        count[i] -= 1

        #en este punto si existe seria 0 o mayor depende cuando existan si fuera -1 significa que no existe en la cadena
        if count[i] < 0:
            return False
    return True

response = valid_anagram('anagram','nagaram')
print(response)