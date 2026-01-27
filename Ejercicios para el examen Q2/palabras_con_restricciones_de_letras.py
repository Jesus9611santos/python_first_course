# 📝 Ejercicio: “Palabras con restricciones de letras”

# Se te da una cadena sentence que contiene palabras separadas por espacios. Tu tarea es contar cuántas palabras cumplen la siguiente regla:

# Una palabra cumple la regla si ninguna letra se repite inmediatamente.

# Es decir, no puede haber letras consecutivas iguales.

# Ejemplo
# sentence = "hello world aaa abcde book"


# Analizando palabra por palabra:

# "hello" → h,e,l,l,o → no cumple (l repetida)

# "world" → w,o,r,l,d → cumple ✅

# "aaa" → a,a,a → no cumple

# "abcde" → a,b,c,d,e → cumple ✅

# "book" → b,o,o,k → no cumple (o repetida)

# Resultado esperado: 2
def funcion(sentence):
    count = 0
    sentence_parts = sentence.split(" ")
    for i in sentence_parts:
        velid = True
        after_word = i[0]
        for j in range(1,len(i)):
            if i[j] == after_word:
                velid = False
                break

            after_word = i[j]
        if velid:
            count += 1

    return count

sentence = "hello world aaa abcde book"
sentence = "abc def ghi jkl"
sentence = "aa bb cc dd ee"
sentence = "a b c aa bb ccc d"
sentence = "programming mississippi assessment"
print(funcion(sentence))