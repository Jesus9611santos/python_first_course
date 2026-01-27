# 📝 EJERCICIO (Tema 2 – nivel examen medio)

# Dado un string s, regresa la longitud de la subcadena más larga que NO contenga números.

# 👉 No puedes usar isdigit(), isalpha(), set(), etc.
# 👉 Usa sliding window y validación manual.

def funcion(s):
    max_len = 0
    current_len = 0

    for i in range(len(s)):
        if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 0

    max_len = max(max_len, current_len)    

    return max_len
        

s = "ab12cde3fg"
s = "a1b2c3"
s = "abcdef"
s = "12345"
s = "12abc"
s = "!!@@##"  
print(funcion(s))