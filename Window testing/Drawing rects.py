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

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('hi')

screen.fill(background_colour)
pygame.draw.rect(screen, (0, 0, 255),
                 [100, 100, 400, 100], 2)
pygame.draw.rect(screen, (0,   0, 255),
                 [300, 300, 400, 100], 0)

pygame.display.flip()
pygame.display.update()
running = True
while running:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT :
			running = False
        
