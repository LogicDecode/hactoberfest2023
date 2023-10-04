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

# Initialize game variables
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_dx, snake_dy = 0, 0
snake_length = 1
snake_body = [(snake_x, snake_y)]

food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

score = 0
game_over = False

# Function to handle events
def handle_events():
    global snake_dx, snake_dy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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

# Function to update snake and game logic
def update_game():
    global snake_x, snake_y, snake_length, score, game_over

    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = get_random_food_position()
        snake_length += 1
        score += 1

    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    if (
        snake_x < 0
        or snake_x >= WIDTH
        or snake_y < 0
        or snake_y >= HEIGHT
        or (snake_x, snake_y) in snake_body[:-1]
    ):
        game_over = True

# Function to get a random food position
def get_random_food_position():
    return (
        random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
        random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
    )

# Main game loop
while not game_over:
    handle_events()
    update_game()

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    for segment in snake_body:
        pygame.draw.rect(screen, RED, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
    pygame.time.Clock().tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()


