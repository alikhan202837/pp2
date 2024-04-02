import pygame as py
py.init()

#Setting font
font = py.font.SysFont(None, 40)
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
LIGHTBLUE = (0,255,255)
#Main screen
W, H = 1000, 600
screen = py.display.set_mode((W, H))
py.display.set_caption("PAINT 2D")
done = False
#FPS
clock = py.time.Clock()
FPS = 60

#Display
toolSC = py.Surface((W, 80))
toolSC.fill("gray")
#Buttons
redR = py.Rect(0, 0, 40, 40)
blueR = py.Rect(0,40,40,40)
greenR = py.Rect(40,0,40,40)
yellowR = py.Rect(40,40,40,40)
lgblueR = py.Rect(80,0,40,40)
blackR = py.Rect(80,40,40,40)
py.draw.rect(toolSC, RED, redR)
py.draw.rect(toolSC, BLUE, blueR)
py.draw.rect(toolSC, GREEN, greenR)
py.draw.rect(toolSC, YELLOW, yellowR)
py.draw.rect(toolSC, LIGHTBLUE, lgblueR)
py.draw.rect(toolSC, BLACK, blackR)
R = [redR, blueR, greenR, yellowR, lgblueR, blackR]
C = [RED, BLUE, GREEN, YELLOW, LIGHTBLUE, BLACK]
#Eraser
erase_text = font.render("ERASER", True, BLACK)
erase_text_rect = erase_text.get_rect(topleft = (120, 30))
toolSC.blit(erase_text, erase_text_rect)
#Size of brush
brush10 = py.Rect(276, 32, 20, 20)
py.draw.circle(toolSC, BLACK, brush10.center, 10)
brush15 = py.Rect(316, 25, 30, 30)
py.draw.circle(toolSC, BLACK, brush15.center, 15)
brush20 = py.Rect(366, 18, 40, 40)
py.draw.circle(toolSC, BLACK, brush20.center, 20)
B = [brush10, brush15, brush20]
S = [10,15,20]
#rectangle
rectangle = py.Rect(436, 20, 40, 40)
py.draw.rect(toolSC, BLACK, rectangle, 1)
#circle
circle = py.Rect(496, 20, 40, 40)
py.draw.circle(toolSC, BLACK, circle.center, 20, 1)
#brush
brush_text = font.render("BRUSH", True, BLACK)
brush_text_rect = brush_text.get_rect(topleft = (556, 30))
toolSC.blit(brush_text, brush_text_rect)

#Initial settings
colorOfBrush = BLUE
status = "brush"
size = 10
drawStarted = False
startPos = (0,0)
ChangingMode = False

#Board
screen.fill(WHITE)


#Main loop
while not done:
    touch = py.mouse.get_pressed()
    posMouse = py.mouse.get_pos()
    if posMouse[1] < 80:
        py.mouse.set_cursor(py.cursors.arrow)
    else:
        py.mouse.set_cursor(py.cursors.diamond)

    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        #Changing mode and color
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            #for colors
            for i in range(len(R)):
                if R[i].collidepoint(posMouse):
                    colorOfBrush = C[i]
            #for eraser
            if erase_text_rect.collidepoint(posMouse):
                colorOfBrush = WHITE
                size = 20
                status = "brush"
            #for change size
            for i in range(len(B)):
                if B[i].collidepoint(posMouse):
                    size = S[i]
            #for rectangle, circle, brush
            if rectangle.collidepoint(posMouse):
                status = "rectangle"
            if circle.collidepoint(posMouse):
                status = "circle"
            if brush_text_rect.collidepoint(posMouse):
                status = "brush"

        #output
        if status == "brush":
            if event.type == py.MOUSEMOTION:
                if touch[0]:
                    py.draw.circle(screen, colorOfBrush, (posMouse), size)
                    
        if status == "rectangle":
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    width = abs(pos[0] - startPos[0])
                    height = abs(pos[1] - startPos[1])
                    py.draw.rect(screen, colorOfBrush, (min(pos[0],startPos[0]), 
                                min(pos[1],startPos[1]), width, height) )
                    
            if event.type == py.MOUSEBUTTONUP:
                drawStarted = False
        if status == "circle":
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    radius = abs(pos[0] - startPos[0])
                    py.draw.circle(screen, colorOfBrush, startPos, radius)

            if event.type == py.MOUSEBUTTONUP:
                drawStarted = False

    screen.blit(toolSC, (0,0))             
    py.display.update()
    clock.tick(FPS)