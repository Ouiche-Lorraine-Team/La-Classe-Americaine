# -*- coding: iso-8859-1 -*-

import pygame
from classes import *

pygame.display.init()

ecran=pygame.display.set_mode((500,500))

niveau=pygame.image.load('niveaupo2.png').convert()

mario_x=0
mario_y = 12*16

scrolling_y = 0

sortie=0
horloge=pygame.time.Clock()

while sortie==0:

        horloge.tick(50)

        for evenement in pygame.event.get():
        
                if evenement.type==pygame.QUIT:
                        sortie=1

        touches=pygame.key.get_pressed()
        
        if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0:
                mario_x+=2
        if touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
                mario_y-=2
                
        if touches[pygame.K_DOWN]==1 and touches[pygame.K_UP]==0:
                mario_y+=2
        
        if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1:
                mario_x-=2
        
        if mario_x<0:
                mario_x=0
        
        elif mario_x>1024-16:
                mario_x=1024-16  

        if mario_x<=1024:
                scrolling_x=0
        
        elif mario_x>512:
                scrolling_x=mario_x-512
                
                if scrolling_x>1024-500:
                        scrolling_x=1024
        
        ecran.blit(niveau,[0,0],[scrolling_x,0,1024,500])
        
        pygame.draw.rect(ecran,(255,0,0),[mario_x-scrolling_x,mario_y,16,16],0)
        
        pygame.display.update()
 
