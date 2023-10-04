#Don't forget to install pygame library using pip install pygame
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

# Initial velocity
snake_dx = 0
snake_dy = 0

# Initial snake length
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Food position
food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

# Score
score = 0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if the snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        snake_length += 1
        score += 1

    # Update the snake's body
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check if the snake hits the wall or itself
    if (snake_x < 0 or snake_x >= WIDTH or
            snake_y < 0 or snake_y >= HEIGHT or
            (snake_x, snake_y) in snake_body[:-1]):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, GREEN, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, RED, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
