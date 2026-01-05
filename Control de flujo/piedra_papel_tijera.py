print("Bienvenido al juego")
print('''Ingrese:
    piedra
    papel
    tijera
      ''')

player1 = input("Ingresa tu opcion jugador 1: ")
if player1 == "piedra" or player1 == "papel" or player1 == "tijera":
    print("La opcion del jugador 1 es valida")
else:
    print("La opcion del jugador 1 no es valida")
    exit()

player2 = input("Ingresa tu opcion jugador 2: ")
if player2 == "piedra" or player2 == "papel" or player2 == "tijera":
    print("La opcion del jugador 2 es valida")
else:
    print("La opcion del jugador 2 no es valida")
    exit()

if player1 == "piedra" and player2 == "papel":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 2")

elif player1 == "papel" and player2 == "piedra":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 1")

elif player1 == "papel" and player2 == "tijera":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 2")

elif player1 == "tijera" and player2 == "piedra":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 2")

elif player1 == "tijera" and player2 == "papel":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 1")

elif player1 == "piedra" and player2 == "tijera":
    print("El jugador 1 eligió", player1, 
          "El jugador 2 eligió", player2, 
          "ganó el jugador 1")

else:
    print("Empate 🤝 ambos eligieron", player1)

