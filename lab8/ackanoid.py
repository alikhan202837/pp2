import pygame as py
from random import randrange
py.init()

# Timer
py.time.set_timer(py.USEREVENT, 5000)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Main screen
W, H = 1200, 650
screen = py.display.set_mode((W, H))
py.display.set_caption("Ackanoid Game")

# Fps
FPS = 60
clock = py.time.Clock()

# Creating a paddle
PW = 200
PH = 25
PSPEED = 20
P = py.Rect(W//2 - PW//2, H - 50, PW, PH)

# Creating a ball
BRADIUS = 20
BSPEED = 5
BRECT = py.Rect(randrange(20, 780), H//2, int(BRADIUS*(2**0.5)), int(BRADIUS*(2**0.5)))
dx = 1
dy = -1

# Game over
fontGameOver = py.font.SysFont(None, 50)
text = fontGameOver.render("GAME OVER", True, WHITE)
text_rect = text.get_rect(center = (W//2, H//2))

# No Game Over
fontWin = py.font.SysFont(None, 50)
text1 = fontWin.render("You WIN", True, WHITE)
text1_rect = text1.get_rect(center = (W//2, H//2))

# Score
game_score = 0
fontGameScore = py.font.SysFont(None,40)
game_score_text = fontGameOver.render(f"Score: {game_score}", True, WHITE)

# Sound
py.mixer.music.load("sound/catch.mp3")
# Blocks
block_list = [py.Rect(10 + 120*i, 50 + 70*j, 50,50) for i in range(10) for j in range(4)]
color_list = [(randrange(0,255), randrange(0,255), randrange(0,255)) for i in range(10) for j in range(4)]


#
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        elif event.type == py.USEREVENT:
            BSPEED += 1
    
    
    game_score_text = fontGameOver.render(f"Score: {game_score}", True, WHITE)

    # Output
    screen.fill(BLACK)
    [py.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    screen.blit(game_score_text, (0,0))
    py.draw.rect(screen, (255,0,40), P)
    py.draw.circle(screen, (0,255,129), BRECT.center, BRADIUS)

    # Motion of PADDLE
    pressed = py.key.get_pressed()
    if pressed[py.K_d] and P.right < W:
        P.centerx += PSPEED
    if pressed[py.K_a] and P.left > 0:
        P.centerx -= PSPEED
    
    # Motion of ball
    BRECT.x += BSPEED * dx
    BRECT.y += BSPEED * dy

    if BRECT.left < 0 or BRECT.right > W:
        dx = -dx
    if BRECT.top < 50:
        dy = -dy
    if P.colliderect(BRECT) and dy > 0:
        dy = -dy
        
    # Collisions with blocks
    hitted = BRECT.collidelist(block_list)

    if hitted != -1:
        game_score += 1
        py.mixer.music.play(1)
        hittedRect = block_list.pop(hitted)
        hittedColor = color_list.pop(hitted)
        dx, dy = detect_collision(dx, dy, BRECT, hittedRect)

    # WIN or LOSE
    if BRECT.bottom > H:
        screen.fill(BLACK)
        screen.blit(text, text_rect)
    if not len(block_list):
        screen.fill(BLACK)
        screen.blit(text1, text1_rect)
    
    py.display.update()
    clock.tick(60)