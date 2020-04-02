# Imports
import pygame

#########################################
# Creates lists of assests used in game #
#########################################

class color:
    COLORS = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "blackish": (30, 30, 30),
        "blue": (0, 0, 255),
        "lime": (0, 255, 0),
        "red": (255, 0, 0),
        "yellow": (255, 255, 0),
        "aqua": (0, 255, 255),
        "magenta": (255, 0, 255),
        "silver": (192, 192, 192),
        "gray": (128, 128, 128),
        "maroon": (128, 0, 0),
        "olive": (128, 128, 0),
        "green": (0, 128, 0),
        "purple": (128, 0, 128),
        "teal": (0, 128, 128),
        "navy": (0, 0, 128),
    }

class sprite_animations:
    SPRITE_STAND = [pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_0.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_1.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_2.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_3.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_4.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_5.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_6.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_7.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_8.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_9.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_10.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_11.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_12.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_13.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_14.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_15.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_16.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_17.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_18.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\idle\survivor-idle_rifle_19.png')]

    SPRITE_WALK = [pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_0.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_1.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_2.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_3.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_4.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_5.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_6.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_7.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_8.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_9.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_10.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_11.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_12.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_13.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_14.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_15.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_16.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_17.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_18.png'),
                pygame.image.load(r'Images\Top_Down_Survivor\rifle\move\survivor-move_rifle_19.png')]

    SPRITE_RELOAD = [pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_0.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_1.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_2.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_3.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_4.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_5.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_6.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_7.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_8.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_9.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_10.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_11.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_12.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_13.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_14.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_15.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_16.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_17.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_18.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\reload\survivor-reload_rifle_19.png')]

    SPRITE_SHOOT = [pygame.image.load(r'Images\Top_Down_Survivor\rifle\shoot\survivor-shoot_rifle_0.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\shoot\survivor-shoot_rifle_1.png'),
                    pygame.image.load(r'Images\Top_Down_Survivor\rifle\shoot\survivor-shoot_rifle_2.png')]

class zombie_animations:
    SPRITE_STAND = [pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_0.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_1.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_2.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_3.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_4.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_5.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_6.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_7.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_8.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_9.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_10.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_11.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_12.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_13.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_14.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_15.png'),
                    pygame.image.load(r'Images\Top_Down_Zombie\idle\skeleton-idle_16.png')]

    SPRITE_WALK = [pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_0.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_1.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_2.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_3.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_4.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_5.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_6.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_7.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_8.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_9.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_10.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_11.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_12.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_13.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_14.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_15.png'),
                pygame.image.load(r'Images\Top_Down_Zombie\move\skeleton-move_16.png')]

    SPRITE_ATTACK = [pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_0.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_1.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_2.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_3.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_4.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_5.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_6.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_7.png'),
                     pygame.image.load(r'Images\Top_Down_Zombie\attack\skeleton-attack_8.png')]

class bullet:
    SPRITE_BULLET = pygame.image.load(r'Images\Bullet\bullet-sprite-png-16.png')

class background:
    BACKGROUND_1 = pygame.image.load(r'Images\Backgrounds\background1.png')