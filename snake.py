import pygame
import sys
import time
import random

# Constants
WINDOW_SIZE = 400
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Snake Game')

# Snake Initial Configuration
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

def draw_score():
    font = pygame.font.SysFont(None, 35)
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_surface, (0, 0))


def check_border_collision():
    if snake_pos[0] >= WINDOW_SIZE or snake_pos[0] < 0 or snake_pos[1] >= WINDOW_SIZE or snake_pos[1] < 0:
        return True
    return False

def check_self_collision():
    # Check the snake's head against its body, excluding the head itself
    if snake_pos in snake_body[:-1]:
        return True
    return False

# Snake movement logic
def change_direction():
    global direction, change_to
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

def move_snake():
    global snake_pos, snake_body
    if direction == 'RIGHT':
        snake_pos[0] += SNAKE_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= SNAKE_SIZE
    if direction == 'UP':
        snake_pos[1] -= SNAKE_SIZE
    if direction == 'DOWN':
        snake_pos[1] += SNAKE_SIZE
    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

# Food spawn logic
def spawn_food():
    return [random.randrange(1, (WINDOW_SIZE//SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (WINDOW_SIZE//SNAKE_SIZE)) * SNAKE_SIZE]

food_pos = spawn_food()
food_spawn = True

# Draw food
def draw_food():
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

# Main game loop
score = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the snake
    change_direction()

    # Determine new head position
    new_head_pos = list(snake_pos)
    if direction == 'RIGHT':
        new_head_pos[0] += SNAKE_SIZE
    if direction == 'LEFT':
        new_head_pos[0] -= SNAKE_SIZE
    if direction == 'UP':
        new_head_pos[1] -= SNAKE_SIZE
    if direction == 'DOWN':
        new_head_pos[1] += SNAKE_SIZE

    # Check self collision with the new head position
    if new_head_pos in snake_body:
        # Reset the Score
        score = 0
        # Reset the snake
        snake_pos = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        direction = 'RIGHT'
        change_to = direction
        continue

    # Check food collision
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
        score += 1  # Increment the score
    else:
        snake_body.pop() # Remove the tail (keeping the length the same)

    # Update the snake's position
    snake_pos = new_head_pos
    snake_body.insert(0, list(snake_pos)) # Add a new head to the snake

    if not food_spawn:
        food_pos = spawn_food()
        food_spawn = True

    if check_border_collision():
        # Reset the Score
        score = 0
        # Reset the snake
        snake_pos = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        direction = 'RIGHT'
        change_to = direction

    # Draw everything
    window.fill((0, 0, 0))
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.flip()

    # Control snake speed
    clock.tick(SNAKE_SPEED)

    # Infinite loop
    if snake_pos[0] >= WINDOW_SIZE:
        snake_pos[0] = 0
    if snake_pos[0] < 0:
        snake_pos[0] = WINDOW_SIZE
    if snake_pos[1] >= WINDOW_SIZE:
        snake_pos[1] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = WINDOW_SIZE
