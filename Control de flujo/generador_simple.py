#yield — devuelve y PAUSA la función
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#Fibonacci tienes un valor sumando los 2 anteriores
# 0 1 1 2 3 5 8 13 21...
    
def fibonacci(limit):
    a=0
    b=1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)