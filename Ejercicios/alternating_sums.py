# 🧩 Ejercicio #9 — alternatingSums
# 📌 Problema

# Dado un arreglo de números, divide la suma en dos equipos:

# Equipo 1: posiciones pares (índice 0, 2, 4, …)

# Equipo 2: posiciones impares (índice 1, 3, 5, …)

# Regresa un arreglo con ambas sumas.

# 🧪 Ejemplo
# a = [50, 60, 60, 45, 70]
# # índices: 0   1   2   3   4
# # equipo1 = 50 + 60 + 70 = 180
# # equipo2 = 60 + 45 = 105

# resultado = [180, 105]

def alternatingSums(a):
    team1 = 0
    team2 = 0

    #El for por si solo te devuelve el valor y el enumerate el indice y valor
    for i, value in enumerate(a):
        if i % 2 == 0:
            team1 += value
        else:
            team2 += value

    return [team1, team2]

a = [50, 60, 60, 45, 70]
response = alternatingSums(a)
print(response)