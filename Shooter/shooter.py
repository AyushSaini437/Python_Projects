import pygame, sys, random

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Variables
player_radius = 20
player_pos_x = SCREEN_WIDTH // 2
player_pos_y = SCREEN_HEIGHT - 100

bullets = []  # List to store bullets
enemies = []  # List to store enemies
y_pos = 0

score = 0

# Sounds 
shoot_sound = pygame.mixer.Sound("sfx/laser-shot-ingame-230500.mp3")
shoot_channel = pygame.mixer.Channel(0)

# Functions
def draw_player(x, y):
    pygame.draw.circle(screen, BLUE, (x, y), player_radius)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.line(screen, RED, bullet, (bullet[0], bullet[1] - 10), width=2)

def create_enemy():
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(0, 50)
    enemies.append(pygame.Rect(x, y, 20, 20))

for _ in range(5):
    create_enemy()

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot when left mouse button is clicked
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            shoot_channel.play(shoot_sound)
            bullets.append([player_pos_x, player_pos_y - player_radius])  # Add a new bullet

    # Move bullets
    for bullet in bullets:
        bullet[1] -= 5  # Move up

    # Remove bullets that go off screen
    for bullet in bullets[:]:
        if bullet[1] <= 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.y += 1

    for bullet in bullets[:]:
        bullte_rect = pygame.Rect(bullet[0], bullet[1], 2, 10)

        for enemy in enemies[:]:
            if bullte_rect.colliderect(enemy):
                print("Hit!!!")
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                create_enemy()

    # Draw everything
    draw_player(player_pos_x, player_pos_y)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos_x += 5
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos_x -= 5

    draw_bullets()

    draw_enemies()

    # Update screen
    pygame.display.flip()
    clock.tick(50)  

# Quit Pygame
pygame.quit()
sys.exit()
print(score)