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

#Display of tools
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
py.draw.rect(toolSC, BLACK, rectangle, 5)
#circle
circle = py.Rect(496, 20, 40, 40)
py.draw.circle(toolSC, BLACK, circle.center, 20, 5)
#brush
brush_text = font.render("BRUSH", True, BLACK)
brush_text_rect = brush_text.get_rect(topleft = (556, 30))
toolSC.blit(brush_text, brush_text_rect)
#rhombus
rhombus = py.Rect(666, 20, 40, 40)
py.draw.polygon(toolSC, BLACK, [(686, 20), (666, 40), (686, 60), (706, 40)], 5)
#triangle
triangle = py.Rect(726, 20, 40, 40)
py.draw.polygon(toolSC, BLACK, [(746, 20), (726, 60), (766, 60)], 5)
#triangle90
triangle90 = py.Rect(786, 20, 40, 40)
py.draw.polygon(toolSC, BLACK, [(786, 20), (786, 60), (826, 60)], 5)
#Initial settings
colorOfBrush = BLUE
status = "brush"
size = 10
drawStarted = False
startPos = (0,0)
top = left = right = bottom = (0,0)

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
            if rhombus.collidepoint(posMouse):
                status = "rhombus"
            if triangle.collidepoint(posMouse):
                status = "triangle"
            if triangle90.collidepoint(posMouse):
                status = "triangle90"

        #output
        # 1
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
                                min(pos[1],startPos[1]), width, height))
                    
            if event.type == py.MOUSEBUTTONUP:
                drawStarted = False
        # 2
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
        # 3
        if status == "rhombus":
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = (startPos[0] + abs(startPos[0] - pos[0]) / 2, startPos[1])
                    bottom = (startPos[0] + abs(startPos[0] - pos[0]) / 2, pos[1])
                    right = (pos[0], startPos[1] + abs(startPos[1] - pos[1]) / 2)
                    left = (startPos[0], startPos[1] + abs(startPos[1] - pos[1]) / 2)

            if event.type == py.MOUSEBUTTONUP:
                py.draw.polygon(screen, colorOfBrush, [top, right, bottom, left])
                drawStarted = False
        # 4
        if status == "triangle":
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = (startPos[0] + abs(startPos[0] - pos[0])/2, startPos[1])
                    left = (startPos[0], pos[1])
                    right = (pos[0], pos[1])
                    

            if event.type == py.MOUSEBUTTONUP:
                py.draw.polygon(screen, colorOfBrush, [top, left, right])
                drawStarted = False
        # 5
        if status == "triangle90":
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == py.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = startPos
                    left = (startPos[0], pos[1])
                    right = (pos[0],pos[1])
            
            if event.type == py.MOUSEBUTTONUP:
                py.draw.polygon(screen, colorOfBrush, [top, left, right])
                drawStarted = False

    screen.blit(toolSC, (0,0))             
    py.display.update()
    clock.tick(FPS)