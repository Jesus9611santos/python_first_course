# Un motociclista emprende un viaje por carretera. El viaje consta de n + 1puntos a diferentes altitudes. El motociclista comienza su viaje en un punto 0con la misma altitud 0.

# Se le proporciona una matriz de números enteros gainde longitud ndonde gain[i]es la ganancia neta de altitud entre puntos iy i + 1para todos ( 0 <= i < n). Devuelve la altitud más alta de un punto.

 

# Ejemplo 1:

# Entrada: ganancia = [-5,1,5,0,-7]
#  Salida: 1
#  Explicación: Las altitudes son [0,-5,-4,1,1,-6]. La más alta es 1.
# Ejemplo 2:

# Entrada: ganancia = [-4,-3,-2,-1,4,3,2]
#  Salida: 0
#  Explicación: Las altitudes son [0,-4,-7,-9,-10,-6,-3,-1]. La más alta es 0.


#OJO [i] cambiara de posicion por el siguiente [i + 1] para todo el array all (0 <= i < n)
#i​​​​​​ and i + 1 for all (0 <= i < n)

def largest_altitude(gain):
    current_altitude = 0
    max_altitude = 0
    
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    
    return max_altitude