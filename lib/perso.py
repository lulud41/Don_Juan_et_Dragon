#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame
import lib.img
import lib.event
from pygame.locals import *
image = lib.img.image()

class personnage(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
        
        #chargement
        self.droite=pygame.image.load(image.persoD).convert_alpha()
        self.gauche=pygame.image.load(image.persoG).convert_alpha()
        self.image=self.droite
        self.atkdroite=pygame.image.load(image.persoAD).convert_alpha()
        self.atkgauche=pygame.image.load(image.persoAG).convert_alpha()
        self.etat = 'terre'
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 341
        self.terre=341
        self.inv=False
        self.collisionmur=0
        self.vie=4
        
    def move(self, direction, attaque):
        if direction == 'droite' and not 1 in attaque:
            self.image = self.droite
        if direction == 'droite' and self.collisionmurG==0:
            self.rect.x = self.rect.x+5
                
        if direction == 'gauche' and not 1 in attaque:
            self.image = self.gauche
        if direction == 'gauche' and self.collisionmurD==0:
            self.rect.x = self.rect.x-5

    def attaque(self, direction, attaque, timeattaque):
        if direction == 'droite' and 1 in attaque and timeattaque<10:
            self.image = self.atkdroite

        if direction == 'gauche' and timeattaque==0:
            self.rect.x=self.rect.x-25

        if direction == 'gauche' and 1 in attaque and timeattaque<10:
            self.image = self.atkgauche

    def jump(self, etatperso, time):
        if etatperso == 'saut' or etatperso == 'plateforme' or etatperso=='tonneau':
            self.rect.y=self.rect.y-((7/20)*(time*time))

    def gravite(self, etatperso):
        if etatperso == 'air':
            self.rect.y = self.rect.y+11

    def reinit(self, timeattaque, direction, event):
        if timeattaque==10 and direction == 'droite':
            self.image=self.droite
        if timeattaque==10 and direction == 'gauche':
            self.image=self.gauche
        if timeattaque==10 and direction == 'gauche':
            self.image=self.gauche
            self.rect.x=self.rect.x+25
        if timeattaque==10:
            event.hasattack=False

    def etatperso(self, keypressed, perso, event):
        if self.etat=='saut':
            if event.timejump<0:
                perso.jump(self.etat, event.timejump)
            elif self.etat!='plateforme' and self.etat !='tonneau':
                event.timejump=0
                self.etat= 'air'
                
        if self.rect.y==self.terre:
            self.etat='terre'
            
        if self.rect.y<self.terre:
            if self.etat != 'saut':
                perso.gravite(self.etat)
                
        if self.rect.y>self.terre:
            self.rect.y=self.terre

        if event.timeinv==30:
            self.inv=False
            self.timeinv=0
            
            
            

            
                
        
            

