import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# something = False

fps = clock.get_fps()


# Screen
screen = pygame.display.set_mode((1300, 650))
pygame.display.set_caption("Traffic vs Zombie FPS: {}".format(fps))

# Lose sound
collision_sound = pygame.mixer.Sound("Sound/Mario Death - Sound Effect (HD).mp3")
collision_sound.set_volume(0.5)
# collision_sound_played = False

# Win Sound
win_sound = pygame.mixer.Sound("Sound/26. winmusic.mp3")
win_sound.set_volume(0.5)
# win_sound_played = False

# Lose screen
def game_over_screen():
    game_over_font = pygame.font.Font("Font/BloodLust.ttf", 100)
    screen.fill("Blue")
    game_over_text = game_over_font.render("GAME OVER", 1, (136, 8, 8))
    screen.blit(game_over_text, (450,275))
    continue_font = pygame.font.Font("Font/MyGirlIsRetro-0Grz.ttf", 50)
    continue_text = continue_font.render("Press enter to restart", 1,(136, 8, 8))
    screen.blit(continue_text,(400,500))
    pygame.display.update()


# Background
background = pygame.image.load("Background/Backgnd.png")

# Player implementation
zombie = pygame.image.load("Player/zombie.png").convert_alpha()
zombie_x_pos = 5
zombie_y_pos = 25
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
police_x_pos = 1000

collision_status = {
    'ambulance': False,
    'buggy': False,
    'truck': False,
    'school_bus': False,
    'convertible': False,
    'police': False,
}

running = True

def zombie_pos(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            zombie_rect = zombie.get_rect(midtop=(50, 50))
            screen.blit(zombie, zombie_rect)
            return True
            if event.key == pygame.K_ESCAPE:
                running = False
    # return False

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


a, b = 0, 0
c = 7
zombie_rect = zombie.get_rect(midtop=(zombie_x_pos, zombie_y_pos))

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Player motion
    keys = pygame.key.get_pressed()
    zombie_x_pos += (keys[pygame.K_d] - keys[pygame.K_a]) * c
    zombie_y_pos += (keys[pygame.K_s] - keys[pygame.K_w]) * c

    # Check for collisions
    zombie_rect = zombie.get_rect(midtop=(zombie_x_pos, zombie_y_pos))
    for vehicle_name, vehicle_rect in vehicle_rectangles.items():
        if zombie_rect.colliderect(vehicle_rect) and not collision_status[vehicle_name]:
            collision_sound.play()
            collision_status[vehicle_name] = True
            print(f"Collision with {vehicle_name} detected!")
            game_over_screen()
            while collision_status[vehicle_name]:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            collision_status = {key: False for key in collision_status}
                            zombie_x_pos = 5
                            zombie_y_pos = 25

    screen.blit(background, (a, b))
    screen.blit(zombie, zombie_rect)
    vehicle_movement()

    pygame.display.flip()
    clock.tick(60)
