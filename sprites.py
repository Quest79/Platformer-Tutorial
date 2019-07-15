
import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game # Allows Player class to see Game class via Player(self) in main.py run(). Used in Jump() below.
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # Check to see if on a playform, then jump if yes.
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.PLATFORMS, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -25

    def update(self):
        self.acc = vec(0, GRAVETY)
        k = pg.key.get_pressed()
        if k[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if k[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        # if k[pg.K_SPACE]:
        #     self.acc.y = PLAYER_ACC
        # # if k[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC

        # Super cool friction code using vectors with velocity & acceleration vars
        # Written in 3 lines but can be one. Easier to read in 3.
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Set the center of the sprite to the new .pos position calculated above.
        self.rect.midbottom = self.pos

        # Lets wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # if self.pos.y > HEIGHT:
        #     self.pos.y = 0
        # if self.pos.y < 0:
        #     self.pos.y = HEIGHT


class Platform(pg.sprite.Sprite):
    def __init__(self, color="WHITE", x=0, y=0, w=100, h=10):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
