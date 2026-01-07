#Clase es una plantilla generica para organizar el software
class Person:
    #Constructor es una funcion especial para definir atributos principales
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Funcion propia dentro de una clase se llama metodo
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

#Un objeto es una muestra particular o instancia de clase
person1 = Person("Ana",30)
person2 = Person("Juan",18)

person1.greet()
person2.greet()