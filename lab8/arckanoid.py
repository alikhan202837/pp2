"""
bonus +10 points
"""

import pygame
from random import randrange, choice
pygame.init()

# Timer
pygame.time.set_timer(pygame.USEREVENT, 5000)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Main screen
W, H = 1200, 650
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Arckanoid Game")

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
fontGameOver = pygame.font.SysFont(None, 50)
text = fontGameOver.render("GAME OVER", True, WHITE)
text_rect = text.get_rect(center = (W//2, H//2))

# No Game Over
fontWin = pygame.font.SysFont(None, 50)
text1 = fontWin.render("You WIN", True, WHITE)
text1_rect = text1.get_rect(center = (W//2, H//2))

# Score
game_score = 0
fontGameScore = pygame.font.SysFont(None,40)
game_score_text = fontGameOver.render(f"Score: {game_score}", True, WHITE)

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            BSPEED += 0.5
            PW -= 10
    
    game_score_text = fontGameOver.render(f"Score: {game_score}", True, WHITE)

    P = pygame.Rect(X, H - 50, PW, PH)

    # Output
    screen.fill(BLACK)
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] # drawing blocks
    [pygame.draw.rect(screen, (255,255,255), unbreakable_block)
     for unbreakable_block in (unbreakable_list)]
    screen.blit(game_score_text, (0,0)) # game score
    pygame.draw.circle(screen, (0,255,129), BRECT.center, BRADIUS) # ball
    pygame.draw.rect(screen, (255,0,40), P) # paddle
    
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
    if BRECT.top < 50:
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

    # WIN or LOSE
    if BRECT.bottom > H:
        screen.fill(BLACK)
        screen.blit(text, text_rect)
    if len(block_list) == 3:
        screen.fill(BLACK)
        screen.blit(text1, text1_rect)
    
    pygame.display.update()
    clock.tick(60)