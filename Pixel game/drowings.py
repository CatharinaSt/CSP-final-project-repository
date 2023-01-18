# Vigual code from: https://www.javatpoint.com/how-to-develop-a-game-in-python
# player movment code from https://www.youtube.com/@MaxTeachesTech
# backgraund https://www.freepik.com/premium-vector/pixel-art-game-background-grass-sky-clouds_9047947.htm
# score & collison https://www.youtube.com/@buildwithpython
import pygame
import sys
import os
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
    boxX -=2
    opstakelX -=2

    
  
    show_score(tetX, testY)

    # Player
    player = pygame.draw.circle(win, (black), (int(x), int(y)), radius)
    # graund     
    graund = pygame.draw.rect(screen, black, [0, 400, 500, 400])
    # opstakel
    opstakel = pygame.draw.rect(screen, red, [boxX, boxY, 50, 40])

    # add a box in a random position in a given coordanit fild, limet the number of boxes to a surten amout

    # coler map the boxes and player so that if they get hit tehy die

    # if euf time add helth bar, if not slap a rage game label on it

        # if helth bar added add boxes that hel player

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
    # if pygame.sprite.spritecollideany(player, objects, pygame.sprite.collide_mask):
    #         screen.fill((255, 255, 255))
    # else:
    #     screen.fill((30, 30, 30))


    userInput = pygame.key.get_pressed()
    #Movment
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x
    # y > 0:
    #     y -= vel_y
    # if y < 500:
    #     y += vel_y

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    # up button moves up by some amount
    # if max jump height is reached or button is released
    # then jump is true
    #since the sprite is not on the ground, jump is true
    if jump is True:
        y -= vel_y
        vel_y -= 1
        if vel_y <-10:
            jump = False
            vel_y = 10

    #collision
    collision = isCollision(opstakelX,opstakelY, x, y)
    if collision:
        score_value -=1


    pygame.time.delay(20)

    pygame.display.update()

    if event.type == pygame.QUIT:
            done = True

pygame.quit()




# Code grave yard

# update_player_position()

# def update_player_position():
#     global player_x
#     global player_y
#     global player_x_direction
#     global player_y_direction
#     if player_x_direction > 0:
#        if player_x < 450 - player_width:
#             player_x += player_x_direction * player_speed
#     if player_x_direction > 0:
#        if player_x > 0:
#             player_x += player_x_direction * player_speed
#     if player_y_direction > 0:
#        if player_y < 450 - player_height:
#             player_y += player_y_direction * player_speed
#     if player_y_direction > 0:
#        if player_y > 0:
#             player_y += player_y_direction * player_speed


#if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player_x_direction = -1
        #     if event.key == pygame.K_RIGHT:
        #         player_x_direction = 1
        #     if event.key == pygame.K_UP:
        #         player_y_direction = -1
        #     if event.key == pygame.K_DOWN:
        #         player_y_direction = 1 
        # if event.type == pygame.KEYUP:
        #     # if event.key == pygame.K_LEFT:
        #     player_x_direction = 0
        #     # if event.key == pygame.K_RIGHT:
        #     player_x_direction = 0
        #     # if event.key == pygame.K_UP:
        #     player_y_direction = 0
        #     # if event.key == pygame.K_DOWN:
        #     player_y_direction = 0

        # if event.type == pygame.KEYDOWN:
        #         # Jumping
        #         if event.key == pygame.K_UP:
        #             global gravity
        #             gravity = -10

        # def physics(keys_pressed, player):
        #     global gravity
        #     gravity += 0.8
        #     player_y += gravity

        #     if keys_pressed[pygame.K_LEFT]:
        #         player_x -= player_speed
        #     if keys_pressed[pygame.K_RIGHT]:
        #         player_x += player_speed

        # def input():