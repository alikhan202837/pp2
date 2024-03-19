import pygame as py
py.init()

W, H = 600, 400
screen = py.display.set_mode((W, H), py.RESIZABLE)
py.display.set_caption("Circle")
clock = py.time.Clock()
RED = (255,0,0)
WHITE = (255,255,255)
x, y = 25,25
speed = 20
screen.fill(WHITE)
circle = py.draw.circle(screen, RED, (x,y), 25)

while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    
    pressed = py.key.get_pressed()
    if pressed[py.K_UP]:
        y -= speed
    if pressed[py.K_DOWN]:
        y += speed
    if pressed[py.K_LEFT]:
        x -= speed
    if pressed[py.K_RIGHT]:
        x += speed

    W = screen.get_width()
    H = screen.get_height()
    
    if x < 25:
        x = 25
    if y < 25:
        y = 25
    if x > W - 25:
        x = W - 25
    if y > H - 25:
        y = H - 25


    screen.fill(WHITE)
    circle = py.draw.circle(screen, RED, (x,y), 25)
    py.display.update()
    clock.tick(60)