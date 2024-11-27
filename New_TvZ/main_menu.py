import pygame
from pygame.locals import *
import sys
import new_game

pygame.font.init()
pygame.mixer.init()

gui_font = pygame.font.Font("Font/MyGirlIsRetro-0Grz.ttf", 50)
starting_sound = pygame.mixer.Sound("Sound/mixkit-arcade-retro-background-219.wav")
starting_sound.set_volume(0.7)


class Button:
    def __init__(self,text,width,height,pos):
        # 1_top_rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = "Red"

        #text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)


    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

fps = clock.get_fps()

# Screen
screen = pygame.display.set_mode((1300, 650))
pygame.display.set_caption("Traffic vs Zombie")
button1 = Button("Play", 200,40,(400,325))
button2 = Button("Quit", 200,40,(700,325))


#Game Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 represents the left mouse button
            # Check for collision with button2 and button1
            if button2.top_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if button1.top_rect.collidepoint(event.pos):
                starting_sound.play()
                new_game.main()

        # To get mouse position
        mouse_pos = pygame.mouse.get_pos()

        if button2.top_rect.collidepoint(mouse_pos):
            button2.top_color = "Green"
        else:
            button2.top_color = "Red"

        if button1.top_rect.collidepoint(mouse_pos):
            button1.top_color = "Green"
        else:
            button1.top_color = "Red"


    screen.fill((0,0,0))
    button1.draw()
    button2.draw()
    pygame.display.update()
    clock.tick(60)
