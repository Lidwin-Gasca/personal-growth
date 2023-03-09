import random

# lista de opciones de juego
opciones = ["piedra", "papel", "tijeras"]

# pregunta al jugador qué opción quiere elegir
jugador = input("Elige piedra, papel o tijeras: ").lower()

# asegura que la opción del jugador es válida
while jugador not in opciones:
    jugador = input("Esa no es una opción válida. Elige piedra, papel o tijeras: ").lower()

# la computadora elige aleatoriamente
computadora = random.choice(opciones)

# imprime la opción de la computadora
print("La computadora eligió:", computadora)

# determina el resultado del juego
if jugador == computadora:
    print("¡Empate!")
elif jugador == "piedra":
    if computadora == "papel":
        print("Perdiste :(")
    else:
        print("¡Ganaste!")
elif jugador == "papel":
    if computadora == "tijeras":
        print("Perdiste :(")
    else:
        print("¡Ganaste!")
elif jugador == "tijeras":
    if computadora == "piedra":
        print("Perdiste :(")
    else:
        print("¡Ganaste!")
