#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scrolling.py
#  
#  Copyright 2013 Lukas <lukas@JeanMi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	return 0

if __name__ == '__main__':
	main()

# -*- coding: iso-8859-1 -*-

import pygame

pygame.display.init()

ecran=pygame.display.set_mode((320,240))

niveau=pygame.image.load('niveaupo2.png').convert()

mario_x=32
mario_y=192

speed=[5,5]

sortie=0
horloge=pygame.time.Clock()

while sortie==0:
    
    horloge.tick(50)
    
    for evenement in pygame.event.get():
		if evenement.type==pygame.QUIT:
			sortie=1
    
    touches=pygame.key.get_pressed()
    
    if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0:
	mario_x+=4
	   
    elif touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1:
	mario_x-=4
	    
    if touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
	mario_y-=4
	
    elif touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==1:
	mario_y+=4
    
    if mario_x<0:
	mario_x=0
    
    elif mario_x>640-16:
	mario_x=640-16 
    
    if mario_x<=152:
	scrolling_x=0
    
    elif mario_x>152:
	scrolling_x=mario_x-152
	   
	if scrolling_x>640-320:
	    scrolling_x=320
    
    if mario_y<130:
	mario_y=130
			    
    elif mario_y>192:
	mario_y=192

    ecran.blit(niveau,[0,0],[scrolling_x,0,320,240])
    
    pygame.draw.rect(ecran,(255,0,0),[mario_x-scrolling_x,mario_y,16,16],3)
    
    pygame.display.update()
 
## Quitte pygame
pygame.quit()
