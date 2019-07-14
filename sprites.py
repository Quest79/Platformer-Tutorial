
import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        k = pg.key.get_pressed()
        if k[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if k[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if k[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if k[pg.K_w]:
            self.acc.y = -PLAYER_ACC

        # Super cool friction code using vectors with velocity & acceleration vars
        # Written in 3 lines but can be one. Easier to read in 3.
        self.acc += self.vel * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Lets wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.center = self.pos
