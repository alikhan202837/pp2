import pygame as py
py.init()

# Main screen
W, H = 600, 400
screen = py.display.set_mode((W, H))
py.display.set_caption("Paint 2D")
done = False

# FPS
clock = py.time.Clock()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Setting initial color
color = BLUE

# Position of mouse when drawing figures
X = Y = 0

prev = None

# First
status = "brush"
py.mouse.set_cursor(py.cursors.diamond)

drawStarted = False
startPos = None

# Our board
screen.fill(WHITE)

while not done:
    touch = py.mouse.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_b:
                status = "brush"

            elif event.key == py.K_e:
                status = "eraser"

            # Colors
            elif event.key == py.K_1:
                color = RED
            elif event.key == py.K_2:
                color = BLUE
            elif event.key == py.K_3:
                color = GREEN
            elif event.key == py.K_4:
                screen.fill(RED)
            elif event.key == py.K_5:
                screen.fill(BLUE)
            elif event.key == py.K_6:
                screen.fill(GREEN)
            elif event.key == py.K_7:
                screen.fill(WHITE)

            # Figures
            elif event.key == py.K_p:
                status = "rectangular"
                py.mouse.set_cursor(py.cursors.arrow)
            elif event.key == py.K_c:
                status = "circle"
                py.mouse.set_cursor(py.cursors.arrow)


        #1
        if status == "brush":
            if touch[0]:
                X = py.mouse.get_pos()[0]
                Y = py.mouse.get_pos()[1]
                if prev is not None:
                    for x in range(20):
                        for y in range(20):
                            py.draw.line(screen, color, (prev[0] + x - 10, prev[1] + y - 20), 
                                         (X + x - 10, Y + y - 20))

                prev = (X, Y) 
            if event.type == py.MOUSEBUTTONUP:
                prev = None
        #2
        elif status == "eraser": 
            if touch[0]:
                X = py.mouse.get_pos()[0]
                Y = py.mouse.get_pos()[1]
                if prev is not None:
                    prevX, prevY = prev
                    for x in range(20):
                        for y in range(20):
                            py.draw.line(screen, WHITE, (prev[0] + x - 10, prev[1] + y - 20), 
                                         (X + x - 10, Y + y - 20))

                prev = (X, Y) 
            if event.type == py.MOUSEBUTTONUP:
                prev = None
        #3
        elif status == "rectangular": 
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    Pos = event.pos

                    width = Pos[0] - startPos[0]
                    height = Pos[1] - startPos[1]
                    py.draw.rect(screen, color, (startPos[0], startPos[1], width, height))

            if event.type == py.MOUSEBUTTONUP:
                drawStarted = False
        #4
        elif status == "circle":
            if event.type == py.MOUSEBUTTONDOWN:
                pos = event.pos
                py.draw.circle(screen, color, (pos[0], pos[1]), 50)

    py.display.update()
    clock.tick(60)
