"""
bonus +10 points
"""

import pygame
from random import randrange, choice
import time
pygame.init()

# Timer
pygame.time.set_timer(pygame.USEREVENT, 5000)

# font
font = pygame.font.SysFont(None, 50)
fontMenu = pygame.font.SysFont(None, 80)
# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Main display
W, H = 1200, 650
display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Arckanoid Game")

# Main menu
menu = pygame.Surface((W, H))
pause = False
menu_text = fontMenu.render("MENU", True, WHITE)
menu_rect = menu_text.get_rect(center = (W//2, 200))
settings_text = font.render("SETTINGS", True, WHITE)
settings_rect = settings_text.get_rect(center = (W//2, 300))
continue_text = font.render("CONTINUE", True, WHITE)
continue_rect = continue_text.get_rect(center = (W//2, 400))

menu.blit(menu_text, menu_rect)
menu.blit(settings_text, settings_rect)
menu.blit(continue_text, continue_rect)

settingsPRESSED = False

# Main screen
screen = pygame.Surface((W, H))

# Fps
FPS = 60
clock = pygame.time.Clock()

# Creating a paddle
PW = 200
PH = 25
PSPEED = 20
P = pygame.Rect(W//2 - PW//2, H - 50, PW, PH)
X = W//2 - PW//2

# Creating a ball
BRADIUS = 20
BSPEED = 5
BRECT = pygame.Rect(randrange(20, 780), H//2, int(BRADIUS*(2**0.5)), int(BRADIUS*(2**0.5)))
dx = choice([-1,1]) # direction x
dy = 1 # direction y

# Game over
text = font.render("GAME OVER", True, WHITE)
text_rect = text.get_rect(center = (W//2, H//2))

# No Game Over
text1 = font.render("You WIN", True, WHITE)
text1_rect = text1.get_rect(center = (W//2, H//2))

# Score
game_score = 0
fontGameScore = pygame.font.SysFont(None,40)
game_score_text = font.render(f"Score: {game_score}", True, WHITE)

# Sound
pygame.mixer.music.load("sound/catch.mp3")
# Blocks
block_list = [pygame.Rect(10 + 120*i, 50 + 70*j, 50,50) for i in range(10) for j in range(4)]
color_list = [(randrange(20,250), randrange(20,250), randrange(20,250)) for i in range(10) for j in range(4)]
unbreakable_list = []
for i in range(3):
    x = choice(block_list)
    unbreakable_list.append(x)
bonus_block = choice(block_list)

# collision with block
def detect_collision(dx, dy, ball, block):
    if dx > 0:
        delta_x = ball.right - block.left
    else:
        delta_x = block.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - block.top
    else:
        delta_y = block.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

while True:
    posMouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = True
        elif event.type == pygame.USEREVENT:
            BSPEED += 0.5
            if PW >= 50:
                PW -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if continue_rect.collidepoint(posMouse):
                pause = False
            if settings_rect.collidepoint(posMouse):
                settingsPRESSED = not settingsPRESSED
                if settingsPRESSED:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)


    game_score_text = font.render(f"Score: {game_score}", True, WHITE)

    P = pygame.Rect(X, H - 50, PW, PH)

    # Output
    if not pause:
        screen.fill(BLACK)
        [pygame.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (block_list)] # drawing blocks
        [pygame.draw.rect(screen, (255,255,255), unbreakable_block)
        for unbreakable_block in (unbreakable_list)]
        screen.blit(game_score_text, (0,0)) # game score
        pygame.draw.circle(screen, (0,255,129), BRECT.center, BRADIUS) # ball
        pygame.draw.rect(screen, (255,0,40), P) # paddle
        display.blit(screen, (0,0))

        # Motion of PADDLE
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d] and P.right < W:
            X += PSPEED
        if pressed[pygame.K_a] and P.left > 0:
            X -= PSPEED
        # Motion of ball
        BRECT.x += BSPEED * dx
        BRECT.y += BSPEED * dy
        # Collision with walls and paddle
        if BRECT.left < 0 or BRECT.right > W:
            dx = -dx
        if BRECT.top < 20:
            dy = -dy
        if P.colliderect(BRECT) and dy > 0:
            dy = -dy
            
        # Collisions with blocks
        hitted = BRECT.collidelist(block_list)

        # Check for bonus
        if block_list[hitted] == bonus_block:
            game_score += 10
            
        # Check for unbreakable
        unbreakable = False
        index = None
        for i in range(3):
            if block_list[hitted] == unbreakable_list[i]:
                unbreakable = True
                index = i
        if unbreakable:
            dx, dy = detect_collision(dx,dy, BRECT, unbreakable_list[index])

        if hitted != -1 and not unbreakable:
            game_score += 1
            pygame.mixer.music.play(1)
            hittedRect = block_list.pop(hitted)
            hittedColor = color_list.pop(hitted)
            dx, dy = detect_collision(dx, dy, BRECT, hittedRect)

    else:
        display.blit(menu, (0,0))
    
    # WIN or LOSE
    if BRECT.bottom > H:
        display.fill(BLACK)
        display.blit(text, text_rect)
    if len(block_list) == 3:
        display.fill(BLACK)
        display.blit(text1, text1_rect)

    pygame.display.update()
    clock.tick(60)