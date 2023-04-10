import pygame
import random
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana del juego
WIDTH = 400
HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño de la fuente
FONT_SIZE = 36

# Velocidad del juego
SPEED = 5

# Velocidad inicial del juego
INITIAL_SPEED = 2

# Aceleración del juego
ACCELERATION = 0.01

# Tamaño del gap entre los obstáculos
OBSTACLE_GAP = 200

# Cantidad de obstáculos en pantalla a la vez
MAX_OBSTACLES = 4

# Lista de obstáculos
obstacles = []

# Creación de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Carga de fuente de texto
font = pygame.font.Font(None, FONT_SIZE)

# Coordenadas del pájaro
bird_x = WIDTH // 4
bird_y = HEIGHT // 2

# Puntuación del jugador
score = 0

# Estado del juego
game_over = False

# Estado del menú de cambio de entrada
change_input = False

# Creación del reloj
clock = pygame.time.Clock()

# Función para crear un nuevo obstáculo
def create_obstacle():
    obstacle_height = random.randint(100, HEIGHT - OBSTACLE_GAP - 100)
    new_obstacle = pygame.Rect(WIDTH, 0, 50, obstacle_height)
    bottom_obstacle = pygame.Rect(WIDTH, obstacle_height + OBSTACLE_GAP, 50, HEIGHT - obstacle_height - OBSTACLE_GAP)
    obstacles.append(new_obstacle)
    obstacles.append(bottom_obstacle)

# Función para reiniciar el juego
def restart_game():
    global bird_y, score, game_over, change_input, obstacles, SPEED
    bird_y = HEIGHT // 2
    score = 0
    game_over = False
    change_input = False
    obstacles = []
    SPEED = INITIAL_SPEED

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Lógica para hacer saltar al pájaro al presionar la barra espaciadora
                bird_y -= 50
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] > WIDTH - 150 and pos[1] < 100:
                # Abrir el menú de cambio de entrada
                change_input = True

    # Lógica del juego
    if not change_input:
        bird_y += SPEED
        SPEED += ACCELERATION

        # Crear nuevos obstáculos
        if len(obstacles) < MAX_OBSTACLES * 2:
            create_obstacle()

        # Mover y dibujar los obstáculos
        for obstacle in obstacles:
            obstacle.x -= SPEED
            pygame.draw.rect(screen, BLACK, obstacle)
            if obstacle.colliderect(pygame.Rect(bird_x, bird_y, 50, 50)):
                # Detección de colisión con los obstáculos
                # Detección de colisión con los obstáculos
                if obstacle.colliderect(pygame.Rect(bird_x, bird_y, 50, 50)):
                    game_over = True
                    break

# Eliminar los obstáculos que salen de la pantalla
obstacles = [obs for obs in obstacles if obs.right > 0]

# Dibujar el fondo de la ventana
screen.fill(WHITE)

# Dibujar el pájaro
pygame.draw.rect(screen, BLACK, pygame.Rect(bird_x, bird_y, 50, 50))

# Mostrar la puntuación
score_text = font.render(f'Score: {score}', True, BLACK)
screen.blit(score_text, (10, 10))

# Actualizar la ventana
pygame.display.flip()

# Aumentar la puntuación
score += 1

# Aumentar la velocidad del juego
if score % 100 == 0:
    SPEED += ACCELERATION

# Verificar si el pájaro toca el suelo
if bird_y > HEIGHT - 50:
    game_over = True

# Controlar la velocidad del juego
clock.tick(60)

#Mensaje de fin de juego
game_over_text = font.render('Game Over. Press R to restart', True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 50))
pygame.display.flip()

# Bucle de reinicio de juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
