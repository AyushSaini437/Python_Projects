import pygame
import sys

pygame.init()
from pygame.locals import *
pygame.font.init()

screen_width, screen_height = 800,600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PingPong")
clock = pygame.time.Clock()
fps = clock.get_fps()
Score1, Score2 = 0, 0

# Paddle A
def draw_paddle1(x,y):
    paddle_a =pygame.Rect(x, y, 30, 125)
    pygame.draw.rect(screen, (255, 0, 0), paddle_a)
    # pygame.display.update()

paddle_speed = 10
paddle1_x = 30
paddle1_y = 225
draw_paddle1(paddle1_x,paddle1_y)

# Paddle B
def draw_paddle2(x,y):
    paddle_a =pygame.Rect(x, y, 30, 125)
    pygame.draw.rect(screen, (255, 0, 0), paddle_a)
    # pygame.display.update()

paddle2_x = 740
paddle2_y = 225
draw_paddle2(paddle2_x,paddle2_y)

# Ball
def draw_ball(x,y):
    ball = pygame.draw.circle(screen,("Red"),(x,y),10,0)

ball_x, ball_y = 400, 300
ball_speed_x, ball_speed_y = 8, 8

# Side Collision
def sc():
    global ball_x, ball_y,Score
    if ball_x <= 0 or ball_x >= 800:
        ball_x = screen_width//2
        ball_y = screen_height//2

# Text
text_font = pygame.font.Font("PressStart2P-vaV7.ttf",10)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            paddle_x = min(paddle1_x, screen_width - 30)
            paddle_y = min(paddle1_y, screen_height - 125)
            draw_paddle1(paddle1_x, paddle1_y)

            paddle_x = min(paddle2_x, screen_width - 30)
            paddle_y = min(paddle2_y, screen_height - 125)
            draw_paddle2(paddle2_x, paddle2_y)

    keys = pygame.key.get_pressed()

    # Update paddle position based on key input
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
    # Ensure the paddle stays within the screen boundaries
    paddle1_y = max(0, min(paddle1_y, screen_height - 125))
    paddle2_y = max(0, min(paddle2_y, screen_height - 125))

    # Updating the ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Keeping the ball within the boundries
    if ball_y <= 0 or ball_y >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball_x <= 0 or ball_x >= screen_width:
        ball_speed_x = -ball_speed_x

    # Collision with paddles
    if (
        paddle1_x < ball_x < paddle1_x + 30
        and paddle1_y < ball_y < paddle1_y + 125
    ) or (
        paddle2_x < ball_x < paddle2_x + 30
        and paddle2_y < ball_y < paddle2_y + 125
    ):
        ball_speed_x = -ball_speed_x
    if ball_x == 0:
        Score2 += 1
    if ball_x == 800:
        Score1 += 1

    # Collision with right and left side of the screen
    sc()

    p1_text = text_font.render(f"Player 1: {Score1}",1,("White"))
    p2_text = text_font.render(f"Player 2: {Score2}",1,("White"))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the updated paddle
    draw_paddle1(paddle1_x, paddle1_y)
    draw_paddle2(paddle2_x, paddle2_y)
    draw_ball(ball_x, ball_y)
    screen.blit(p1_text,(350,10))
    screen.blit(p2_text,(350,580))

    pygame.display.flip()
    clock.tick(60)
