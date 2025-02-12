import pygame
import sys

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Set up the screen
screen_width, screen_height = 1300, 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic vs Zombie")

# Set up clock
clock = pygame.time.Clock()

# Load sounds
collision_sound = pygame.mixer.Sound("Sound/Mario Death - Sound Effect (HD).mp3")
collision_sound.set_volume(0.5)
win_sound = pygame.mixer.Sound("Sound/26. winmusic.mp3")
win_sound.set_volume(0.5)

# Load fonts
game_over_font = pygame.font.Font("Font/BloodLust.ttf", 100)
continue_font = pygame.font.Font("Font/MyGirlIsRetro-0Grz.ttf", 50)

# Load images
background = pygame.image.load("Background/Backgnd.png")
zombie = pygame.image.load("Player/zombie.png").convert_alpha()
ambulance = pygame.image.load("Road_1/ambulance.png").convert_alpha()
buggy = pygame.image.load("Road_1/buggy.png").convert_alpha()
truck = pygame.image.load("Road_1/truckdelivery.png").convert_alpha()
school_bus = pygame.image.load("Road_2/bus_school.png").convert_alpha()
convertible = pygame.image.load("Road_2/convertible.png").convert_alpha()
transport = pygame.image.load("Road_3/transport.png").convert_alpha()
sedan = pygame.image.load("Road_3/sedan.png").convert_alpha()
police = pygame.image.load("Road_3/police.png").convert_alpha()

# Vehicle positions
vehicle_positions = {
    'ambulance': (100, 125),
    'buggy': (600, 125),
    'truck': (1000, 125),
    'school_bus': (325, 260),
    'convertible': (975, 260),
    'police': (1000, 395),
}

collision_status = {vehicle: False for vehicle in vehicle_positions}

# Initialize player position
zombie_pos = [5, 25]
speed = 7

def game_over_screen():
    screen.fill((0, 0, 255))  # Blue background
    game_over_text = game_over_font.render("GAME OVER", 1, (136, 8, 8))
    screen.blit(game_over_text, (450, 275))
    continue_text = continue_font.render("Press enter to restart", 1, (136, 8, 8))
    screen.blit(continue_text, (400, 500))
    pygame.display.update()

def vehicle_movement():
    for vehicle, (x, y) in vehicle_positions.items():
        if vehicle == 'school_bus' or vehicle == 'convertible':
            x -= 7
            if x <= -10:
                x = screen_width
        else:
            x += 4
            if x >= screen_width:
                x = 0
        vehicle_positions[vehicle] = (x, y)
        screen.blit(eval(vehicle), (x, y))

def check_collision():
    zombie_rect = zombie.get_rect(topleft=zombie_pos)
    for vehicle, (x, y) in vehicle_positions.items():
        vehicle_rect = eval(vehicle).get_rect(topleft=(x, y))
        if zombie_rect.colliderect(vehicle_rect) and not collision_status[vehicle]:
            collision_sound.play()
            collision_status[vehicle] = True
            print(f"Collision with {vehicle} detected!")
            game_over_screen()
            return True
    return False

zombie_pos = [5, 25]
collision_status = {vehicle: False for vehicle in vehicle_positions}

# Game loop
def main():
    global zombie_pos
    global collision_status

    running = True
    wait_to_restart = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    collision_status = {vehicle: False for vehicle in vehicle_positions}
                    zombie_pos = [5, 25]
                    wait_to_restart = False

        keys = pygame.key.get_pressed()
        zombie_pos[0] += (keys[pygame.K_d] - keys[pygame.K_a]) * speed
        zombie_pos[1] += (keys[pygame.K_s] - keys[pygame.K_w]) * speed

        screen.blit(background, (0, 0))
        screen.blit(zombie, zombie_pos)
        vehicle_movement()

        if check_collision():
            while any(collision_status.values()):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            collision_status = {vehicle: False for vehicle in vehicle_positions}
                            zombie_pos = [5, 25]

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
