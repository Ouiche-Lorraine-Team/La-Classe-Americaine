#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sans titre.py
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

import sys, pygame

pygame.init()

size = width, height = 320, 240
speed_x = 0
speed_y = 0

screen = pygame.display.set_mode(size)

niveau=pygame.image.load('niveaupo2.png').convert()

mario = pygame.image.load("mario.png")
mariorect = mario.get_rect()

mario_x = 20
mario_y = 180

horloge = pygame.time.Clock()

sortie=0

while sortie==0:
	
	horloge.tick(50)
	
	for evenement in pygame.event.get():
		if evenement.type==pygame.QUIT:
			sortie=1
	
	touches=pygame.key.get_pressed()
	
	if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0:
		speed_x+=2
	   
	elif touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1:
		speed_x-=2
	    
	if touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
		speed_y-=2
	
	elif touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==1:
		speed_y+=2
		
	if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==0:
		speed_x=0
	
	if touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==0:
		speed_y=0
		
	if mario_x<0:
		mario_x=0
	
	elif mario_x>640-16:
		mario_x=640-16 
	
	if mario_x<=152:
		scrolling_x=0
	
	elif mario_x>152:
		scrolling_x=speed_x-152
	   
	if scrolling_x>640-320:
	    scrolling_x=320
	    
	if speed_x>3:
		speed_x=3
		
	elif speed_x<-3:
		speed_x=-3
	
	if speed_y>3:
		speed_y=3

	elif speed_y<-3:
		speed_y=-3
	
	#~ 
	#~ if mario_y<130:
		#~ speed_y=130
			    #~ 
	#~ elif mario_y>192:
		#~ speed_y=192
	
	screen.blit(niveau,[0,0],[scrolling_x,0,320,240])
		
	mariorect = mariorect.move(speed_x, speed_y)
	
	screen.blit(mario, mariorect)
	pygame.display.flip()
	
pygame.quit()
