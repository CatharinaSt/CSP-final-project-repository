import pygame
import random

screen_width = 500
screen_height = 500

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()


black = (0, 0, 0)
red = (255,0,0)
blue = (0, 0, 255)

fps = 30


#the size of our player square
playerSize = 50

#rectangles get declared with x, y, w, h
obstacle = [0, 0, 350, 50]


obstacleMoveSpeed = 5
#how fast to move obstalce down


def check_collision(playerRect, obstacleRect):
    #convert rectangles into x,y,w,h
    playerX = playerRect[0]
    playerY = playerRect[1]
    playerWidth = playerRect[2]
    playerHeight = playerRect[3]

    obstacleX = obstacle[0]
    obstacleY = obstacle[1]
    obstacleWidth = obstacle[2]
    obstacleHeight = obstacle[3]

    #get the right left top and bottom
    myRight = playerX + playerWidth
    myLeft = playerX
    myTop = playerY
    myBottom = playerY + playerHeight

    otherRight = obstacleX + obstacleWidth
    otherLeft = obstacleX
    otherTop = obstacleY
    otherBottom = obstacleY + obstacleHeight

    #now the collision code
    collision = True

    if ((myRight < otherLeft) or (myLeft > otherRight) or (myBottom < otherTop) or (myTop > otherBottom)):
        collision = False


    return collision

"""def randomOb(randomize, obstacle, obstacle2):



                if randomize == 0:
                        pygame.draw.rect(screen, red, obstacle)
                        obstacle = [0, 0, 350, 50]
                        randomize = random.randrange(0,2)
                if randomize == 1:
                        pygame.draw.rect(screen, red, obstacle2)
                        obstacle2 = [150, 0, 410, 50]
                        randomize = random.randrange(0,2)

                randomize = random.randrange(0,2)
                return randomize"""

def game_loop():


        randomize = random.randrange(0,2)
        playerRect = [(screen_width / 2)-(playerSize/2), 400, playerSize, playerSize]
        screen_padding = random.randint(0, 100)
        #(screen_width / 2)-(playerSize/2) just figures out how to center the player
        while 1:

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        playerRect = [(screen_width * 0.2)-(playerSize/2), 400, playerSize, playerSize]
                                if event.key == pygame.K_RIGHT:
                                        playerRect = [(screen_width * 0.8)-(playerSize/2), 400, playerSize, playerSize]
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        playerRect = [(screen_width / 2)-(playerSize/2), 400, playerSize, playerSize]







                #move obstacle downward
                obstacle[1] = obstacle[1] + obstacleMoveSpeed



                if (check_collision(playerRect, obstacle)):
                        print("COLLISION")
                if obstacle[1] > screen_height + screen_padding:
                        obstacle[1] = -50
                        screen_padding = random.randint(0, 100)
                        orientation = bool(random.getrandbits(1))
                        if orientation:
                                obstacle[0] = 0
                        else:
                                obstacle[0] = 150



                #drawing code
                screen.fill(black)


                #draw our player
                pygame.draw.rect(screen, blue, playerRect)

                pygame.draw.rect(screen, red, obstacle)

                """randomOb(randomize, obstacle, obstacle2)
                if obstacle[1] > 500 or obstacle2[1] > 500:
                        randomize = random.randrange(0,2)
                        randomOb(randomize, obstacle, obstacle2)"""


                pygame.display.update()

                clock.tick(fps)


game_loop()