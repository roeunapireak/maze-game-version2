from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(picture), (width, height))

        self.rect = self.image .get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self, window_):
        window_.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, picture, x, y, width, height, x_speed, y_speed):
        GameSprite.__init__(self, picture, x, y, width, height)

        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self, hero, window_width, window_height, object_group):
        if hero.rect.x <= window_width-80 and hero.x_speed > 0 or hero.rect.x >= 0 and hero.x_speed < 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self, object_group, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)

        if hero.rect.y <= window_height-80 and hero.y_speed > 0 or hero.rect.y >= 0 and hero.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, object_group, False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
            elif self.y_speed < 0:
                for p in platforms_touched:
                    self.rect.top = max(self.rect.top, p.rect.bottom)

class Enemy(GameSprite):
    def __init__(self, picture, x,y, width,height, speed):
        GameSprite.__init__(self, picture, x,y, width,height)
        self.speed = speed
    
    direction = 'left'

    def update(self, window_width):
        if self.rect.x <= 430:
            self.direction = 'right'
        elif self.rect.x >= window_width - 70:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, picture, x,y, width,height, speed):
        GameSprite.__init__(self, picture, x,y, width,height)
        self.speed = speed

    def update(self, window_width):
        self.rect.x += self.speed
        if self.rect.x > window_width + 250:
            self.kill()