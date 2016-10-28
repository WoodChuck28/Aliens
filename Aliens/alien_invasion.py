import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)


    #start main game loop
    while True:

        #import game_functions
        gf.check_events(ai_settings, screen, ship, bullets)

        #update ship because we want to see changes after check_events
        ship.update()

        gf.update_bullets(bullets)

        #redraw screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
