# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# primero hay que entender el problema que quiere hacer?
#     invertir el array pero con in-place with O(1) lo que dice que sin crear otro array solo cambaindo posiciones

# como lo hago?
#     la clave seria ii invirtiendo de izuqierda a derecha cabiando de posicion hasta que se crusen

def reverse_string(s):
    #establesco el limite inferiori
    left = 0
    #establesco el limite maximo
    right = len(s) - 1

    #hacemos un bucle con while pq sera mientras se cumpla una condicion hasta que se cruce
    while left < right:
        #aqui hacemos la asignacion cruzada de los valores
        #esta linea se ejecuta hasta que hace el salto si lo tuvieramos separado perderiamos el valor
        s[left], s[right] = s[right], s[left]

        #luego agregamos uno a left y quitamos uno a right para cambiar los extremos
        left += 1
        right -= 1
        #si primero comenzaba de 0 y 4 ahora lo hara de 1 y 3 despues de 2 y 2 y aqui se rompera

    return s

#s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
print(reverse_string(s))