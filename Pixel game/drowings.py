import pygame
import pygame.freetype
import math

pygame.init()
win = pygame.display.set_mode((500, 450))
bg_img = pygame.image.load('gras_BG.png')
bg = pygame.transform.scale(bg_img, (500, 450))

def isCollision(opstakelX,opstakelY,x,y):
    distance = math.sqrt(math.pow(opstakelX-x,2)) + (math.pow(opstakelY-y,2))
    if distance <50:
        return True
    else:
        return False


black = (0, 0, 0)
wite = (255, 255, 255)
red = (255, 0, 0)
size = [500, 450]
x = 20
y = 380
opstakelX = 250
opstakelY = 379
boxX = 225
boxY = 359
radius = 15
vel_x = 10
vel_y = 10
i = 0
width = 500
jump = False

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
tetX= 10
testY = 10

def show_score(x,y):
    score = font.render("Score:" + str(score_value), True, (wite))
    screen.blit(score, (x, y))

screen = pygame.display.set_mode(size)
screen.fill(wite)
pygame.display.set_caption("Pixel Game")

done = False    
clock = pygame.time.Clock()    
while not done:
    win.fill((wite))
    clock.tick(10)

    win.fill((0,0,0))
    win.blit(bg, (i, 0))
    win.blit(bg, (width+i, 0))
    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0
    i -= 1
    boxX -=5
    opstakelX -=5
    if boxX < -20:
        boxX = 500
    if opstakelX < -20:
        opstakelX = 500

    if pygame.time.wait(100):
        score_value = score_value + 1
  
    show_score(tetX, testY)

    # Player
    player = pygame.draw.circle(win, (black), (int(x), int(y)), radius)
    # graund     
    graund = pygame.draw.rect(screen, black, [0, 400, 500, 400])
    # opstakel
    opstakel = pygame.draw.rect(screen, red, [boxX, boxY, 50, 40])


    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False


    userInput = pygame.key.get_pressed()
    #Movment
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y
        vel_y -= 1
        if vel_y <-10:
            jump = False
            vel_y = 10

    #collision
    collision = isCollision(opstakelX,opstakelY, x, y)
    if collision:
        score_value -=5


    pygame.time.delay(20)

    pygame.display.update()

    if event.type == pygame.QUIT:
            done = True

pygame.quit()