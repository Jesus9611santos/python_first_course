# 🧪 EJERCICIO 13 — longest_word_length
# 📌 Enunciado

# Dada una cadena de texto text, devuelve la longitud de la palabra más larga.

# 👉 Las palabras están separadas por espacios
# 👉 No hay signos raros (solo letras y espacios)

# 🧠 Ejemplo 1
# text = "Aprender python toma tiempo"
# resultado = 8


# 👉 "Aprender" tiene 8 letras

def longest_word_length(text):
    text_array = text.split()
    current_word = text_array[0]

    for i in range(1, len(text_array)):
        if len(text_array[i]) > len(current_word):
            current_word = text_array[i]

    return len(current_word)

text = "Aprender python toma tiempo"
print(longest_word_length(text))