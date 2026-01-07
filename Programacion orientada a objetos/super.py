# Clase base más general
# Representa lo MÁS básico que todo ser vivo debe tener
class LivingBeing:
    def __init__(self, name):
        # Este atributo pertenece al objeto final (Student)
        # aunque se defina aquí
        self.name = name


# Person hereda de LivingBeing
# Una persona ES un ser vivo
class Person(LivingBeing):
    def __init__(self, name, age):
        # super().__init__(name)
        # 👉 Le dice a LivingBeing:
        # "ejecuta tu __init__ usando ESTE MISMO objeto"
        # Aquí se inicializa self.name
        super().__init__(name)

        # Person agrega SU responsabilidad
        self.age = age


# Student hereda de Person
# Un estudiante ES una persona
class Student(Person):
    def __init__(self, name, age, student_id):
        # super().__init__(name, age)
        # 👉 Le dice a Person:
        # "haz tu parte (y la de LivingBeing) con este mismo objeto"
        # Aquí se inicializan:
        # self.name (LivingBeing)
        # self.age  (Person)
        super().__init__(name, age)

        # Student agrega lo que solo él conoce
        self.student_id = student_id

    
    def introduce(self):
        # Este método funciona porque:
        # name viene de LivingBeing
        # age viene de Person
        # student_id viene de Student
        print(
            f"Hi, I'm {self.name}, "
            f"{self.age} years old, "
            f"and my student ID is {self.student_id}"
        )


# Aquí se crea UN SOLO objeto de tipo Student
# El __init__ se ejecuta en cadena:
# Student -> Person -> LivingBeing
student = Student("Carlos", 21, "S54321")

# El objeto ya tiene TODOS los atributos
student.introduce()