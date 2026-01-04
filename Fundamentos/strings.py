name = 'Jesus Reyes Santos'#no son sensibles a saltos de linea
name = "Jesus Reyes Santos"#no son sensibles a saltos de linea
name = '''Jesus 
Reyes 
Santos''' #comillas triples si
print(type(name))
print(name)

#Indexacion para cadenas
#consulta de posiciones
jugito = "Jumex Valle"
print(jugito)
print(jugito[0])
print(jugito[1])
print(jugito[2])
print(jugito[3])
print(jugito[4])
print(jugito[5])

print(jugito[-1])#negativo para obtener de atras para delante

#concatenacion
name1 = "Jesus"
lastname = "Santos"

print(name1 + " " + lastname)

#repeticion
print(3 * (name1 + " " + lastname))

#contar caracteres de un string
print(len(name1 + " " + lastname))

#len es una funcion y existen metodos que son propios de las variables
#Metodo para transformar a minusculas y mayusculas
mayusculas = "PERRO"
minusculas = "  gato  "
print(mayusculas.lower())
print(minusculas.upper())
print(minusculas.strip())#elimina espacios