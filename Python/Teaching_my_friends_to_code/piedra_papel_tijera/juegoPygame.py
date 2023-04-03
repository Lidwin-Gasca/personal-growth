import pygame
import random

# inicializa Pygame
pygame.init()

# define las constantes para los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# define las constantes para las opciones de juego
PIEDRA = 0
PAPEL = 1
TIJERAS = 2

# define las constantes para las posiciones de los botones
POSICIONES_BOTONES = [
    (100, 100),
    (250, 100),
    (400, 100)
]

# define la función que muestra el mensaje del resultado del juego
def mostrar_mensaje(resultado):
    # crea la fuente del texto
    fuente = pygame.font.SysFont("arial", 48)

    # crea el texto
    texto = fuente.render(resultado, True, BLANCO)

    # centra el texto en la pantalla
    x = (ANCHO - texto.get_width()) / 2
    y = (ALTO - texto.get_height()) / 2

    # dibuja el texto en la pantalla
    pantalla.blit(texto, [x, y])

# define la función que determina el resultado del juego
def determinar_resultado(jugador, computadora):
    if jugador == computadora:
        return "¡Empate!"
    elif jugador == PIEDRA:
        if computadora == PAPEL:
            return "Perdiste :("
        else:
            return "¡Ganaste!"
    elif jugador == PAPEL:
        if computadora == TIJERAS:
            return "Perdiste :("
        else:
            return "¡Ganaste!"
    elif jugador == TIJERAS:
        if computadora == PIEDRA:
            return "Perdiste :("
        else:
            return "¡Ganaste!"

# crea la pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("Piedra, papel o tijeras")

# crea los botones
fuente = pygame.font.SysFont("arial", 24)
botones = [
    {
        "texto": "Piedra",
        "posicion": POSICIONES_BOTONES[0],
        "rectangulo": None
    },
    {
        "texto": "Papel",
        "posicion": POSICIONES_BOTONES[1],
        "rectangulo": None
    },
    {
        "texto": "Tijeras",
        "posicion": POSICIONES_BOTONES[2],
        "rectangulo": None
    }
]

# crea el bucle principal del juego
jugando = True
while jugando:
    # maneja los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # obtiene la posición del clic del ratón
            x, y = pygame.mouse.get_pos()

            # determina si se hizo clic en algún botón
            for boton in botones:
                if boton["rectangulo"].collidepoint(x, y):
                    # el jugador eligió este botón
                    jugador = botones.index(boton)

                    # la computadora elige aleatoriamente
                    computadora = random.randint(0, 2)

                    # determina el resultado del juego
                   
