# ################################################# #
# Author: Paul Duncan 2019 July 10
# Tutorial used: https://www.youtube.com/playlist?list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw
# Sprites used: https://opengameart.org/content/space-shooter-redux
# ################################################# #
# Import needed libraries.
# ################################################# #
import pygame as pg
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # Init the game window, mixer, pygame, etc
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.gameON = True

    def new(self):
        # Start new game
        self.ALL_SPRITES = pg.sprite.Group()
        self.PLATFORMS = pg.sprite.Group()
        self.player = Player(self)
        p1 = Platform(GREEN, 0, HEIGHT - 32, WIDTH, 32)
        p2 = Platform(RED, WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.ALL_SPRITES.add(p1)
        self.PLATFORMS.add(p1)
        self.ALL_SPRITES.add(p2)
        self.PLATFORMS.add(p2)
        self.ALL_SPRITES.add(self.player)

        # Lets run the game
        self.run()

    def run(self):
        # Main game loop.
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw()

    def update(self):
        # Game loop - Updates
        self.ALL_SPRITES.update()

        # Collide conditionals
        # Check if hitting playform while falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.PLATFORMS, False)
            if hits:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top
                # self.player.vel.x *= 0.5

    def events(self):
        # Game loop - Events
        for e in pg.event.get():
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                if self.playing:
                    self.playing = False
                self.gameON = False
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.player.jump()

    def draw(self):
        # Game loop - Draw
        # Draw / Render
        self.SCREEN.fill(BLACK)
        self.ALL_SPRITES.draw(self.SCREEN)
        # AFTER drawining everything, flip the display.
        pg.display.flip()

    def showStart(self):
        # Show start screen
        pass

    def showEnd(self):
        # Show end screen
        pass


g = Game()
# g.showStart
while g.gameON:
    g.new()

pg.quit()
