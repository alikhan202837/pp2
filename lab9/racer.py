import pygame as py
from random import randrange, choice
import time

py.init()

# Icreasing speed by time
INC_SPEED = py.USEREVENT
py.time.set_timer(INC_SPEED, 2000)


# Main screen
W, H = 400, 600
screen = py.display.set_mode((W, H))
py.display.set_caption("Forza Horizon 6")
done = False

# Background
back = py.image.load("images/bg.png")

# FPS
clock = py.time.Clock()
FPS = 60

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating font
f = py.font.SysFont(None, 50) # default phyton font

# SPEED and SCORE of enemies and player respectively
SPEED = 7
SCORE = 0

# Class 1
class Player(py.sprite.Sprite):
    def __init__(self, image):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.rect = self.image.get_rect(center = (160,520))
    def move(self):
        pressed = py.key.get_pressed()
        if pressed[py.K_w] and self.rect.top > 0:
            self.rect.top -= 10
        if pressed[py.K_s] and self.rect.bottom < H:
            self.rect.bottom += 5
        if pressed[py.K_a] and self.rect.left > 0:
            self.rect.left -= 10
        if pressed[py.K_d] and self.rect.right < W:
            self.rect.right += 10

# Class 2
class Enemy(py.sprite.Sprite):
    def __init__(self, image):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.rect = self.image.get_rect(center = (randrange(40, W - 40), 0)) #initial position
    def move(self):
        self.rect.bottom += SPEED
        if self.rect.top > H:
            self.rect.bottom = 0
            self.rect.center = (randrange(20, 380), 0)



# Class 3
class Coin(py.sprite.Sprite):
    def __init__(self, image, group):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.image = py.transform.scale(self.image, (30,30)) # changing width and height
        self.rect = self.image.get_rect(center = (randrange(20,380), 0))
        self.add(group)
    def move(self):
        self.rect.bottom += 5
        if self.rect.top > H:
            self.kill()

# Class 4
class SpecialCoin(py.sprite.Sprite):
    def __init__(self, image, group):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.rect = self.image.get_rect(center = (randrange(20, 380), 0))
        self.add(group)
    def move(self):
        self.rect.bottom += 5
        if self.rect.top > H:
            self.kill()



# Creating cars
P1 = Player("images/Player.png")
E1 = Enemy("images/Enemy.png")


# Creating group
enemies = py.sprite.Group()
coins = py.sprite.Group()
allSprites = py.sprite.Group()
specialCoins = py.sprite.Group()

enemies.add(E1)
allSprites.add(E1)
allSprites.add(P1) 


# Creating sound
soundList = ["sound/crash.wav", "sound/background.wav"]
py.mixer.music.load(soundList[1])
py.mixer.music.play(-1)

# Creating new coins
def createCoin():
    return Coin("images/coin.png", coins)

def createSpecialCoin():
    return Coin("images/super_coin.png", specialCoins)

# Collision and game over
def collideCar():
    for enemy in enemies:
        if P1.rect.colliderect(enemy.rect):
            # Sound
            py.mixer.music.load(soundList[0])
            py.mixer.music.play(1)
            time.sleep(1)

            # Creating text to game over
            text1 = f.render(f"GAME OVER", True, WHITE)
            text2 = f.render(f"Your score is {SCORE}", True, WHITE)
            
            # Game over
            screen.fill(RED)
            screen.blit(text1, (85,H//2))
            screen.blit(text2, (65, H//2 + 50))
            py.display.update()

            # Cleaning
            for all in allSprites:
                all.kill()
            time.sleep(2)
            exit()


def collideCoin():
    global SCORE
    for coin in coins:
        if P1.rect.colliderect(coin.rect):
            SCORE += 1
            coin.kill()

def collideSpecialCoin():
    global SCORE
    for scoin in specialCoins:
        if P1.rect.colliderect(scoin.rect):
            SCORE += 5
            scoin.kill()

# Main loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        if event.type == INC_SPEED:
            if SCORE%2 == 0 and SCORE > 9:
                SPEED += 1
                
            x = choice([1,2])
            if x == 1:
                createSpecialCoin()
            else:
                createCoin()
            

    # Checking for collision
    collideCar()
    collideCoin()
    collideSpecialCoin()

    # Creating text for score
    text3 = f.render(f"{SCORE}", True, GREEN)

    # Output
    screen.blit(back, (0,0)) # background
    screen.blit(text3, (6,3)) # score
    for sprite in allSprites:
        screen.blit(sprite.image, sprite.rect) # player, enemies
        sprite.move()
    for coin in coins:
        screen.blit(coin.image, coin.rect)
        coin.move()
    for scoin in specialCoins:
        screen.blit(scoin.image, scoin.rect)
        scoin.move()
    py.display.update()
    clock.tick(FPS)