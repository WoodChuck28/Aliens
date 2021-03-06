import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #positioning
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Next position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)
