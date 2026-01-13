# 🚀 El que sigue es el #8
# 🧩 Ejercicio #8 — isLucky

# 📌 Problema isLucky

# Un número es “lucky” si:

# La suma de la primera mitad de sus dígitos

# Es igual a la suma de la segunda mitad

# 🧪 Ejemplo
# n = 1230
# # 1 + 2 == 3 + 0 → True

def isLucky(n):
    string = str(n)
    mitad1 = string[:len(string)//2]
    mitad2 = string[len(string)//2:]

    total1 = 0
    for i  in mitad1:
        total1 += int(i)

    total2 = 0
    for i  in mitad2:
        total2 += int(i)

    if total1 != total2:
        return False

    return True

response = isLucky(1230)
print(response)