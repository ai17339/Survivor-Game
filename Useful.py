# Imports
import math, time, random, pygame
import Useful, Assets, Sprites

# Provides useful functions to the game
class Game():
    
    # DELTA TIME 
    delta_time = 0
    ticks_Last_Frame = 0
    def get_deltatime():
        total_ticks = pygame.time.get_ticks()
        delta_time = (total_ticks - Game.ticks_Last_Frame) / 1000.0
        Game.ticks_Last_frame = total_ticks
        return delta_time
    
    # Rotates image
    def rotate_image(sprite, angle, pivot, offset, sprite_rect):
        sprite = pygame.transform.rotate(sprite, int(angle))
        sprite_rect = sprite.get_rect(center=pivot-offset)
        return sprite, sprite_rect 
    
    # Checks if mouse is over 
    def is_over(x, y, width, height):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < (x + width) and y < mouse[1] < (y + height):
            return True
    
    # Checks if two sprites collide
    def collide_check(sprite1, s1_x, s1_y, sprite2, s2_x, s2_y):
        offset_x = int(s2_x) - int(s1_x)
        offset_y = int(s2_y) - int(s1_y)
        collide = sprite1.mask.overlap(sprite2.mask, (int(offset_x), int(offset_y)))
        if collide != None:
            return True
        else:
            return False

    # displays hit boxes of sprites
    draw_hit_box = False
    def display_hit_box():
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_p] and Game.draw_hit_box == False:
            Game.draw_hit_box = True
            time.sleep(0.2)
        elif key_pressed[pygame.K_p] and Game.draw_hit_box == True:
            Game.draw_hit_box = False 
            time.sleep(0.2)

# Randomizes variables in different zombies
class zombie_spawn():
    def spawn_point():
        spawn_point_list = []
        # Top right corner
        spawn_point_list.append((2000, random.randint(-10, 200)))
        # Top left corner
        spawn_point_list.append((-30, random.randint(-10, 200)))
        # Bottom right corner
        spawn_point_list.append((2000, random.randint(-900, 1080)))
        # Bottom left corner
        spawn_point_list.append((-30, random.randint(900, 1080)))


        random_spawn_point = spawn_point_list[random.randint(0, len(spawn_point_list) - 1)]
        return random_spawn_point[0], random_spawn_point[1]
    
    def speed():
        # Generates a random value out of 100 to use as percentage
        random_percent = random.randint(1, 100)

        # Returns a random speed
        if random_percent >= 1 and random_percent <= 50:
            return 4
        elif random_percent >= 51 and random_percent <= 75:
            return 8
        elif random_percent >= 76 and random_percent <= 100:
            return 15
