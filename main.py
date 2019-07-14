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
        self.player = Player()
        self.ALL_SPRITES.add(self.player)
        self.run()

    def run(self):
        # Main game loop.
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - Updates
        self.ALL_SPRITES.update()

    def events(self):
        # Game loop - Events
        for e in pg.event.get():
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                if self.playing:
                    self.playing = False
                    self.gameON = False

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
