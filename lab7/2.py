# S - Start 
# LEFT - next music
# RIGHT - previous music
# SPACE - pause
# UP, DOWN - change volume 

import pygame as py

py.init()

screen = py.display.set_mode((600,400))
py.display.set_caption("MP3")

jan_khalib_path = r"C:\Users\Asus\Desktop\pp2\lab7\sound\1.mp3"
miyagi_path = r"C:\Users\Asus\Desktop\pp2\lab7\sound\2.mp3"
weeknd_path = r"C:\Users\Asus\Desktop\pp2\lab7\sound\3.mp3"
kairosh_path = r"C:\Users\Asus\Desktop\pp2\lab7\sound\4.mp3"



apple_music = [jan_khalib_path, miyagi_path, weeknd_path, kairosh_path]

volume = 1
clock = py.time.Clock()
FPS = 60
pause = False
i = 0
started = False

while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()

        elif event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                volume -= 0.1
                py.mixer.music.set_volume(volume)

            elif event.key == py.K_UP:
                volume += 0.1
                py.mixer.music.set_volume(volume)

            elif event.key == py.K_SPACE and started:
                pause = not pause
                if pause:
                    py.mixer.music.pause()
                else:
                    py.mixer.music.unpause()
            
            elif event.key == py.K_RIGHT and started:
                i += 1
                if i == len(apple_music): 
                    i = 0 

                py.mixer.music.load(apple_music[i])
                py.mixer.music.play(-1)

            elif event.key == py.K_LEFT and started:
                i -= 1
                if i == -1: 
                    i = len(apple_music) - 1
 
                py.mixer.music.load(apple_music[i])
                py.mixer.music.play(-1)

            elif event.key == py.K_s:
                py.mixer.music.load(apple_music[0])
                py.mixer.music.play(-1)
                started = True
            

    py.display.update()
    clock.tick(FPS)