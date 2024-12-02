import pygame, sys, time
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


class Player:
    def __init__(self, ground):
        self.player_pos = pygame.Vector2(PLAYER_ORIGINAL_POS_X, PLAYER_ORIGINAL_POS_Y)
        self.player_speed_on_x = PLAYER_SPEED_ON_X
        self.player_speed_on_y = PLAYER_SPEED_ON_Y
        self.jump_strength = JUMP_STRENGHT
        self.ground = ground  # Reference to Ground
        self.player_rect = pygame.Rect(self.player_pos.x, self.player_pos.y, CIRCLE_DIAMETER, CIRCLE_DIAMETER)

    def player_movements(self, delta_time, keys):
        self.direction = pygame.Vector2(0, 0)

        # Horizontal Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x -= 1 * self.player_speed_on_x

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x += 1 * self.player_speed_on_x

        # Vertical Movement (Simulating Gravity + Jump)
        if keys[pygame.K_SPACE]:
            self.direction.y -= self.jump_strength * self.player_speed_on_y * .16
        else:
            self.direction.y += self.jump_strength * self.player_speed_on_y * delta_time * 2

        # Update Position
        self.player_pos.x += self.direction.x * self.player_speed_on_x * delta_time * 2
        self.player_pos.y += self.direction.y * self.player_speed_on_y * delta_time * 2

        # Debug Position
        print(f"Player Position: {self.player_pos}")

        # Keep Player Within Window Boundaries
        self.player_pos.x = max(CIRCLE_RADIUS, min(WINDOW_WIDTH - CIRCLE_RADIUS, self.player_pos.x))
        self.player_pos.y = max(CIRCLE_RADIUS, min(self.ground.ground_pos.y - CIRCLE_RADIUS, self.player_pos.y))

        if(self.direction.length() > 100):
            self.direction = self.direction.normalize()

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
        tolerance = 2

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
            # if self.ground.circle_collide_with_ground(self.player):
            #     self.player.player_jump(delta_time)
            #     self.sound_on_impact()
            #     self.on_collision = False
            #     print("COllision Happened!!!")

            if(self.ground_rect.colliderect(self.player.player_rect.bottom)):
                print("Collision Happened!!!")

            # Update Display
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
