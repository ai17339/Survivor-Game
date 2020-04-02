# -------------------------------------------------------------------------------
# Name:        Survivor
# Purpose:
#
# Author:      Archie Irving
#
# Created:     27/02/2020
# -------------------------------------------------------------------------------

# Imports
import math, time, random, pygame
import Useful, Assets, Sprites
from Constants import*

# Scenes #######################################################################################################################################################################
# ##############################################################################################################################################################################

# MAIN MENU SCENE ##############################################################################################################################################################
def main_menu():
    # Buttons
    play_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["silver"], COLORS["black"], COLORS["silver"], COLORS["black"], 400, 350, 600, 100, 100, 8, "PLAY", True)
    controls_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["silver"], COLORS["black"], COLORS["silver"], COLORS["black"], 400, 500, 600, 100, 100, 8, "CONTROLS", True)
    exit_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["silver"], COLORS["black"], COLORS["silver"], COLORS["black"], 400, 800, 400, 100, 100, 8, "EXIT", True)
    
    # Creates spinning sprite
    player_sprite = Sprites.menu_sprite(1300, 500)
    
    # Runs the menu loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # DISPLAY ##############################################################################################################################################################

        # Background
        SCREEN.blit(Assets.background.BACKGROUND_1, (0, 0))

        # Draws buttons
        play_button.update()
        controls_button.update()
        exit_button.update()

        # Button Actions
        if play_button.was_clicked:
            main_game()
        if controls_button.was_clicked:
            controls_menu()
        if exit_button.was_clicked:
            pygame.quit()

        # Draws Title 
        Sprites.Text.draw_text('SURVIVOR', 300 , COLORS["red"], SCREEN, 400, 100)
        Sprites.Text.draw_text('SURVIVOR', 300 , COLORS["black"], SCREEN, 400 - 2, 100 - 1)

        # Draws Sprite
        player_sprite.update()

        # Updates dispay every frame 
        pygame.display.update()

    pygame.quit()

# CONTROLS SCENE ###############################################################################################################################################################
def controls_menu():
    # Backdrop for text
    controls_button = Sprites.Button(COLORS["blackish"], COLORS["blackish"], COLORS["blackish"], COLORS["white"], COLORS["white"], COLORS["white"], COLORS["black"], 'centered', 100, 800, 700, 100, 8, "", True)

    # Button that takes player back to menu
    menu_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["silver"], COLORS["black"], COLORS["silver"], COLORS["black"], 'centered', 850, 650, 100, 100, 8, "BACK TO MENU", True)

    # Runs loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        # DISPLAY ##############################################################################################################################################################
        
        # Background
        SCREEN.blit(Assets.background.BACKGROUND_1, (0, 0))

        # Draws buttons
        controls_button.update()
        menu_button.update()

        # Button Actions
        if menu_button.was_clicked:
            main_menu()

        # Controls title
        Sprites.Text.draw_text('CONTROLS', 80 , COLORS["white"], SCREEN, 'centered', 120)

        # Shooting control
        Sprites.Text.draw_text('Shooting:', 50 , COLORS["silver"], SCREEN, 600, 210)
        Sprites.Text.draw_text('MouseButton1', 50 , COLORS["silver"], SCREEN, 1050, 210)

        # Movement
        Sprites.Text.draw_text('Move Left:', 50 , COLORS["silver"], SCREEN, 600, 270)
        Sprites.Text.draw_text('a', 50 , COLORS["silver"], SCREEN, 1050, 270)
        Sprites.Text.draw_text('Move Right:', 50 , COLORS["silver"], SCREEN, 600, 330)
        Sprites.Text.draw_text('d', 50 , COLORS["silver"], SCREEN, 1050, 330)
        Sprites.Text.draw_text('Move Up:', 50 , COLORS["silver"], SCREEN, 600, 390)
        Sprites.Text.draw_text('w', 50 , COLORS["silver"], SCREEN, 1050, 390)
        Sprites.Text.draw_text('Move Down:', 50 , COLORS["silver"], SCREEN, 600, 450)
        Sprites.Text.draw_text('s', 50 , COLORS["silver"], SCREEN, 1050, 450)

        # Development tool
        Sprites.Text.draw_text('Show colision boxes:', 50 , COLORS["silver"], SCREEN, 600, 510)
        Sprites.Text.draw_text('p', 50 , COLORS["silver"], SCREEN, 1050, 510)

        # Updates display every frame
        pygame.display.update()

# GAME SCENE ###################################################################################################################################################################
def main_game():
    # Clears all lists 
    BULLETS.clear()
    ZOMBIES.clear()
    PLAYER.clear()
    BULLETS_FIRED_LIST.clear()

    # Resets all counts 
    global round_count
    global round_count
    global zombie_count
    global bullets_fired
    round_count = 0 
    old_round_count = 0
    zombie_count = 0
    bullets_fired = 0
    dead_zombies = 0

    # Creates ammo and health bar rects
    UI_bar_width = 1115
    UI_bar_hieght = 300
    UI_bar_x = 350
    UI_bar_y = 960
    
    # Creates a player sprite
    PLAYER1 = Sprites.Player(700, 500, 3, SPRITE_STAND)
    PLAYER.append(PLAYER1)

    # Scene loop
    run = True
    while run:
        
        # Event handeling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()
        
        # Time Keeper
        Useful.Game.delta_time = Useful.Game.get_deltatime()
        Useful.Game.ticks_Last_Frame = pygame.time.get_ticks()

        # DISPLAY ##############################################################################################################################################################

        # Background
        SCREEN.blit(Assets.background.BACKGROUND_1, (0,0))

        # Displays hit_boxes of sprites
        Useful.Game.display_hit_box()

        # Bullets
        for bullet in BULLETS:
            if bullet.in_bounds == False:
                BULLETS.pop(BULLETS.index(bullet))

            # Blitz's bullet each frame
            bullet.update()

        # Updates number of bullets fired
        bullets_fired = len(BULLETS_FIRED_LIST)

        # Zombies to spawn each round
        if zombie_count == 0:
            round_count += 1
            zombie_count = round_count * 3

        # Randomly spawns zombies
        if round_count == old_round_count + 1:
            for zombie in range(0, zombie_count):
                random_spawn_point =  Useful.zombie_spawn.spawn_point()
                ZOMBIES.append(Sprites.Zombie(random_spawn_point[0], random_spawn_point[1], Useful.zombie_spawn.speed(), Assets.zombie_animations.SPRITE_STAND))
            old_round_count = round_count
        
        # Updates zombies each frame
        for zombie in ZOMBIES:
            zombie.update()
            
        # Deletes zombie if its health is 0
        for zombie in ZOMBIES:
            if zombie.health <= 0:
                pygame.mixer.find_channel().play(pygame.mixer.Sound(r'Sounds\ping2.wav'))
                ZOMBIE_DROPS.append(Sprites.zombie_drop(zombie.x, zombie.y))
                ZOMBIES.pop(ZOMBIES.index(zombie))
                zombie_count -= 1
                dead_zombies += 1

        # Zombie drops
        for drop in ZOMBIE_DROPS:
            drop.drop()
            if drop.finished == True:
                 ZOMBIE_DROPS.pop(ZOMBIE_DROPS.index(drop))

        # Updates player each frame 
        PLAYER1.update()

        # Ends game if player dies
        if PLAYER1.alive == False:
            time_dead = 0
            while True:
                Useful.Game.delta_time = Useful.Game.get_deltatime()
                Useful.Game.ticks_Last_Frame = pygame.time.get_ticks()
                Sprites.Text.draw_text("You DIED!", 400, COLORS["red"], SCREEN, 'centered', 400)
                time_dead += Useful.Game.delta_time
                if time_dead >= 2:
                    dead_screen(dead_zombies, round_count, bullets_fired)
                pygame.display.update()
                print(time_dead)

        # UI ##################################################################################################################################################################       
        
        # Ammo and HP
        UI_bar_border = pygame.draw.rect(SCREEN, COLORS['black'], (UI_bar_x - 5, UI_bar_y - 5, UI_bar_width + 10, UI_bar_hieght + 10))
        UI_bar_rect = pygame.draw.rect(SCREEN, COLORS['blackish'], (UI_bar_x, UI_bar_y, UI_bar_width, UI_bar_hieght))
        Sprites.Text.draw_text("AMMO: " + str(PLAYER1.BULLETS) + "/" + str(PLAYER1.BULLETS_LEFT), 80, COLORS["yellow"], SCREEN, UI_bar_x + 20, 980)
        
        # Round number 
        round_number_bar_border = pygame.draw.rect(SCREEN, COLORS['black'], (0 - 5, UI_bar_y - 5, 350 + 10, 100 + 10))
        round_number_bar_rect = pygame.draw.rect(SCREEN, COLORS['blackish'], (0, UI_bar_y, 350, 100))
        Sprites.Text.draw_text("ROUND " + str(round_count), 80, COLORS["white"], SCREEN, 30, 980)

        # Health Bar
        bar_height = 50
        red_bar_width = 450
        health_bar_width = (red_bar_width/100) * PLAYER1.health
        red_bar = pygame.draw.rect(SCREEN, COLORS['red'], (UI_bar_x + 640, 980, red_bar_width, bar_height))
        green_bar = pygame.draw.rect(SCREEN, COLORS['green'], (UI_bar_x + 640, 980, health_bar_width, bar_height))
        Sprites.Text.draw_text("HP ", 80, COLORS["red"], SCREEN, UI_bar_x + 530, 980)
        Sprites.Text.draw_text(str(PLAYER1.health), 80, COLORS["black"], SCREEN, UI_bar_x + 670, 980)

        # Zombie bar
        zombie_bar_border = pygame.draw.rect(SCREEN, COLORS['black'], (UI_bar_x + UI_bar_width - 5, UI_bar_y - 5, 450 + 10, UI_bar_hieght + 10))
        zombie_bar_rect = pygame.draw.rect(SCREEN, COLORS['blackish'], (UI_bar_x + UI_bar_width, UI_bar_y, 450, UI_bar_hieght))
        zombies_left = Sprites.Text.draw_text("Zombies Left: " + str(zombie_count), 40, COLORS["white"], SCREEN, UI_bar_x + UI_bar_width + 15, 975)
        zombies_dead = Sprites.Text.draw_text("Zombies Killed: " + str(dead_zombies), 40, COLORS["silver"], SCREEN, UI_bar_x + UI_bar_width + 15, 1015)
        
        # Frame rate
        Sprites.Text.draw_text(str(round(1/Useful.Game.delta_time)) + "FPS", 40, COLORS["black"], SCREEN, 1800, 20)

        # Updates display every frame 
        pygame.display.update()

# DEAD SCENE ###################################################################################################################################################################
def dead_screen(zombies_dead, rounds, bullets_fired):
    # Buttons
    play_again_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["white"], COLORS["lime"], COLORS["red"], COLORS["black"], 'centered', 300, 800, 100, 100, 8, "PLAY AGAIN", True)
    back_to_menu_button = Sprites.Button(COLORS["blackish"], COLORS["red"], COLORS["black"], COLORS["white"], COLORS["lime"], COLORS["red"], COLORS["black"], 'centered', 450, 800, 100, 100, 8, "BACK TO MENU", True)
    stats = Sprites.Button(COLORS["blackish"], COLORS["blackish"], COLORS["blackish"], COLORS["white"], COLORS["white"], COLORS["white"], COLORS["black"], 'centered', 590, 800, 400, 100, 8, "", True)

    # Clears lists
    BULLETS.clear()
    ZOMBIES.clear()
    PLAYER.clear()

    # Runs loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # DISPLAY ##############################################################################################################################################################

        # Background
        SCREEN.blit(Assets.background.BACKGROUND_1, (0, 0))

        # Draws buttons
        play_again_button.update()
        back_to_menu_button.update()
        stats.update()

        # Button Actions
        if play_again_button.was_clicked:
            main_game()
        if back_to_menu_button.was_clicked:
            main_menu()

        # Draws Title 
        Sprites.Text.draw_text('YOU DIED', 300, COLORS["red"], SCREEN, 'centered', 50)

        # STATS 
        Sprites.Text.draw_text('STATS', 150, COLORS["silver"], SCREEN, 'centered', 600)
        Sprites.Text.draw_text('Rounds Alive: ' + str(rounds), 100, COLORS["white"], SCREEN, 'centered', 700)
        Sprites.Text.draw_text('Zombies Killed: ' + str(zombies_dead), 100, COLORS["white"], SCREEN, 'centered', 800)
        Sprites.Text.draw_text('Bullets Fired: ' + str(bullets_fired), 100, COLORS["white"], SCREEN, 'centered', 900)
        
        # Updates display every frame
        pygame.display.update()
    
    pygame.quit()

# Game Start ########################################################################################################################################################################
# ##############################################################################################################################################################################
main_menu()
