import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH // 2
    Y_POS = 500
    MAX_Y_POS = SCREEN_HEIGHT // 2  # La mitad de la altura de la pantalla
    SPEED = 10

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.SPEED
            else:
                self.rect.x = SCREEN_WIDTH
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SPEED
            else:
                self.rect.x = -self.SPACESHIP_WIDTH
        elif user_input[pygame.K_UP]:
            if self.rect.y > self.MAX_Y_POS:
                self.rect.y -= self.SPEED
        elif user_input[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
                self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))