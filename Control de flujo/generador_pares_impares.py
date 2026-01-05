#Obtener los numero pares 2,4,6,8,10....

def pares(limit):
    num = 2
    while num <= limit:
        yield num
        num += 2

#Obtener los numero impares 1,3,6,9....
def impares(limit):
    num = 1
    while num <= limit:
        yield num
        num += 2

for par in pares(10):
    print(par)

for impar in impares(10):
    print(impar)