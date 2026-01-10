#open() es la función base de Python para trabajar con archivos
#.txt
#.csv
#.json
#.xml
#.log

with open('./cuento.txt', 'r') as file:
    for lineas in file:
        #.strip() es un método de strings que sirve para limpiar texto
        #Evita líneas en blanco
        #Elimina saltos de línea
        #Hace la salida limpia
        print(lineas.strip())


#leer todas las lineas en una lista
#r hace referencia a leer el archivo
with open('./cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#Escribir al final del archivo
#a hace referencia append añadir informacion nueva al final
#w Hace referencia a sobreescribir y eliminar contenido previo
with open('./cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")

#sobreescribir el texto
with open('./cuento2.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")

with open('./cuento.txt', 'r') as file:
    lines = file.readlines()
    new_lines = []
    for line in lines:
        if line == '\n':
            new_lines.append(line)
    print(len(new_lines))