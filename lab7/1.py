import pygame as py
import datetime

py.init()

# Initializing surface
W, H = 829, 836
screen = py.display.set_mode((W, H))
py.display.set_caption("Mickey's Clock")


# Variables
done = False
FPS = 60
clock = py.time.Clock()
angle1 = 0
angle2 = 0

main = py.image.load("images/MAIN.jpg")
right = py.image.load("images/RIGHT.jpg") # "smaller hand" minutes
left = py.image.load("images/LEFT.jpg") # seconds


# Size of the MAIN image
w = main.get_width()
h = main.get_height()
print(w, h)


# Rect
main_rect = main.get_rect(center = (W//2, H//2))
right_rect = right.get_rect(center = (W//2, H//2))
left_rect = left.get_rect(center = (W//2, H//2))


# Main loop
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    
    # Time
    time = datetime.datetime.now()
    minutes = time.minute
    seconds = time.second


    
    # Minutes
    angle1 = minutes*6
    minutesTransformed = py.transform.rotate(right, -angle1 + 90)
    rect1 = minutesTransformed.get_rect()
    rect1.center = right_rect.center

    # Seconds
    angle2 = seconds*6
    secondsTransformed = py.transform.rotate(left, -angle2 + 90)
    rect2 = secondsTransformed.get_rect()
    rect2.center = left_rect.center

    # Blit
    screen.blit(main, main_rect)
    screen.blit(minutesTransformed, rect1)
    screen.blit(secondsTransformed, rect2)
    

    py.display.update()
    clock.tick(60)