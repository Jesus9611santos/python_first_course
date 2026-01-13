# 🧩 Ejercicio #10 — addBorder
# 📌 Problema

# Dado un arreglo de strings (todas del mismo tamaño), agrega un borde de * alrededor.

# 🧪 Ejemplo
# picture = ["abc", "ded"]


# Resultado:

# [
#   "*****",
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

def add_border(picture):
    border = "*" * (len(picture[0]) + 2)
    result = [border]
    
    for row in picture:
        result.append(f"*{row}*")

    result.append(border)
    return result

picture = ["abc", "ded"]
print(add_border(picture))