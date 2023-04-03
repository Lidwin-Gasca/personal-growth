import random
import pygame
import os

# Set up the game window
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")

# Set up the images
base_folder = os.path.dirname(__file__)
image_folder = os.path.join(base_folder, "images")
rock_image = pygame.image.load(os.path.join(image_folder, "rock.png"))
paper_image = pygame.image.load(os.path.join(image_folder, "paper.png"))
scissors_image = pygame.image.load(os.path.join(image_folder, "scissors.png"))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game loop
choices = ["rock", "paper", "scissors"]
user_choice = None

while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                user_choice = "rock"
            elif event.key == pygame.K_p:
                user_choice = "paper"
            elif event.key == pygame.K_s:
                user_choice = "scissors"

    # Update the screen
    screen.fill((255, 255, 255))
    screen.blit(rock_image, (100, 100))
    screen.blit(paper_image, (250, 100))
    screen.blit(scissors_image, (400, 100))

    if user_choice is not None:
        computer_choice = random.choice(choices)
        result = None
        if user_choice == computer_choice:
            result = "Tie!"
        elif user_choice == "rock" and computer_choice == "scissors":
            result = "You win!"
        elif user_choice == "paper" and computer_choice == "rock":
            result = "You win!"
        elif user_choice == "scissors" and computer_choice == "paper":
            result = "You win!"
        else:
            result = "You lose!"
        text = font.render(result, True, (0, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 300))

    pygame.display.update()
