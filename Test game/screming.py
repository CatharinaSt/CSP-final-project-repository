import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 250
y = 250
radius = 15
vel = 10

run = True
while run:

    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False

    
    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT]:
        x -= vel
    if userInput[pygame.K_RIGHT]:
        x += vel
    if userInput[pygame.K_UP]:
        x -= vel
    if userInput[pygame.K_DOWN]:
        x -= vel

    pygame.display.update()
