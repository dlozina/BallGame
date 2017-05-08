import pygame

from settings import Settings
from game_stats import GameStats
from player import Player
from ball import Ball
import game_functions as gf

def run_game():
    #Initialize pygame,settings and screen object.
    pygame.init()
    bg_settings = Settings()
    screen = pygame.display.set_mode(
        (bg_settings.screen_width, bg_settings.screen_height))
    pygame.display.set_caption("Ball Game")
    #Create an instance to store game statistics.
    stats = GameStats(bg_settings)
    #Make a player and a random ball
    player = Player(bg_settings, screen)
    ball = Ball(bg_settings, screen)
    
    
    
    #Start the main loop for the game.
    while True:
        gf.check_events(bg_settings, screen, player, ball)
        
        if stats.game_active:
            player.update()
            gf.ball_update(bg_settings, stats, player, ball)
            
        
        gf.update_screen(bg_settings, stats, screen, player, ball)
        
        
run_game()
