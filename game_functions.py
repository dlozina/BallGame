import sys

from time import sleep

import pygame
import random

from player import Player
from ball import Ball

def check_keydown_events(event, bg_settings, screen, stats, sb, play_button,
        player, ball):
    if event.key == pygame.K_RIGHT:
        #Move player to the right.
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move player to the left.
        player.moving_left = True
    #Not in real bg
    #elif event.key == pygame.K_UP:
        #Move player to the up.
        #ship.moving_up = True
    #elif event.key == pygame.K_DOWN:
        #Move player to the down.
        #ship.moving_down = True
    #elif event.key == pygame.K_SPACE:
        #fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        filename = 'highscore.txt'
        with open(filename) as file_object:
            highscore = file_object.read()
        if int(highscore) <= stats.score:
            with open(filename, 'w') as file_object:
                file_object.write(str(stats.score))
        sys.exit()
        
    elif event.key == pygame.K_p:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_pressed = True
        check_play_button(bg_settings, screen, stats, sb, play_button, player, 
            ball, mouse_x, mouse_y, button_pressed)
                    
def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        #Move player to the right.
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        #Move player to the left.
        player.moving_left = False
    elif event.key == pygame.K_UP:
        #Move player to the up.
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        #Move player to the down.
        player.moving_down = False

def check_events(bg_settings, screen, stats, sb, play_button, player, ball):
    """Respond to key press and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                filename = 'highscore.txt'
                with open(filename) as file_object:
                    highscore = file_object.read()
                if int(highscore) <= stats.score:
                    with open(filename, 'w') as file_object:
                        file_object.write(str(stats.score))
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, bg_settings, screen, stats, sb, 
                    play_button, player, ball)
                 
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, player)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_pressed = True
                check_play_button(bg_settings, screen, stats, sb, play_button, 
                    player, ball, mouse_x, mouse_y, button_pressed)

def collision_check(bg_settings, player, ball, stats, sb):
    """Detect colision of player and the ball"""
    if pygame.sprite.collide_rect(player, ball):
        stats.score = stats.score + 1
        stats.level_up += 1
        if stats.level_up >= 10:
            bg_settings.increase_speed()
            stats.level += 1
            sb.prep_level()
            stats.level_up = 0
        sb.prep_score()
        check_high_score(stats, sb) 
        ball.x = random.randint(ball.rect.width, 
            (ball.bg_settings.screen_width - ball.rect.width))
        ball.y = ball.rect.height
        
def check_play_button(bg_settings, screen, stats, sb, play_button, player, 
        ball, mouse_x, mouse_y, button_pressed):
    """Start a new game when the player clics Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    start_game = button_clicked or button_pressed
    if start_game and not stats.game_active:
        #Disable P pressed to start new game
        button_clicked = False
        #Reset the game settings
        bg_settings.initialize_dynamic_settings()
        #Hide mouse cursor.
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        
        #Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        
        #Center Player
        player.center_player()
             
def ball_update(bg_settings, stats, player, ball, sb):
    """
    Create ball movement and detect end of screen and collisions
    with player
    """
    if stats.player_left > 0:
        if ball.end_of_screen():
            stats.player_left -= 1
            sleep(0.5)
        collision_check(bg_settings, player, ball, stats, sb)
        ball.update()
    
    else: #bg_settings.player_limit <= 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    """Check to see if there is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
                
def update_screen(bg_settings, stats, screen, player, ball, sb, play_button):
    """Update images on the screen and flip to the new screen"""
    #Redraw the screen during each pass trough the loop
    screen.fill(bg_settings.bg_color)
    
    #Redraw player and ball.
    player.blitme()
    ball.blitme()
    
    #Draw score information
    sb.show_score()
    
    #Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
        
    #Make the most recently drawn screen visible.
    pygame.display.flip()
