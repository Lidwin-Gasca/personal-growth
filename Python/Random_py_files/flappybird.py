import pygame
import random

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

# Espacio entre los obstáculos
OBSTACLE_GAP = 200

# Creación de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Carga de fuente de texto
font = pygame.font.Font(None, FONT_SIZE)

# Coordenadas del pájaro
bird_x = WIDTH // 4
bird_y = HEIGHT // 2

# Coordenadas de los obstáculos
obstacles = []
for i in range(4):
    obstacle_height = random.randint(100, 400)
    obstacle_x = WIDTH + i * WIDTH // 2
    obstacles.append(pygame.Rect(obstacle_x, 0, 50, obstacle_height))
    obstacles.append(pygame.Rect(obstacle_x, obstacle_height + OBSTACLE_GAP, 50, HEIGHT - obstacle_height - OBSTACLE_GAP))

# Puntuación del jugador
score = 0

# Estado del juego
game_over = False

# Estado del menú de cambio de entrada
change_input = False

# Creación del reloj
clock = pygame.time.Clock()

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

        # Mover los obstáculos
        for obstacle in obstacles:
            obstacle.x -= SPEED

        # Crear nuevos obstáculos cuando los primeros dos de las cuatro entidades salgan de pantalla
        if obstacles[0].right <= 0:
            obstacle_height = random.randint(100, 400)
            obstacles.pop(0)
            obstacles.pop(0)
            obstacles.append(pygame.Rect(WIDTH, 0, 50, obstacle_height))
            obstacles.append(pygame.Rect(WIDTH, obstacle_height + OBSTACLE_GAP, 50, HEIGHT - obstacle_height - OBSTACLE_GAP))

    # Detección de colisión con el suelo
    if bird_y >= HEIGHT - 50:
        game_over = True

    # Detección de colisión con los obstáculos
    for obstacle in obstacles:
        if bird_x + 50 > obstacle.left and bird_x < obstacle.right:
            if bird_y < obstacle.top or bird_y + 50 > obstacle.bottom:
                game_over = True
                break

    # Actualización
    # Actualización de la ventana
    screen.fill(WHITE)

    # Dibujar los obstáculos
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Dibujar el pájaro
    pygame.draw.rect(screen, BLACK, pygame.Rect(bird_x, bird_y, 50, 50))

    # Dibujar la puntuación
    score_text = font.render('Score: {}'.format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Actualizar la ventana
    pygame.display.flip()

    # Verificar si el pájaro toca el suelo o los obstáculos
    if game_over:
        # Mostrar mensaje de Game Over
        game_over_text = font.render('Game Over', True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()

        # Esperar 2 segundos antes de reiniciar el juego
        pygame.time.delay(2000)

        # Reiniciar las variables del juego
        bird_y = HEIGHT // 2
        obstacles = []
        for i in range(4):
            obstacle_height = random.randint(100, 400)
            obstacle_x = WIDTH + i * WIDTH // 2
            obstacles.append(pygame.Rect(obstacle_x, 0, 50, obstacle_height))
            obstacles.append(pygame.Rect(obstacle_x, obstacle_height + OBSTACLE_GAP, 50, HEIGHT - obstacle_height - OBSTACLE_GAP))
        score = 0
        game_over = False
        change_input = False

    # Actualizar la puntuación cuando el pájaro pasa por un obstáculo
    for obstacle in obstacles:
        if bird_x > obstacle.right and not obstacle.colliderect(obstacle, bird_x, bird_y):
            score += 1

    # Limitar la velocidad de actualización de la ventana
    clock.tick(60)

# Cerrar pygame al salir del bucle
pygame.quit()
 