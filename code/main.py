import pygame, sys, time, random
from settings import *


class Ground:
    def __init__(self, game):
        self.ground_pos = pygame.Vector2(0, WINDOW_HEIGHT - 20)
        self.game = game  # Reference to Game

    def circle_collide_with_ground(self, player):
        circle_rect = pygame.Rect(
            player.player_pos.x - CIRCLE_RADIUS,
            player.player_pos.y - CIRCLE_RADIUS,
            CIRCLE_RADIUS * 2,
            CIRCLE_RADIUS * 2 + 1
        )
        return circle_rect.colliderect(self.game.ground_rect)

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player:
    def __init__(self, ground):
        self.player_pos = pygame.Vector2(PLAYER_ORIGINAL_POS_X, PLAYER_ORIGINAL_POS_Y)
        self.player_speed_on_x = PLAYER_SPEED_ON_X
        self.player_speed_on_y = PLAYER_SPEED_ON_Y
        self.jump_strength = JUMP_STRENGHT
        self.ground = ground  # Reference to Ground
        self.player_rect = pygame.Rect(self.player_pos.x, self.player_pos.y, CIRCLE_DIAMETER, CIRCLE_DIAMETER)
        self.bounce_factor = 0.6
        self.vertical_velocity = 0

    def player_movements(self, delta_time, keys):
        self.direction = pygame.Vector2(0, 0)

        if(self.direction.length() > 100):
            self.direction = self.direction.normalize()

        # Horizontal Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x -= 1 * self.player_speed_on_x

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x += 1 * self.player_speed_on_x

        # Vertical Movement (Simulating Gravity + Jump)
        self.vertical_velocity += self.jump_strength * delta_time
        if keys[pygame.K_SPACE] and (self.ground.circle_collide_with_ground(self)):
            self.vertical_velocity = -self.jump_strength * self.player_speed_on_y * 0.16

        # Update Position
        self.player_pos.x += self.direction.x * self.player_speed_on_x * delta_time * 2
        self.player_pos.y += self.vertical_velocity * delta_time * 2

        # Debug Position
        print(f"Player Position: {self.player_pos}")

        # Keep Player Within Window Boundaries
        self.player_pos.x = max(CIRCLE_RADIUS, min(WINDOW_WIDTH - CIRCLE_RADIUS, self.player_pos.x))

        if(self.player_pos.y >= self.ground.ground_pos.y - CIRCLE_RADIUS):
            self.player_pos.y = self.ground.ground_pos.y - CIRCLE_RADIUS  # Reset to ground level

    def reset_position(self):
        self.player_pos = pygame.Vector2(PLAYER_ORIGINAL_POS_X, PLAYER_ORIGINAL_POS_Y)

    def player_jump(self, delta_time):
        if self.ground.circle_collide_with_ground(self):
            self.player_pos.y -= self.jump_strength * delta_time


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Jump")

        self.color = "white"
        self.ground_rect = pygame.Rect(0, WINDOW_HEIGHT - 20, WINDOW_WIDTH, 20)
        self.ground = Ground(self)  # Pass self to Ground
        self.player = Player(self.ground)  # Pass Ground to Player

        self.bg_sound = pygame.mixer.Sound("C:/Users/Abhinav/Desktop/Python/code/sounds/music.wav")
        self.channel1 = pygame.mixer.Channel(0)

        self.impact_sound = pygame.mixer.Sound("C:/Users/Abhinav/Desktop/Python/code/sounds/impact.wav")
        self.channel2 = pygame.mixer.Channel(1)

        self.on_collision = False
        self.on_ground = False

    def circle_pos(self):
        return (int(self.player.player_pos.x), int(self.player.player_pos.y))

    def sound_on_impact(self):
        self.on_collision = True
        if(self.on_collision):
            self.channel2.play(self.impact_sound)

    def bg_music(self):
        self.channel1.play(self.bg_sound,loops=1)
        
        
    def run(self):
        last_time = time.time()
        self.bg_music()

        while True:
            delta_time = time.time() - last_time
            last_time = time.time()

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Key Handling
            keys = pygame.key.get_pressed()

            self.player.player_movements(delta_time, keys)

            # Drawing
            self.display_surface.fill("black")
            pygame.draw.circle(self.display_surface, self.color, self.circle_pos(), CIRCLE_RADIUS)
            pygame.draw.rect(self.display_surface, "red", self.ground_rect)

            # Collision Check
            if self.ground.circle_collide_with_ground(self.player):
                if (self.on_ground != True):
                    self.sound_on_impact()
                    self.on_ground = True
                    print("Collision Happened!!!")
            else:
                self.on_ground = False

            if(self.player.player_pos.x - CIRCLE_RADIUS < 0) or (self.player.player_pos.x > (WINDOW_WIDTH - self.ground.ground_pos.x)):
                self.player.player_speed_on_x = -self.player.player_speed_on_x

            if(self.player.player_pos.y - CIRCLE_RADIUS < 0) or (self.player.player_pos.x > (WINDOW_HEIGHT - self.ground.ground_pos.y)):
                self.player.player_speed_on_y = -self.player.player_speed_on_y

            # Update Display
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
