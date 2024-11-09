from pygame import *

from mazeClass import GameSparite, Player

''' colors '''
backgroud = (119, 180, 223)


win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(backgroud)

''' objects '''
HERO = Player('images/hero.png', 5, win_height-80, 80, 80, 0,0) 
WALL1 = GameSparite('images/platform2_v.png', 370, 100, 50, 400)
WALL2 = GameSparite('images/platform2_h.png', win_width/2-win_width/3, win_height/2, 300, 50)


running = True
''' game loop '''
while running: 
    
    window.fill(backgroud)
    WALL1.reset(window)
    WALL2.reset(window)
    HERO.reset(window_=window)
    HERO.update()

    for e in event.get():

        if e.type == QUIT:
            running = False

        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                HERO.x_speed = -1
            elif e.key == K_RIGHT:
                HERO.x_speed = 1
            elif e.key == K_UP:
                HERO.y_speed = -1
            elif e.key == K_DOWN:
                HERO.y_speed = 1
        if e.type == KEYUP:
            if e.key == K_LEFT:
                HERO.x_speed = 0
            elif e.key == K_RIGHT:
                HERO.x_speed = 0
            elif e.key == K_UP:
                HERO.y_speed = 0
            elif e.key == K_DOWN:
                HERO.y_speed = 0



    display.update()

