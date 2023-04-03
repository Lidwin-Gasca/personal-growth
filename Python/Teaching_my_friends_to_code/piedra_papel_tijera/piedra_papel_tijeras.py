

#       JUEGO EN TERMINAL: piedra papel o tijeras.


#   Que es una lista?

#       [item_1, item_2, etc] 



import random


x = 's'

while x == 's':

    # Lista de opciones de juego:
    opciones = ["piedra", "papel", "tijeras"]


    #  Pregunta al jugador que opcion quiere elegir:
    jugador = input("Elige piedra, papel, o tijera \t").lower()


    # La computadora elige aleatoriamente:
    computadora = random.choice(opciones)


    # Asegura que la opcion de el jugador sea valida:
    while jugador not in opciones:
         jugador = input(f"{jugador} no es una opcion valida.\nEscribe un valor valido:\t").lower()


    # Imprimir la opcion de la computadora:
    print(f"La computadora escogio: {computadora}.")


    # Determina el resultado del juego:
    if jugador == computadora:
         print("Empate!")
    elif jugador == "piedra":
        if computadora == "papel":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif jugador == "papel":
        if computadora == "tijeras":
            print("Perdiste!")
        else:
            print("Ganastes!")
    elif jugador == "tijeras":
        if computadora == "piedra":
            print("Perdiste!")
        else:
            print("Ganaste!")

    x = input("Deseas jugar otra vez?\nPresiona 'S' para si o 'N' para no.\n\t\t").lower()



