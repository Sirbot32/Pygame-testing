import pygame
import random as r

red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
purple = (255,0,255)
green = (0,255,0)
cyan = (0,255,255)


background_colour = (cyan)

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('hi')

screen.fill(background_colour)


pygame.display.flip()

running = True
while running:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT :
			running = False
        
