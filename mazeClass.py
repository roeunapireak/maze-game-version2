from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height):
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

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
