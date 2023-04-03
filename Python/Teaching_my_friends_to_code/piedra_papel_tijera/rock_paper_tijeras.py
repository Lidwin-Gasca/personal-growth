import random

while True:
    opciones = ['piedra', 'papel', 'tijera']

    # Solicitar la opción del usuario
    usuario = input("Elige piedra, papel o tijera: ").lower()

    # Validar que la opción del usuario es correcta
    if usuario not in opciones:
        print("Opción inválida, intenta de nuevo.")
        continue

    # Generar la opción aleatoria de la computadora
    computadora = random.choice(opciones)

    print(f"La computadora eligió: {computadora}")

    # Determinar el ganador
    if usuario == computadora:
        print("Empate.")
    elif usuario == 'piedra' and computadora == 'tijera':
        print("¡Ganaste!")
    elif usuario == 'papel' and computadora == 'piedra':
        print("¡Ganaste!")
    elif usuario == 'tijera' and computadora == 'papel':
        print("¡Ganaste!")
    else:
        print("Perdiste.")

    # Preguntar si se desea jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        break

print("¡Gracias por jugar!") 
