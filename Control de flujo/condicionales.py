x = 5
#El nivel de identacion es muy importante en python
if x > 5:
    print("X es mayor que 5")
elif x == 5:
    print("X es igual que 5")
else:
    print("X es menor que 5")
print("Finalizo la condicio")

y = 15
z = 20
if y>10 and z>25:#las 2 condiciones tienen que ser verdaderas
    print("y es mayor que 10 y z es mayo que 25")

if y>10 or z>25:#Una de las 2 condiciones tienen que ser verdaderas
    print("y es mayor que 10 o z es mayo que 25")

if not y>10:
    print("Y no es mayor que 10")

#if anidados if dentro de if
is_member = False
age = 14

if is_member:
    if age>=15:
        print("Puedes entrar al club, eres miembro y por lo menos tienes 15 años")
    else:
        print("No puedes entrar eres menor de 15 años")
else:
    print("No eres miembro")