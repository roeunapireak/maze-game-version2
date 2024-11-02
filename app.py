from pygame import *
from mazeClass import GameSprite, Player

''' colors '''
background = (119, 180, 223)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(background)

''' characters '''
HERO = Player('images/hero.png', 5, win_height-80, 80,80, 0, 0)
WALL1 = GameSprite('images/platform2_v.png', 370, 100, 50, 400)
WALL2 = GameSprite('images/platform2_h.png', win_width/2-win_width/3, win_height/2, 300, 50)

running = True

while running:
    
    window.fill(background)

    HERO.reset(window)
    WALL1.reset(window)
    WALL2.reset(window)

    for e in event.get():
        if e.type == QUIT:
            running = False 
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                HERO.x_speed = -1
            elif e.key == K_RIGHT:
                HERO.x_speed = 1
            elif e.key == K_UP:
                HERO.y_speed = -1
            elif e.key == K_DOWN:
                HERO.y_speed = 1
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                HERO.x_speed = 0
            elif e.key == K_RIGHT:
                HERO.x_speed = 0
            elif e.key == K_UP:
                HERO.y_speed = 0
            elif e.key == K_DOWN:
                HERO.y_speed = 0
    HERO.update()

    display.update()