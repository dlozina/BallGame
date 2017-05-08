import sys

from time import sleep

import pygame
import random

from player import Player
from ball import Ball

def check_keydown_events(event, bg_settings, screen, player):
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
        sys.exit()

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

def check_events(bg_settings, screen, player, ball):
    """Respond to key press and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, bg_settings, screen, player)
                 
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, player)

def collision_check(player, ball):
    """Detect colision of player and the ball"""
    if pygame.sprite.collide_rect(player, ball):
        ball.x = random.randint(ball.rect.width, 
            (ball.bg_settings.screen_width - ball.rect.width))
        ball.y = ball.rect.height

def ball_update(bg_settings, stats, player, ball):
    """
    Create ball movement and detect end of screen and collisions
    with player
    """
    if ball.end_of_screen() and bg_settings.player_limit > 0:
        bg_settings.player_limit -= 1
        sleep(0.5)
        
    elif bg_settings.player_limit <= 0:
        stats.game_active = False
        
    collision_check(player, ball)
    ball.update()
                       
def update_screen(bg_settings, stats, screen, player, ball):
    """Update images on the screen and flip to the new screen"""
    #Redraw the screen during each pass trough the loop
    screen.fill(bg_settings.bg_color)
    #Redraw player and ball.
    player.blitme()
    ball.blitme()
    collision_check(player, ball)
    #Make the most recently drawn screen visible.
    pygame.display.flip()
