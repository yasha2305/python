import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
GREEN = (34, 139, 34)
GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 30, 30)
BLUE = (30, 100, 220)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 70)

# Player car
car_width = 50
car_height = 90

car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 7

# Enemy car
enemy_width = 50
enemy_height = 90
enemy_speed = 6

enemy_x = random.randint(100, WIDTH - 150)
enemy_y = -100

score = 0
game_over = False


def draw_road():
    # Grass
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(screen, GRAY, (70, 0, 360, HEIGHT))

    # Road borders
    pygame.draw.line(screen, WHITE, (70, 0), (70, HEIGHT), 5)
    pygame.draw.line(screen, WHITE, (430, 0), (430, HEIGHT), 5)

    # Road lane markings
    for y in range(-20, HEIGHT, 80):
        pygame.draw.rect(screen, WHITE, (245, y, 10, 40))


def draw_car(x, y, color):
    # Main body
    pygame.draw.rect(
        screen,
        color,
        (x, y, car_width, car_height),
        border_radius=8
    )

    # Windows
    pygame.draw.rect(
        screen,
        (180, 220, 240),
        (x + 8, y + 10, 34, 25),
        border_radius=5
    )

    pygame.draw.rect(
        screen,
        (180, 220, 240),
        (x + 8, y + 48, 34, 25),
        border_radius=5
    )

    # Wheels
    pygame.draw.rect(screen, BLACK, (x - 5, y + 10, 7, 25))
    pygame.draw.rect(screen, BLACK, (x + car_width - 2, y + 10, 7, 25))
    pygame.draw.rect(screen, BLACK, (x - 5, y + 55, 7, 25))
    pygame.draw.rect(screen, BLACK, (x + car_width - 2, y + 55, 7, 25))


def reset_game():
    global car_x, enemy_x, enemy_y
    global score, game_over, enemy_speed

    car_x = WIDTH // 2 - car_width // 2
    enemy_x = random.randint(85, 365)
    enemy_y = -100

    score = 0
    enemy_speed = 6
    game_over = False


# Main game loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # Restart
            if event.key == pygame.K_r and game_over:
                reset_game()

            # Quit
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if not game_over:

        # Keyboard
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            car_x -= car_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            car_x += car_speed

        # Keep car inside road
        if car_x < 75:
            car_x = 75

        if car_x > 425 - car_width:
            car_x = 425 - car_width

        # Move enemy
        enemy_y += enemy_speed

        # Enemy reached bottom
        if enemy_y > HEIGHT:

            enemy_y = -100
            enemy_x = random.randint(85, 365)

            score += 1

            # Increase difficulty
            if score % 5 == 0:
                enemy_speed += 1

        # Collision
        player_rect = pygame.Rect(
            car_x,
            car_y,
            car_width,
            car_height
        )

        enemy_rect = pygame.Rect(
            enemy_x,
            enemy_y,
            enemy_width,
            enemy_height
        )

        if player_rect.colliderect(enemy_rect):
            game_over = True

    # Draw everything
    draw_road()

    draw_car(car_x, car_y, RED)
    draw_car(enemy_x, enemy_y, BLUE)

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (15, 15))

    # Game over screen
    if game_over:

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        restart_text = font.render(
            "Press R to Restart",
            True,
            WHITE
        )

        quit_text = font.render(
            "Press ESC to Quit",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                270
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                360
            )
        )

        screen.blit(
            quit_text,
            (
                WIDTH // 2 - quit_text.get_width() // 2,
                410
            )
        )

    pygame.display.update()

    clock.tick(60)