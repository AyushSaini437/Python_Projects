import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((1300, 650))
clock = pygame.time.Clock()
fps = clock.get_fps()

# Lose sound
collision_sound = pygame.mixer.Sound("Sound/Mario Death - Sound Effect (HD).mp3")
collision_sound.set_volume(0.5)

# Background
background = pygame.image.load("Background/Backgnd.png")

# Player implementation
zombie = pygame.image.load("Player/zombie.png").convert_alpha()
zombie_x_pos = 615
zombie_y_pos = 10
pygame.key.set_repeat(1, 100)

# Vehicles on road
ambulance = pygame.image.load("Road_1/ambulance.png").convert_alpha()
buggy = pygame.image.load("Road_1/buggy.png").convert_alpha()
truck = pygame.image.load("Road_1/truckdelivery.png").convert_alpha()

school_bus = pygame.image.load("Road_2/bus_school.png").convert_alpha()
convertible = pygame.image.load("Road_2/convertible.png").convert_alpha()

transport = pygame.image.load("Road_3/transport.png").convert_alpha()
sedan = pygame.image.load("Road_3/sedan.png").convert_alpha()
police = pygame.image.load("Road_3/police.png").convert_alpha()

ambulance_x_pos = 100
buggy_x_pos = 600
truck_x_pos = 1000

school_bus_x_pos = 325
convertible_x_pos = 975

transport_x_pos = 100
sedan_x_pos = 600
police_x_pos = 605

collision_status = {
    'ambulance': False,
    'buggy': False,
    'truck': False,
    'school_bus': False,
    'convertible': False,
    'police': False,
}

def zombie_movement():
    global zombie_x_pos
    global zombie_y_pos
    global zombie_rect
    zombie_rect = zombie.get_rect(midtop=(zombie_x_pos, zombie_y_pos))
    c = 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                zombie_y_pos -= c
            if event.key == pygame.K_s:
                zombie_y_pos += c
            if event.key == pygame.K_a:
                zombie_x_pos -= c
            if event.key == pygame.K_d:
                zombie_x_pos += c

    screen.blit(zombie, zombie_rect)

def zombie_pos(event):
    global running
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return True
        elif event.key == pygame.K_ESCAPE:
            running = False
    return False

def vehicle_implement():
    screen.blit(ambulance,(ambulance_x_pos,125))
    screen.blit(buggy,(buggy_x_pos,125))
    screen.blit(truck,(truck_x_pos,125))
    screen.blit(school_bus,(school_bus_x_pos,260))
    screen.blit(convertible,(convertible_x_pos,260))
    screen.blit(police,(police_x_pos,390))


vehicle_rectangles = {
    'ambulance': ambulance.get_rect(topleft=(ambulance_x_pos, 125)),
    'buggy': buggy.get_rect(topleft=(buggy_x_pos, 125)),
    'truck': truck.get_rect(topleft=(truck_x_pos, 125)),
    'school_bus': school_bus.get_rect(topleft=(school_bus_x_pos, 260)),
    'convertible': convertible.get_rect(topleft=(convertible_x_pos, 260)),
    'police': police.get_rect(topleft=(police_x_pos, 395))
    }

def vehicle_movement():
# Motion of vehicles on road
    global ambulance_x_pos
    ambulance_x_pos += 4
    if ambulance_x_pos >= 1320:
        ambulance_x_pos = 0
    screen.blit(ambulance, (ambulance_x_pos, 125))

    global buggy_x_pos
    buggy_x_pos += 4
    if buggy_x_pos >= 1320:
        buggy_x_pos = 0
    screen.blit(buggy, (buggy_x_pos, 125))

    global truck_x_pos
    truck_x_pos += 4
    if truck_x_pos >= 1320:
        truck_x_pos = 0
    screen.blit(truck, (truck_x_pos, 125))

    global school_bus_x_pos
    school_bus_x_pos -= 7
    if school_bus_x_pos <= -10:
        school_bus_x_pos = 1300
    screen.blit(school_bus, (school_bus_x_pos, 260))

    global convertible_x_pos
    convertible_x_pos -= 7
    if convertible_x_pos <= -10:
        convertible_x_pos = 1300
    screen.blit(convertible, (convertible_x_pos, 260))

    global police_x_pos
    police_x_pos += 10
    if police_x_pos > 1320:
        police_x_pos = 0
    screen.blit(police, (police_x_pos, 395))


def collision_check():
    # Check for collisions
    for vehicle_name, vehicle_rect in vehicle_rectangles.items():
        if zombie_rect.colliderect(vehicle_rect) and not collision_status[vehicle_name]:
            collision_sound.play()
            collision_status[vehicle_name] = True
            print(f"Collision with {vehicle_name} detected!")
            game_over_screen()


def collision_reset():
    global collision_status, zombie_x_pos, zombie_y_pos
    for key in collision_status:
        collision_status[key] = False
    zombie_x_pos = 615
    zombie_y_pos = 10

# Lose screen
def game_over_screen():
    game_over_font = pygame.font.Font("Font/BloodLust.ttf", 100)
    screen.fill("Blue")
    game_over_text = game_over_font.render("GAME OVER", 1, (136, 8, 8))
    screen.blit(game_over_text, (450, 275))
    continue_font = pygame.font.Font("Font/MyGirlIsRetro-0Grz.ttf", 50)
    continue_text = continue_font.render("Press enter to restart", 1, (136, 8, 8))
    screen.blit(continue_text, (400, 500))

def game_win_screen():
    game_win_font = pygame.font.Font("Font/BloodLust.ttf", 100)
    screen.fill("Blue")
    game_over_text = game_over_font.render("YOU WIN", 1, (136, 8, 8))
    screen.blit(game_over_text, (450, 275))
    exit_font = pygame.font.Font("Font/MyGirlIsRetro-0Grz.ttf", 50)
    continue_text = continue_font.render("Press enter to restart", 1, (136, 8, 8))
    exit_text = continue_font.render("Press escape to end", 1, (136, 8, 8))
    screen.blit(continue_text, (400, 500))

def game():
    global running
    running = True
    game_over = False

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            screen.blit(background, (0, 0))
            zombie_movement()
            vehicle_movement()

            if collision_check():
                game_over = True

            pygame.display.flip()
            clock.tick(60)

        else:
            game_over_screen()
            pygame.display.flip()
            clock.tick(1)  # Limit to 1 FPS for the game over screen

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_over = False
                    collision_reset()

if __name__ == "__main__":
    game()
