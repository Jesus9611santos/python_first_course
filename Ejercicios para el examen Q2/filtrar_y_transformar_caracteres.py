# 📝 EJERCICIO 2 (Strings + concatenación + parsing)

# Dado un string s, regresa un nuevo string donde:

# se eliminen todos los números

# se conserven solo letras

# y todas las letras queden en minúsculas

# ❌ No usar funciones built-in como isdigit(), isalpha(), lower()
# ✅ Usa loops, condiciones y concatenación

def funcion(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if 'A' <= i <= 'Z':
                result += chr(ord(i) + 32)
            else:
                result += i

    return result

s = "HeL1oW0rLD!"
print(funcion(s))
#char_minuscula = chr(ord(char) + 32)
