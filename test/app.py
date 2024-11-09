from pygame import *

from mazeClass import GameSprite, Player

''' colors '''
backgroud = (119, 180, 223)
white = (255, 255, 255)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(backgroud)

''' objects '''
HERO = Player('../images/hero.png', 5, win_height-80, 80, 80, 0,0) 
WALL1 = GameSprite('../images/platform2_v.png', 370, 100, 50, 400)
WALL2 = GameSprite('../images/platform2_h.png', win_width/2-win_width/3, win_height/2, 300, 50)
final_sprite = GameSprite('../images/pac-1.png', win_width - 85, win_height - 100, 80, 80)
monster = GameSprite('../images/cyborg.png', win_width - 80, 180, 80, 80)

wall_group = sprite.Group()
wall_group.add(WALL1)
wall_group.add(WALL2)

running = True
finish = True
''' game loop '''
while running: 
    if finish:
        window.fill(backgroud)
        # WALL1.reset(window)
        # WALL2.reset(window)
        wall_group.draw(window)
        HERO.reset(window)
        HERO.update(HERO, win_width, win_height, wall_group)
        final_sprite.reset(window)
        monster.reset(window)
        if sprite.collide_rect(HERO, monster):
            finish = False
            game_over = image.load('../images/game-over_1.png')
            back_gr = game_over.get_width() // game_over.get_height()
            window.fill(white)
            window.blit(transform.scale(game_over, (win_height * back_gr, win_height)), (90, 0))
        if sprite.collide_rect(HERO, final_sprite):
            finish = False
            game_over = image.load('images/thumb.jpg')
            back_gr = game_over.get_width() // game_over.get_height()
            window.fill(white)
            window.blit(transform.scale(game_over, (win_height * back_gr, win_height)), (90, 0))

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

