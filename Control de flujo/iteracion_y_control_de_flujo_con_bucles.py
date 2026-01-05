numbers = [1,2,3,4,5,6]
for i in numbers:
    print("Aqui i es igual a:", i)

#range es una funcion si se le pasa 1 numero va del 0 a un numero antes del especificado
for i in range(10):
    print(i)

#tambien se pueden pasar 2 si se quiere iniciar en otro
for i in range(3,10):
    print(i)

#dentro del for tambien se puede utilizar if
fruits = [
    "Manzana",
    "Pera",
    "Uva",
    "Naranja",
    "Tomate"
]

for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")


#mientras se cumpla una condicion vamos a entrar dentro del cuerpo del while
x = 0
while x<5:
    if x == 3:
        break#finaliza la iteracion
    print(x)
    x+=1

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue#salta la iteracion
    print("Aqui i es igual a:", i)