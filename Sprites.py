# Imports
import math, time, random, pygame
import Useful, Assets, Sprites
from Constants import*
from pygame.math import Vector2

# SMALL CLASSES ##############################################################################################################################
# ############################################################################################################################################

# Text
class Text:
    def draw_text(text, size, color, surface, x, y):
        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, 1, color)
        if x == 'centered':
            x = (S_WIDTH / 2) - (label.get_width() / 2)
        else:
            x = x
        surface.blit(label, (x, y))

# Drops valuable items to player when the kill zombies
class zombie_drop:
    def __init__(self, zombie_x, zombie_y):
        # Time keeper 
        self.time = 0
        self.finished = False
        self.x = zombie_x
        self.y = zombie_y

        # Type of drop
        self.health_drop = False
        self.bullet_drop = False 

        # Generates a random value out of 100 to use as percentage
        self.random_percent = random.randint(1, 100)

        # Randomizes player drops
        for player in PLAYER:
            
            # No drop
            if self.random_percent >= 1 and self.random_percent <= 50:
                return None  

            # Bullet drop
            elif self.random_percent >= 51 and self.random_percent <= 75 and player.BULLETS_LEFT != 400:
                self.bullet_drop = True
                if player.BULLETS_LEFT <= 370:
                    player.BULLETS_LEFT += 30
                else:
                    player.BULLETS_LEFT = 400

            # Health drop
            elif self.random_percent >= 76 and self.random_percent <= 100 and player.health != 100:
                if player.health > 90:
                    player.health = 100 
                else:
                    player.health += 10  
                    self.health_drop = True 

    def drop(self):
        if self.health_drop == True:
            text_displayed = Text.draw_text("+10 HP" , 20, COLORS["red"], SCREEN, self.x, self.y)
        if self.bullet_drop == True:
            text_displayed = Text.draw_text("+30 Bullets" , 20, COLORS["yellow"], SCREEN, self.x, self.y)

        # Displays drop on screen for two seconds
        self.time += Useful.Game.delta_time
        if self.time >= 2:
            self.finished = True 

# Menu sprite
class menu_sprite():
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y
        # Rotation
        self.angle = 0
        self.rotation_offset = Vector2(-60, 15)
        # Sprite
        self.current_sprite = SPRITE_STAND[0]
        self.sprite_rect = 0,0
    
    def update(self):
        # Updates angle
        self.angle += 2
        if self.angle >= 360:
            self.angle = 0

        # Updates sprite 
        self.current_sprite = SPRITE_STAND[0]

        # Rotates sprite
        rotation_pivot = (self.x, self.y)
        rotation_offset_rotated = self.rotation_offset.rotate(-self.angle)
        rotated = Useful.Game.rotate_image(self.current_sprite, self.angle, rotation_pivot, rotation_offset_rotated, self.sprite_rect)
        self.current_sprite = rotated[0]
        self.sprite_rect = rotated[1]
        
        # Blits sprite
        SCREEN.blit(self.current_sprite, self.sprite_rect)


# Main classes ###############################################################################################################################
# ############################################################################################################################################

# Button class ###############################################################################################################################
class Button(pygame.sprite.DirtySprite):
    def __init__(self, box_color, box_color2, box_color3, text_color, text_color2, text_color3, border_color, x, y,
                 width, height, text_size, border_size, text='', border=None):
        pygame.sprite.DirtySprite.__init__(self)
        # Box colors for different states
        self.box_color = box_color
        self.box_color2 = box_color2
        self.box_color3 = box_color3
        # Text colors for different states
        self.text_color = text_color
        self.text_color2 = text_color2
        self.text_color3 = text_color3
        # Border color
        self.border_color = border_color
        # Co-ordinates for button
        self.x = x
        self.y = y
        # Dimensions for button
        self.width = width
        self.height = height
        self.text_size = text_size
        self.text = text
        self.border_size = border_size
        # Border
        self.border = border
        # Determines box and text colors
        self.color_box = COLORS["black"]
        self.color_text = COLORS["black"]
        # Records the state of the button
        self.button_down = False
        self.button_old_down = self.button_down
        self.was_clicked = False

    def update(self):
        # Creates ability to centre the bytton
        if self.x == 'centered':
            self.x = (S_WIDTH / 2) - (self.width / 2)

        # Checks if the mouse is over
        is_over_check = Useful.Game.is_over(self.x, self.y, self.width, self.height)
        
        # Changes the colors of the button if mouse is over
        if is_over_check:
            self.color_box = self.box_color2
            self.color_text = self.text_color2
        else:
            self.color_box = self.box_color
            self.color_text = self.text_color
        
        # Checks if the mouse is over and clicked and changes colors.
        if pygame.mouse.get_pressed()[0] and is_over_check:
            self.color_box = self.box_color3
            self.color_text = self.text_color3
            self.button_down = True
        else:
            self.button_down = False
        
        # Records if button is clicked 
        if self.button_down == False and self.button_down != self.button_old_down and is_over_check:
            self.was_clicked = True
        
        # Records the state of the previous button
        self.button_old_down = self.button_down
        
        # Draws button border
        if self.border:
            pygame.draw.rect(SCREEN, self.border_color, (self.x - (self.border_size/2), self.y - (self.border_size/2), self.width + self.border_size, self.height + self.border_size))
        
        # Draws button
        pygame.draw.rect(SCREEN, self.color_box, (self.x, self.y, self.width, self.height))

        # Draws text
        font = pygame.font.SysFont('comicsans', self.text_size, bold=True)
        label = font.render(self.text, 1, self.color_text)

        # Text positions
        x = self.x + (self.width / 2) - (label.get_width() / 2)
        y = self.y + (self.height / 2) - (label.get_height() / 2)

        # Blits text
        SCREEN.blit(label, (x, y))

# Player class ###############################################################################################################################
class Player(pygame.sprite.DirtySprite):
    def __init__(self, x, y, vel, images):
        pygame.sprite.DirtySprite.__init__(self)
        # Co-Ordinates of sprite
        self.x = x
        self.y = y
        # Hit box 
        self.hit_box_x = 0
        self.hit_box_y = 0
        self.hit_box_width = 0
        self.hit_box_height = 0 
        self.hit_box_center = (0, 0)
        # Record of sprite state for animatiion
        self.idle = False
        self.move = False
        self.shoot = False
        self.reload = False 
        # Sprite image and current animation
        self.current_images = images
        self.current_sprite = self.current_images[0]
        self.index = 0
        # Rotation of sprite
        self.angle = 0
        self.rotation_offset = Vector2(-35, 37)
        self.gun_offset = Vector2(-100, 2)
        self.hit_box_offset = Vector2(-0, 25)
        # Mask of sprite
        self.mask = pygame.mask.from_surface(self.current_sprite)
        # Sprite rect
        self.player_rect = 0, 0
        # Velocity 
        self.vel = vel 
        self.vel_left = vel
        self.vel_right = vel
        self.vel_up = vel
        self.vel_down = vel
        # Barrel position (tells bullets where to shoot from)
        self.barrel_pos_x = 0
        self.barrel_pos_y = 0
        # Number of bullets player can shoot
        self.BULLETS = 30
        self.BULLETS_LEFT = 180
        # Player health 
        self.alive = True
        self.health = 100

    # Creates frame rate variables
    frame = 0
    fps = 20

    # Updates sprite every frame
    def update(self):
        # Animation ##########################################################################################################################

        # Finds the state of keys
        key_pressed = pygame.key.get_pressed()

        # Frame number 
        Player.frame += Useful.Game.delta_time

        # Sprite animation frame rate
        if (Player.frame*1000) >= (1000/Player.fps):
            self.index += 1
            Player.frame = 0

        # changes sprite animation
        if self.index >= len(self.current_images):
            self.index = 0
        self.current_sprite = self.current_images[self.index]

        # Shooting Animation
        if pygame.mouse.get_pressed()[0] and not self.current_images == SPRITE_RELOAD and self.BULLETS >= 1 and self.current_images != SPRITE_SHOOT:
            self.index = 0
            self.current_images = SPRITE_SHOOT
            self.shoot = True
            Player.fps = 10

            # Plays gun sounds
            pygame.mixer.find_channel().play(GUNSHOT_SOUND2)
            pygame.mixer.find_channel().play(GUNSHOT_SOUND)

            # Updates number of bullets shot
            BULLETS_FIRED_LIST.append('b')

            # Activates a bullet sprite
            BULLETS.append(Projectile(self.x + 30, self.y + 200, self.x, self.y, self.barrel_pos_x, self.barrel_pos_y))
        
        if self.current_sprite == SPRITE_SHOOT[2] and self.shoot:
            self.BULLETS -= 1
            self.shoot = False
            global bullets_fired
            bullets_fired += 1 

        # Reload Animation
        reload_amount = 30 - self.BULLETS
        if reload_amount > self.BULLETS_LEFT:
            reload_amount = self.BULLETS_LEFT
        
        if key_pressed[pygame.K_r] and not self.shoot and not self.reload and self.BULLETS_LEFT >= 1:
            self.index = 0
            self.current_images = SPRITE_RELOAD
            self.reload = True 
            Player.fps = 20

            # Plays reload sound
            pygame.mixer.find_channel().play(RELOAD_SOUND)

        if self.current_sprite == SPRITE_RELOAD[19]:
            self.reload = False 

            # Updates ammocount
            self.BULLETS += reload_amount
            self.BULLETS_LEFT -= reload_amount

                    
        # Walking Animation
        if self.move and not self.reload and not self.shoot:
            self.current_images = SPRITE_WALK
            Player.fps = 40

        # Standing Animation
        if not self.move and not self.reload and not self.shoot:
            self.current_images = SPRITE_STAND
            Player.fps = 20

        # Rotation ###########################################################################################################################

        # Resizing
        self.current_sprite = pygame.transform.scale(self.current_sprite, (230, 152))

        # Finds direction of mouse 
        rotation_pivot = [self.x, self.y]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_x = mouse_x - rotation_pivot[0]
        direction_y = mouse_y - rotation_pivot[1]
        
        # Angle
        self.angle = (180 / math.pi) * -math.atan2(direction_y, direction_x)

        # Rotaded sprite
        rotation_offset_rotated = self.rotation_offset.rotate(-self.angle)
        rotated = Useful.Game.rotate_image(self.current_sprite, self.angle, rotation_pivot, rotation_offset_rotated, self.player_rect)
        
        # Updates sprite to rotated version
        self.current_sprite = rotated[0]
        self.player_rect = rotated[1]

        # Gun barrel position
        gun_offset_rotated = self.gun_offset.rotate(-self.angle)
        self.barrel_pos_x = rotation_pivot[0] - gun_offset_rotated[0]
        self.barrel_pos_y = rotation_pivot[1] - gun_offset_rotated[1]
    
        # Hit box center rotation
        hit_box_offset_rotated = self.hit_box_offset.rotate(-self.angle)
       
        # Collide checks #####################################################################################################################
        
        # Hit box parameters 
        self.hit_box_width = 90 
        self.hit_box_height = 90
        self.hit_box_x = rotation_pivot[0] - (self.hit_box_width/2) - hit_box_offset_rotated[0]
        self.hit_box_y = rotation_pivot[1] - (self.hit_box_height/2) - hit_box_offset_rotated[1]
        self.hit_box_center = self.hit_box_x + (self.hit_box_width/2), self.hit_box_y + (self.hit_box_height/2)
        
        # Resets velocity every frame
        self.vel_left = self.vel
        self.vel_right = self.vel
        self.vel_up = self.vel
        self.vel_down = self.vel

        # Collide check with zombies
        for zombie in ZOMBIES:
            # If collision on left 
            if (self.hit_box_x - self.vel) <= (zombie.hit_box_x + zombie.hit_box_width) and self.hit_box_x > zombie.hit_box_x:
                if self.hit_box_y <= (zombie.hit_box_y + zombie.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= zombie.hit_box_y:
                    self.vel_left = 0
                    self.x += 1 * 100 * Useful.Game.delta_time
            else:
                self.vel_left = self.vel
            # If collision on right
            if (self.hit_box_x + self.hit_box_width + self.vel) >= zombie.hit_box_x and self.hit_box_x < zombie.hit_box_x:
                if self.hit_box_y <= (zombie.hit_box_y + zombie.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= zombie.hit_box_y:
                    self.vel_right = 0
                    self.x -= 1 * 100 * Useful.Game.delta_time
            else:
                self.vel_right = self.vel
            # If collision on up 
            if (self.hit_box_y - self.vel) <= (zombie.hit_box_y + zombie.hit_box_height) and self.hit_box_y > zombie.hit_box_y:
                if self.hit_box_x <= (zombie.hit_box_x + zombie.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= zombie.hit_box_x:
                    self.vel_up = 0
                    self.y += 1 * 100 * Useful.Game.delta_time
            else:
                self.vel_up = self.vel
            # If collision on down
            if (self.hit_box_y + self.hit_box_height + self.vel) >= zombie.hit_box_y and self.hit_box_y < zombie.hit_box_y:
                 if self.hit_box_x <= (zombie.hit_box_x + zombie.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= zombie.hit_box_x:
                    self.vel_down= 0
                    self.y -= 1 * 100 * Useful.Game.delta_time
            else:
                self.vel_down = self.vel
        
        # Movement  ##########################################################################################################################
        
        # Moves when WASD is pressed
        if key_pressed[pygame.K_a]:
            self.x -= self.vel_left * 100 * Useful.Game.delta_time
        if key_pressed[pygame.K_d]:
            self.x += self.vel_right * 100 * Useful.Game.delta_time
        if key_pressed[pygame.K_w]:
            self.y -= self.vel_up * 100 * Useful.Game.delta_time
        if key_pressed[pygame.K_s]:
            self.y += self.vel_down * 100 * Useful.Game.delta_time
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_d] or key_pressed[pygame.K_w] or key_pressed[pygame.K_s]:
            self.move = True
        else:
            self.move = False 

        # Inbounds check
        if self.x >= S_WIDTH - 40:
            self.x = S_WIDTH - 40
        if self.x <= 40:
            self.x = 40
        if self.y >= S_HEIGHT - 120:
            self.y = S_HEIGHT - 120
        if self.y <= 40:
            self.y = 40

        # Blits ##############################################################################################################################

        # Blits sprite to screen
        SCREEN.blit(self.current_sprite, self.player_rect)
        
        # Hit boxes
        if Useful.Game.draw_hit_box == True:
            # Shows TRUE OFFSET
            pygame.draw.rect(SCREEN, (255,255,0), (rotation_pivot[0] - rotation_offset_rotated[0], rotation_pivot[1] - rotation_offset_rotated[1], 5,5))
            # Shows gun offset
            pygame.draw.rect(SCREEN, (255,0,255), (rotation_pivot[0] - gun_offset_rotated[0], rotation_pivot[1] - gun_offset_rotated[1], 5,5))
            # Shows pivot point 
            pygame.draw.rect(SCREEN, (0, 0,255), (rotation_pivot[0], rotation_pivot[1], 5,5))
            # Shows hit box center
            pygame.draw.rect(SCREEN, (255,0,0), (self.hit_box_x + (self.hit_box_width/2), self.hit_box_y + (self.hit_box_height/2), 5,5))
            # Shows hit box 
            pygame.draw.rect(SCREEN, (255,0,0), (self.hit_box_x, self.hit_box_y, self.hit_box_width, self.hit_box_height), 2)
        
        # Health 
        if self.health <= 0:
            self.alive = False 

# Zombie class ###############################################################################################################################
class Zombie(pygame.sprite.DirtySprite):
    def __init__(self, x, y, vel, images):
        pygame.sprite.DirtySprite.__init__(self)
        # Co-Ordinates of sprite
        self.x = x
        self.y = y
        # Hit box
        self.hit_box_x = 0
        self.hit_box_y = 0
        self.hit_box_width = 0
        self.hit_box_height = 0 
        self.hit_box_center = (0, 0)
        # Record of sprite state for animatiion
        self.idle = False
        self.move = True
        self.attack = False
        # Sprite image and current animation
        self.current_images = images
        self.current_sprite = self.current_images[0]
        self.index = 0
        # Rotation of sprite
        self.angle = 0
        self.rotation_offset = Vector2(-10, 10)
        self.hit_box_offset = Vector2(-0, 0)
        # Mask of sprite
        self.mask = pygame.mask.from_surface(self.current_sprite)
        # Sprite rect
        self.zombie_rect = 0, 0
        # Velocity 
        self.vel = vel 
        self.old_vel = vel
        # Animation frame rate
        self.frame = 0
        self.fps = random.randint(16, 26)
        # Distance from player
        self.distance = 1000
        # Zombie health
        self.health = 100

    # updates sprite every frame
    def update(self):
        # Animation ##########################################################################################################################

        # Finds the state of keys
        key_pressed = pygame.key.get_pressed()

        # Frame number
        self.frame += Useful.Game.delta_time
        
        # Sprite animation frame rate
        if (self.frame*1000) >= (1000/self.fps):
            self.index += 1
            self.frame = 0
            new_frame = True
        else: 
            new_frame = False

        # changes sprite animation
        if self.index >= len(self.current_images):
            self.index = 0
        self.current_sprite = self.current_images[self.index]

        # Starts attack animation if 150 pixels or less from player
        if self.distance < 150:
            self.fps = 20
            self.current_images = Assets.zombie_animations.SPRITE_ATTACK
            self.attack = True

        # Declares if the player is not attacking that it is moving
        else: 
            self.move = True
            self.attack = False

        # Makes the attack animation start on first image
        if self.attack == True and self.move == True:
            self.index = 0
            self.move = False

        # Movement animation
        if self.move == True:
            self.fps = 20
            self.current_images = Assets.zombie_animations.SPRITE_WALK

        # Damages player if the full attack animation is finished 
        if self.current_sprite == Assets.zombie_animations.SPRITE_ATTACK[8]:
            self.attack = False
            if new_frame:
                for player in PLAYER:
                    player.health -= 10

        # Rotation ###########################################################################################################################

        # Resizing
        self.current_sprite = pygame.transform.scale(self.current_sprite, (200, 184))
        self.mask = pygame.mask.from_surface(self.current_sprite)

        # Finds direction of player
        for player in PLAYER:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction_x = player.hit_box_center[0] - self.x
            direction_y = player.hit_box_center[1] - self.y

            # Zombie angle
            self.angle = (180 / math.pi) * -math.atan2(direction_y, direction_x)

        # Pivot point that image is rotated around
        rotation_pivot = [self.x, self.y]

        # Rotated sprite
        rotation_offset_rotated = self.rotation_offset.rotate(-self.angle)
        rotated = Useful.Game.rotate_image(self.current_sprite, self.angle, rotation_pivot, rotation_offset_rotated, self.zombie_rect)

        # Updates sprite to rotated version
        self.current_sprite = rotated[0]
        self.zombie_rect = rotated[1]

        # Hit box center rotation
        hit_box_offset_rotated = self.hit_box_offset.rotate(-self.angle)

        # Collide checks #####################################################################################################################

        # Hit box parameters 
        self.hit_box_width = 110
        self.hit_box_height = 110
        self.hit_box_x = rotation_pivot[0] - (self.hit_box_width/2) - hit_box_offset_rotated[0]
        self.hit_box_y = rotation_pivot[1] - (self.hit_box_height/2) - hit_box_offset_rotated[1]
        self.hit_box_center = self.hit_box_x + (self.hit_box_width/2), self.hit_box_y + (self.hit_box_width/2)
        
        # Bullet check
        for bullet in BULLETS:
            if Useful.Game.collide_check(self, self.zombie_rect[0], self.zombie_rect[1], bullet, bullet.x, bullet.y):
                if self.health > 0:
                    self.health -= 30
                    BULLETS.pop(BULLETS.index(bullet))
        
        # Collide check with player 
        for player in PLAYER:
            # If collision on left 
            if (self.hit_box_x - self.vel) <= (player.hit_box_x + player.hit_box_width) and self.hit_box_x > player.hit_box_x:
                if self.hit_box_y <= (player.hit_box_y + player.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= player.hit_box_y:
                    self.x += 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel
            # If collision on right
            if (self.hit_box_x + self.hit_box_width + self.vel) >= player.hit_box_x and self.hit_box_x < player.hit_box_x:
                if self.hit_box_y <= (player.hit_box_y + player.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= player.hit_box_y:
                    self.x -= 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = 3
            # If collision on up 
            if (self.hit_box_y - self.vel) <= (player.hit_box_y + player.hit_box_height) and self.hit_box_y > player.hit_box_y:
                if self.hit_box_x <= (player.hit_box_x + player.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= player.hit_box_x:
                    self.y += 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel
            # If collision on down
            if (self.hit_box_y + self.hit_box_height + self.vel) >= player.hit_box_y and self.hit_box_y < player.hit_box_y:
                 if self.hit_box_x <= (player.hit_box_x + player.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= player.hit_box_x:
                    self.y -= 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel

        # Collide check with zombies
        for zombie in ZOMBIES:
            # If collision on left 
            if (self.hit_box_x - self.vel) <= (zombie.hit_box_x + zombie.hit_box_width) and self.hit_box_x > zombie.hit_box_x:
                if self.hit_box_y <= (zombie.hit_box_y + zombie.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= zombie.hit_box_y:
                    self.x += 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel
            # If collision on right
            if (self.hit_box_x + self.hit_box_width + self.vel) >= zombie.hit_box_x and self.hit_box_x < zombie.hit_box_x:
                if self.hit_box_y <= (zombie.hit_box_y + zombie.hit_box_height) and (self.hit_box_y + self.hit_box_height) >= zombie.hit_box_y:
                    self.x -= 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel
            # If collision on up 
            if (self.hit_box_y - self.vel) <= (zombie.hit_box_y + zombie.hit_box_height) and self.hit_box_y > zombie.hit_box_y:
                if self.hit_box_x <= (zombie.hit_box_x + zombie.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= zombie.hit_box_x:
                    self.vel_up = 0
                    self.y += 1 * 100 * Useful.Game.delta_time
            else:
                self.vel = self.old_vel
            # If collision on down
            if (self.hit_box_y + self.hit_box_height + self.vel) >= zombie.hit_box_y and self.hit_box_y < zombie.hit_box_y:
                 if self.hit_box_x <= (zombie.hit_box_x + zombie.hit_box_width) and (self.hit_box_x + self.hit_box_width) >= zombie.hit_box_x:
                    self.y -= 1 * 100 * Useful.Game.delta_time
                    self.vel = 0
            else:
                self.vel = self.old_vel

        # Movement  ##########################################################################################################################

        # Finds distance to player
        for player in PLAYER:
            distance_x = self.hit_box_center[0] - player.hit_box_center[0]
            distance_y = self.hit_box_center[1] - player.hit_box_center[1]

        # Makes the distance a positive number 
        if distance_x <= -1:
            distance_x = distance_x * -1
        if distance_y <= -1:
            distance_y = distance_y * -1

        # Uses a^2 + b^2 = c^2 equation to find the distance
        distance_squared = (distance_x**2)+(distance_y**2)

        # Square roots c^2 
        self.distance = distance_squared**0.5
        
        # Caclulates velocity
        self.vel_x = round(math.cos(-self.angle / (180 / math.pi)) * self.vel)
        self.vel_y = round(math.sin(-self.angle / (180 / math.pi)) * self.vel)

        # Moves at set velocity
        self.x += self.vel_x
        self.y += self.vel_y

        # Blits ##############################################################################################################################

        # Blits sprite to screen   
        SCREEN.blit(self.current_sprite, self.zombie_rect)

        # Hit boxes 
        if Useful.Game.draw_hit_box:
            # Shows TRUE OFFSET
            pygame.draw.rect(SCREEN, (255,255,0), (rotation_pivot[0] - rotation_offset_rotated[0], rotation_pivot[1] - rotation_offset_rotated[1], 5,5))
            # Shows pivot point 
            pygame.draw.rect(SCREEN, (0, 0,255), (rotation_pivot[0], rotation_pivot[1], 5,5))
            # Shows hit box center
            pygame.draw.rect(SCREEN, (255,0,0), (self.hit_box_x + (self.hit_box_width/2), self.hit_box_y + (self.hit_box_height/2), 5,5))
            # Shows hit box 
            pygame.draw.rect(SCREEN, (255,0,0), (self.hit_box_x, self.hit_box_y, self.hit_box_width, self.hit_box_height), 2)

        # Health bar 
        bar_height = 10
        health_bar_width = (100/100)*self.health
        red_bar_width = 100
        red_bar = pygame.draw.rect(SCREEN, COLORS['red'], (self.x - 50, self.y - 100, red_bar_width, bar_height))
        if self.health >= 1:
            green_bar = pygame.draw.rect(SCREEN, COLORS['green'], (self.x - 50, self.y - 100, health_bar_width, bar_height))

# Bullet class ###############################################################################################################################
class Projectile(pygame.sprite.DirtySprite):
    def __init__(self, x, y, player_x, player_y, player_gun_x, player_gun_y):
        pygame.sprite.DirtySprite.__init__(self)
        # Starting co-ordinates of bullets
        self.x = player_gun_x
        self.y = player_gun_y
        # Bullet image 
        self.current_sprite = pygame.transform.scale(Assets.bullet.SPRITE_BULLET, (10, 10))
        # Bullet mask
        self.mask = pygame.mask.from_surface(self.current_sprite)
        # Velocity of bullet
        self.vel = 50 #* 100 * Useful.Game.delta_time
        # Finds direction of mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_x = mouse_x - player_x
        direction_y = mouse_y - player_y
        # Bullet angle
        self.angle = math.atan2(direction_y, direction_x)
        self.vel_x = round(math.cos(self.angle) * self.vel)
        self.vel_y = round(math.sin(self.angle) * self.vel)
        # Records whether bullet is on the screen or not
        self.in_bounds = True 

    # Updates sprite every frame
    def update(self):
        # Moves bullet in direction its shot 
        self.x += self.vel_x
        self.y += self.vel_y

        # Records whether bullet is on the screen
        if self.x < 1980 and self.x > 0 and self.y > 0 and self.y < 1080:
            self.in_bounds = True
        else:
            self.in_bounds = False

        # Blitz image to screen
        SCREEN.blit(self.current_sprite, (round(self.x), round(self.y)))

