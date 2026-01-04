print("Nunca pares de aprender")#imprimir un string normal
print("Nunca", "pares", "de", "aprender")#, agrega un espacio automaticamente
print("Nunca" + "pares" + "de" + "aprender")#+ no agrega espacio
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")#Aqui podemos agregar los espacios explicitos
print("Nunca", "pares", "de", "aprender", sep="\ ")#sep agrega un simbolo antes del espacio
print("Nunca", end=" ")#end=" " concatena el sigueinte print y lo muestra en una sola linea
print("pares de aprender")

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)#concatenando con ,
print(f"Frase: {frase}, Autor: {author}")#concatenando con f
print("Frase: {}, Autor: {}".format(frase, author))#concatenando con format

valor = 3.14159
print("Valor: {:.2f}".format(valor))#estableces estrictamente el numero de decimales de salida

print("Hola\nmundo")#otra forma de agregar saltos de linea

print('Hola soy \'Carli\'')#agrgar comillas simples a la salida para decorar el texto

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")#poner \\ sirve para que python no interprete rutas como secuencias de escape