#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame
import random
import time
from pygame.locals import *
import lib.img
import lib.perso
import lib.classemap
import lib.ennemi
import lib.event

pygame.display.init()
pygame.font.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#boucle menu 

fenetre = pygame.display.set_mode((640, 480))
image = lib.img.image()
menu=pygame.image.load(image.menu)
jouerimg=pygame.image.load(image.jouer2)
Mperso=pygame.image.load(image.persoAD)
Mia=pygame.image.load(image.ennemiD)
fenetre.blit(menu, (0,0))
pygame.display.flip()
jouer=0
Miax=0
myfont = pygame.font.SysFont("monospace", 16)
version_display = myfont.render(str("version 0.1"), 1, (255,255,255))
fenetre.blit(version_display, (100, 10))

Mpersox=0

while jouer ==0:
    (mouseX, mouseY) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
        
        if mouseX>280 and mouseX<360 and mouseY>250 and mouseY<330:
            jouerimg=pygame.image.load(image.jouer1)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    jouer=1
        else:
            jouerimg=pygame.image.load(image.jouer2)
                
            
    fenetre.blit(menu, (0,0))
    fenetre.blit(Mia, (Miax,280))
    fenetre.blit(Mperso, (Mpersox,300))
    fenetre.blit(jouerimg, (280, 250))
    version_display = myfont.render("version 0.1", 1, (0,0,0))
    fenetre.blit(version_display, (10, 10))
    Miax+=2
    Mpersox+=1
    pygame.display.flip()
    if Mpersox ==650:
        Mpersox=-20
        Miax=-10

#variables
score=0
image = lib.img.image()
event = lib.event.event()
perso = lib.perso.personnage()
Sprite_perso=pygame.sprite.Group()
Sprite_perso.add(perso)
Sprite_en=pygame.sprite.Group()
#apparition des sprites ennemis
nbren=random.randrange(1,5)
for i in range(nbren):
    en=lib.ennemi.ennemi()

    en.rect.x = random.randrange(200,480)
    en.rect.y=random.randrange(200,330)

    Sprite_en.add(en)
#attaque
attaque=[]

#Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(40,30)
fond = pygame.image.load(image.fond).convert()
fenetre.blit(fond, (0,0))
sol = pygame.image.load(image.sol).convert()
fenetre.blit(sol, (0,420))
Fond=fond.get_rect()
Sol=sol.get_rect()


keypressed= []

#génération du niveau
decor=lib.classemap.obstacle()
decor.generation()
decor.affichage(fenetre)
fenetre.blit(pygame.image.load(image.trois), (300,200))
pygame.display.update()
time.sleep(1)
fenetre.blit(pygame.image.load(image.deux), (300,200))
pygame.display.update()
time.sleep(1)
fenetre.blit(pygame.image.load(image.un), (300,200))
pygame.display.update()
time.sleep(1)
        
#BOUCLE JEU
while event.continuer == 1:
    pygame.time.Clock().tick(60)

    #actualise les compteurs de temps d'attaque et de saut
    event.compteur(perso)
    #capture les évènements
    event.capture(pygame.event.get())
    #test les évènements et agit en conséquence
    event.test(perso.etat, perso)
    score=event.collision(score, pygame.sprite.spritecollideany(perso, decor.Sprite_plateforme, pygame.sprite.collide_mask), pygame.sprite.spritecollideany(perso, decor.Sprite_tonneaux, pygame.sprite.collide_mask), pygame.sprite.spritecollideany(perso, decor.Sprite_pique, pygame.sprite.collide_mask), perso, pygame.sprite.spritecollideany(perso, Sprite_en, pygame.sprite.collide_mask), pygame, Sprite_en, pygame.sprite.spritecollideany(perso, decor.Sprite_fondpique, pygame.sprite.collide_mask))
    #test l'état du personnage et agit en conséquence
    perso.etatperso(event.keypressed, perso, event)
    
    #gère l'IA de l'ennemi
    Sprite_en.update(perso.etat, perso.rect.x, perso.rect.y, event.timejump)
    #reinitialisation du personnage à sa position de base
    perso.reinit(event.timeattaque, event.direction, event)
    
    #affichage/actualisation des éléments à l'écran
    fenetre.blit(fond, (0,0))
    fenetre.blit(sol, (0,420))
    decor.affichage(fenetre)
    Sprite_en.draw(fenetre)
    Sprite_perso.draw(fenetre)
    if perso.inv==True:
        fenetre.blit(pygame.image.load(image.persoinv).convert_alpha(), (perso.rect.x,perso.rect.y))
    event.UI(perso, fenetre)
    myfont = pygame.font.SysFont("monospace", 16)
    score_display = myfont.render(str(score), 1, (0,0,0))
    fenetre.blit(score_display, (100, 30))
    pygame.display.update()

#REGENERATION DU TABLEAU------------------------------------------------------------
    
    if pygame.sprite.Group.sprites(Sprite_en)==[]:

        #mise à jour du score
        score+=100
        print(score)
        perso.rect.x=0
        fenetre.blit(fond, (0,0))
        fenetre.blit(sol, (0,420))
        #variables
        image = lib.img.image()
        event = lib.event.event()
        #perso = lib.perso.personnage()
        #Sprite_perso=pygame.sprite.Group()
        #Sprite_perso.add(perso)
        Sprite_en=pygame.sprite.Group()
        #apparition des sprites ennemis
        nbren=random.randrange(1,5)
        for i in range(nbren):
            en=lib.ennemi.ennemi()

            en.rect.x = random.randrange(200,480)
            en.rect.y=random.randrange(200,330)

            Sprite_en.add(en)
        #attaque
        attaque=[]

        #Rafraîchissement de l'écran
        pygame.display.flip()
        pygame.key.set_repeat(40,30)
        fond = pygame.image.load(image.fond).convert()
        fenetre.blit(fond, (0,0))
        sol = pygame.image.load(image.sol).convert()
        fenetre.blit(sol, (0,420))
        Fond=fond.get_rect()
        Sol=sol.get_rect()


        keypressed= []

        #génération du niveau
        decor=lib.classemap.obstacle()
        decor.generation()
        decor.affichage(fenetre)
        fenetre.blit(pygame.image.load(image.trois), (300,200))
        pygame.display.update()
        time.sleep(1)
        fenetre.blit(pygame.image.load(image.deux), (300,200))
        pygame.display.update()
        time.sleep(1)
        fenetre.blit(pygame.image.load(image.un), (300,200))
        pygame.display.update()
        time.sleep(1)

    if perso.vie==0:
        event.continuer=0

while True:
    fenetre.blit(pygame.image.load(image.GM), (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.quit()

print("GAME OVER")
