#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from random import*
import lib.img
import lib.perso
image = lib.img.image()
#mettre les variables pique,plate

class obstacle:
    
    def __init__(self):
        self.structure=[0,0,0]
        self.positionX=[0,0,0]
    def generation(self):
        i=int=0   
        for i in range(0,3):
            self.structure[i]=randint(1,3)
            self.positionX[i]=randint(50,600)
            sorted(self.positionX)
        
        
            
        if abs(self.positionX[0]-self.positionX[1])<50 or abs(self.positionX[1]-self.positionX[2])<50 or abs(self.positionX[0]-self.positionX[2])<50 :     
            self.positionX.pop(1)
            self.positionX.insert(1,randint(50,600))
                
    def affichage(self,fenetre):

        self.Sprite_tonneaux=pygame.sprite.Group()
        self.Sprite_plateforme=pygame.sprite.Group()
        self.Sprite_pique=pygame.sprite.Group()
        self.Sprite_fondpique=pygame.sprite.Group()
        i=0
        for i in range(0,3):
            
            if self.structure[i]==1:
                self.pique=pique(i, self.positionX[i])
                self.Sprite_pique.add(self.pique)
                self.fondpique=fondpique(i, self.positionX[i])
                self.Sprite_fondpique.add(self.fondpique)
            if  self.structure[i]==2:
                self.tonneaux=tonneaux(i, self.positionX[i])
                self.Sprite_tonneaux.add(self.tonneaux)
            if self.structure[i]==3:
                self.plateforme=plateforme(i, self.positionX[i])
                self.Sprite_plateforme.add(self.plateforme)


            self.Sprite_plateforme.draw(fenetre)
            self.Sprite_fondpique.draw(fenetre)
            self.Sprite_pique.draw(fenetre)
            self.Sprite_tonneaux.draw(fenetre)

class plateforme(pygame.sprite.Sprite):

    def __init__(self, i, posx):

        super().__init__()
        self.image=pygame.image.load(image.plateforme).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 300
        self.mask = pygame.mask.from_surface(self.image)

class pique(pygame.sprite.Sprite):

    def __init__(self, i, posx):

        super().__init__()
        self.image=pygame.image.load(image.pique).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 420
        self.mask = pygame.mask.from_surface(self.image)

class fondpique(pygame.sprite.Sprite):

    def __init__(self, i, posx):

        super().__init__()
        self.image=pygame.image.load(image.fondpique).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 420
        self.mask = pygame.mask.from_surface(self.image)

class tonneaux(pygame.sprite.Sprite):

    def __init__(self, i, posx):

        super().__init__()
        self.image=pygame.image.load(image.tonneaux).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
        
        
                
        
