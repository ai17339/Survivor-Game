# Imports
import os, pygame

import Assets

#######################################################
# Creates constant variables used over multiple files #
#######################################################

# initialize the pygame module
pygame.init()
pygame.mixer.set_num_channels(30)

# Surface
pygame.display.set_caption("Survivor")

# Screen 
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 30'
S_WIDTH = 1920
S_HEIGHT = 1050
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

# Lists
BULLETS = []
ZOMBIES = []
PLAYER = []
ZOMBIE_DROPS = []
BULLETS_FIRED_LIST = []

# Round count
round_count = 0 
old_round_count = 0

# Zombie count
zombie_count = 0

# Bullet count
bullets_fired = 0

# Assets
COLORS = Assets.color.COLORS

# Sprite Animations
SPRITE_STAND = Assets.sprite_animations.SPRITE_STAND
SPRITE_WALK = Assets.sprite_animations.SPRITE_WALK
SPRITE_RELOAD = Assets.sprite_animations.SPRITE_RELOAD
SPRITE_SHOOT = Assets.sprite_animations.SPRITE_SHOOT

# Gun Sounds
GUNSHOT_SOUND = pygame.mixer.Sound(r'Sounds\gunshot.wav')
GUNSHOT_SOUND2 = pygame.mixer.Sound(r'Sounds\gunshot3.wav')
RELOAD_SOUND = pygame.mixer.Sound(r'Sounds\reload.wav')

#pygame
KEY_PRESSED = pygame.key.get_pressed()
MOUSE_POS = pygame.mouse.get_pos()
CLOCK = pygame.time.Clock()