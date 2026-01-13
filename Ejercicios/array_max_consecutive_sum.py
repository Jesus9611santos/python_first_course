# 🧩 Ejercicio #11 — arrayMaxConsecutiveSum

# Este es muy importante para entrevistas, porque evalúa si conoces sliding window.

# 📌 Problema

# Dado un arreglo de enteros a y un número k, encuentra la suma máxima de k elementos consecutivos.

# 🧪 Ejemplo
# a = [2, 3, 5, 1, 6]
# k = 2


# Posibles sumas:

# 2 + 3 = 5

# 3 + 5 = 8

# 5 + 1 = 6

# 1 + 6 = 7

# 👉 Resultado:

# 8

def array_max_consecutive_sum(a, k):
    # Esta función encuentra la suma máxima de k elementos consecutivos en el arreglo a

    # a[:k] toma los primeros k elementos del arreglo
    # Ejemplo: si a = [2, 3, 5, 1] y k = 2 → a[:2] = [2, 3]
    # sum() suma esos elementos
    current_sum = sum(a[:k])

    # max_sum guarda la suma más grande encontrada hasta ahora
    max_sum = current_sum

    # range(k, len(a)) genera índices desde k hasta el último índice del arreglo
    # Ejemplo: si k=2 y len(a)=5 → range(2, 5) → 2, 3, 4
    for i in range(k, len(a)):

        # Aquí se aplica la técnica de "ventana deslizante"
        # Restamos el elemento que sale de la ventana (a[i-k])
        # Sumamos el nuevo elemento que entra a la ventana (a[i])
        current_sum = current_sum - a[i - k] + a[i]

        # Si la nueva suma es mayor que la máxima guardada
        if current_sum > max_sum:
            # Actualizamos la suma máxima
            max_sum = current_sum

    # Regresamos la suma máxima de k elementos consecutivos
    return max_sum

a = [2, 3, 5, 1, 6]
k = 2
print(array_max_consecutive_sum(a,k))