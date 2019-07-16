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
from os import *


class Game:
    def __init__(self):
        # Init the game window, mixer, pygame, etc
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.gameON = True
        self.highscore = 0
        self.font_name = pg.font.match_font(FONT)

    def loadAssets(self):
        # Constants
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        snd_dir = path.join(self.dir, 'snd')
        # Try to load highscore
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # Load spritesheet
        self.spritesheet = SpriteSheet(path.join(img_dir, SPRITESHEET))

    def new(self):
        # Start new game
        self.score = 0
        self.ALL_SPRITES = pg.sprite.Group()
        self.PLATFORMS = pg.sprite.Group()
        self.player = Player(self)
        self.ALL_SPRITES.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.ALL_SPRITES.add(p)
            self.PLATFORMS.add(p)

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

        # If the player gets to 2/3 of screen
        if self.player.rect.top <= HEIGHT / 3:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.PLATFORMS:
                plat.rect.y += abs(self.player.vel.y)
                # Kill platforms as the diffapear off the bottom of the screen.
                if plat.rect.top >= HEIGHT:
                    print(len(self.PLATFORMS))
                    self.score += 10
                    plat.kill()  # Removed platform from platforms group.

        # Load more platforms when the number in the PLATFORMS group is less than 6.
        while len(self.PLATFORMS) < 6:
            width = random.randrange(64, 196)
            p = Platform(RED, random.randrange(0, WIDTH - width), random.randrange(-100, -50), width, 20)
            self.PLATFORMS.add(p)
            self.ALL_SPRITES.add(p)

        # On death
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.ALL_SPRITES:
                sprite.rect.y -= max(self.player.vel.y, 5)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.PLATFORMS) == 0:
            self.playing = False

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
        self.SCREEN.fill(SKYBLUE)
        self.ALL_SPRITES.draw(self.SCREEN)
        # Draw Score
        self.drawText(str(self.score), 30, WHITE, WIDTH / 2, 20)
        # AFTER drawining everything, flip the display.
        pg.display.flip()

    def showStart(self):
        # Show start screen
        pass

    def showEnd(self):
        # Show end screen
        pass

    def drawText(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.SCREEN.blit(text_surface, text_rect)


g = Game()
# g.showStart
while g.gameON:
    g.new()

pg.quit()
