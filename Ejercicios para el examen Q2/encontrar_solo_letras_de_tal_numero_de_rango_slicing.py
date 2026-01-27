# 📝 EJERCICIO (Strings / slicing / validación)

# Dado un string s y un entero k, regresa cuántas subcadenas de longitud k contienen solo letras
# (no números, no símbolos).

def funcion(s,k):
    count = 0

    for i in range(len(s) - k + 1):
         valido = True

         for j in s[i:i + k]:
              if not ('a' <= j <= 'z' or 'A' <= j <= 'Z'):
                    valido = False
                    break
              
         if valido:
              count += 1

    return count

s = "ab1cDe!fg"
k = 2
print(funcion(s,k))