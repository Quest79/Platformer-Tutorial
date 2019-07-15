
# Constants
TITLE = "Platformer"
WIDTH, HEIGHT = 600, 800
FPS = 60


# Player Properties
PLAYER_ACC = .8
PLAYER_FRIC = -0.12
GRAVETY = 1.2

# Platforms
# (self, color="WHITE", x=0, y=0, w=100, h=10)
PLATFORM_LIST = [(GREEN, 0, HEIGHT - 32, WIDTH, 32),
                 (RED, WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)]

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
