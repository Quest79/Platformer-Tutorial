
# Constants
TITLE = "Platformer"
WIDTH, HEIGHT = 600, 800
FPS = 60
FONT = 'arial'
HS_FILE = 'highscores.txt'
SPRITESHEET = "spritesheet_jumper.png"


# Player Properties
PLAYER_ACC = .8
PLAYER_FRIC = -0.12
GRAVETY = 1.2

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKYBLUE = (135, 206, 235)


# Platforms
# (self, color="WHITE", x=0, y=0, w=100, h=10)
PLATFORM_LIST = [(GREEN, 0, HEIGHT - 32, WIDTH, 32),
                 (RED, WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (GREEN, 77, 300, 88, 20),
                 (YELLOW, WIDTH - 50, HEIGHT * 3 / 5, 55, 20),
                 (BLUE, 50, 100, 155, 20),

                 ]


# def rgb(hex):
#     h = hex.lstrip('#')
#     print(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))


# rgb(HEX)
