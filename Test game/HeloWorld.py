#code from https://www.javatpoint.com/how-to-develop-a-game-in-python
import pygame
from math import pi

pygame.init()    
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Pixel Game")    
done = False   
clock = pygame.time.Clock()  
    
while not done:    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            done = True    
    pygame.display.flip()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True

screen.fill((0, 0, 0)) 

# Draw on the screen a green line which is 5 pixels wide.    
pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 30], 5)