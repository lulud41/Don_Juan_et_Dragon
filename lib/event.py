#!/usr/bin/python
# -*- coding: UTF-8 -*-

#classe event
import os
import lib.perso
import lib.img
import pygame
from pygame import *
image = lib.img.image()


class event:

     def __init__(self):
          self.keypressed=[]
          self.attaque=[]
          self.timeattaque = 0
          self.timejump=0
          self.timeinv=0
          self.direction = 'droite'
          self.dirpre= 'none'
          self.continuer = 1
          self.fromplateforme=False
          self.droite=True
          self.gauche=True
          self.hasattack=False
          self.icone=pygame.image.load(image.perso1).convert_alpha()

#fonction de capture des évènements
     def capture(self, pygameevent):

          for event in pygameevent:
             if event.type == QUIT:
                 self.continuer = 0

             if event.type == KEYDOWN:
                 if event.key == K_RIGHT:
                     if 'R' in self.keypressed:
                         self.keypressed.remove('R')
                     self.keypressed.append('R')
                 if event.key == K_LEFT:
                     if 'L' in self.keypressed:
                         self.keypressed.remove('L')
                     self.keypressed.append('L')
                 if event.key == K_UP:
                     if 'U' in self.keypressed:
                         self.keypressed.remove('U')
                     self.keypressed.append('U')

             if event.type == KEYUP:
                 if event.key == K_RIGHT:
                     if 'R' in self.keypressed:
                         self.keypressed.remove('R')
                 if event.key == K_LEFT:
                     if 'L' in self.keypressed:
                         self.keypressed.remove('L')
                 if event.key == K_UP:
                     self.keypressed.remove('U')
             #bloc attaque
             if event.type == MOUSEBUTTONDOWN:
                 if event.button == 1:
                     if self.timeattaque>10:
                         if 1 in self.attaque:
                             self.attaque.remove(1)
                         self.attaque.append(1)
                         self.timeattaque=0
                         
             if self.timeattaque>10:
                  if 1 in self.attaque:
                       self.attaque.remove(1)

#fonction de test des évènements
     def test(self, etat, perso):
     
          if 'R' in self.keypressed and self.droite==True:
               self.direction = 'droite'
               perso.move(self.direction, self.attaque)
               if 'L' in self.keypressed:
                   self.keypressed.remove('L')
          if 'L' in self.keypressed and self.gauche==True:
               self.direction = 'gauche'
               perso.move(self.direction, self.attaque)
               if 'R' in self.keypressed:
                    self.keypressed.remove('R')
          if 1 in self.attaque:
               perso.attaque(self.direction, self.attaque, self.timeattaque)
                              
          if etat == 'terre' or etat == 'plateforme' or etat=='tonneau':
               if 'U' in self.keypressed:
                   perso.etat='saut'
                   self.timejump=-10

          if etat == 'tonneau' and perso.rect.y>230:
               self.fromplateforme=True
                 
     def collision(self, score, plateforme, tonneaux, pique, perso, ennemi, pygame, Sprite_en, fondpique):
          
          if 1 in self.attaque and self.hasattack==False:
               if pygame.sprite.spritecollide(perso, Sprite_en, False, pygame.sprite.collide_mask) != []:
                    self.hasattack=True
                    score+=10
               pygame.sprite.spritecollide(perso, Sprite_en, True, pygame.sprite.collide_mask)
          if perso.rect.y <230:
               if plateforme != None and perso.etat=='air':
                    perso.etat='plateforme'
                    if perso.rect.y>=220:
                         perso.rect.y=221
               elif plateforme == None and perso.etat=='plateforme' and perso.etat!='saut':
                    perso.etat='air'
                    
          if tonneaux != None and perso.rect.y > 280:
               self.collide=True
               if self.fromplateforme == False:
                    if self.direction == 'droite':
                         perso.collisionmurG=1
                         perso.collisionmurD=0
                    if self.direction == 'gauche':
                         perso.collisionmurD=1
                         perso.collisionmurG=0

               if self.fromplateforme == True:
                    if self.direction == 'droite':
                         perso.collisionmurG=0
                         perso.collisionmurD=1
                         if perso.etat=='terre':
                              self.gauche=False
                    if self.direction == 'gauche':
                         perso.collisionmurD=0
                         perso.collisionmurG=1
                         if perso.etat=='terre':
                              self.droite=False
                    
          else:
               perso.collisionmurD=0
               perso.collisionmurG=0
               self.gauche=True
               self.droite=True
               if perso.etat=='terre':
                    self.fromplateforme=False
               
          if perso.rect.x<-5:
               perso.rect.x=-5

          if perso.rect.x>595:
               perso.rect.x=595
               
          if perso.rect.y <=290:
               if tonneaux != None and perso.etat=='air':
                    perso.etat='tonneau'
                    if perso.rect.y>=280:
                         perso.rect.y=281
               elif tonneaux == None and perso.etat=='tonneau':
                    perso.etat='air'
                    
          if pique != None:
               if perso.inv==False:
                    self.timeinv=0
                    perso.inv= True
                    perso.vie= perso.vie - 1
                    print(perso.vie)
                    perso.etat='saut'
                    self.timejump=-10
          if fondpique != None:
               perso.terre=480
               if perso.etat!='saut':
                    perso.etat='air'
          else:
               perso.terre=341


          if ennemi != None and 1 not in self.attaque:
               if perso.inv==False:
                    self.timeinv=0
                    perso.inv= True
                    perso.vie= perso.vie - 1
                    print(perso.vie)

          return score
               
     def UI(self, perso, fenetre):         
          if perso.vie==3:
               self.icone=pygame.image.load(image.perso2).convert_alpha()
          if perso.vie==2:
               self.icone=pygame.image.load(image.perso3).convert_alpha()
          if perso.vie==1:
               self.icone=pygame.image.load(image.perso4).convert_alpha()

          fenetre.blit(self.icone, (30,30))
#fonction compteur
     def compteur(self, perso):
          if self.timeattaque < 11:
               self.timeattaque=self.timeattaque+1
          if self.timejump <0:
               self.timejump=self.timejump+1
          if perso.inv==True:
               self.timeinv=self.timeinv+1
          else:
               self.timeinv=0
