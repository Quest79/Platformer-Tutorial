
import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        k = pg.key.get_pressed()
        if k[pg.K_d]:
            self.vx = 12
        if k[pg.K_a]:
            self.vx = -12

        self.rect.x += self.vx
        self.rect.y += self.vy
