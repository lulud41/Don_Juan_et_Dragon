import pygame
from pygame.locals import *
import lib.perso
import lib.img
image = lib.img.image()

class ennemi(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
        
        self.image= pygame.image.load(image.ennemiG).convert_alpha()
        self.rect= self.image.get_rect()
        self.etat = 'terre'
        self.direction= 'gauche'
            
    def update(self, etat, persox, persoy, timejump):
                #bloc ennemi
        if persox-50 > self.rect.x :
            self.direction = 'droite'
        if persox+50 < self.rect.x :
            self.direction = 'gauche'
        if self.rect.y>390:
            self.rect.y=390
        if self.direction == 'droite':
            if persox > self.rect.x and etat == 'saut':
                self.rect.x = self.rect.x+2
                self.image = pygame.image.load(image.ennemiD).convert_alpha()                
            elif persox < self.rect.x and etat == 'saut':
                self.rect.x = self.rect.x+2
                self.image = pygame.image.load(image.ennemiD).convert_alpha()
            elif persox > self.rect.x and etat == 'air':
                self.rect.x = self.rect.x+2
                self.image = pygame.image.load(image.ennemiD).convert_alpha()
            elif persox < self.rect.x and etat == 'air':
                self.rect.x = self.rect.x+2
                self.image = pygame.image.load(image.ennemiD).convert_alpha()
            else:
                self.rect.x = self.rect.x+2
                self.image = pygame.image.load(image.ennemiD).convert_alpha()
            if self.rect.y < persoy and self.rect.x - persox >= -100:
                self.rect.y = self.rect.y + 3
            if self.rect.y > persoy and self.rect.x - persox >= -100:
                self.rect.y = self.rect.y - 3
            
        if self.direction == 'gauche':
            if persox > self.rect.x and etat == 'saut':
                self.rect.x = self.rect.x-2
                self.image = pygame.image.load(image.ennemiG).convert_alpha()
            elif persox < self.rect.x and etat == 'saut':
                self.rect.x = self.rect.x-2
                self.image = pygame.image.load(image.ennemiG).convert_alpha()
            elif persox > self.rect.x and etat == 'air':
                self.rect.x = self.rect.x-2
                self.image = pygame.image.load(image.ennemiG).convert_alpha()
            elif persox < self.rect.x and etat == 'air':
                self.rect.x = self.rect.x-2
                self.image = pygame.image.load(image.ennemiG).convert_alpha()
            else:
                self.rect.x = self.rect.x-2
                self.image = pygame.image.load(image.ennemiG).convert_alpha()                
            if self.rect.y < persoy and self.rect.x - persox <= 100:
                self.rect.y = self.rect.y + 3
            if self.rect.y > persoy and self.rect.x - persox <= 100:
                self.rect.y = self.rect.y - 3
