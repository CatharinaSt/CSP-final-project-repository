# Vigual code from: https://www.javatpoint.com/how-to-develop-a-game-in-python
# player movment code from https://youtu.be/hsJ7K301mEU
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

black = (0, 0, 0)
wite = (255, 255, 255)
size = [500, 450]
x = 20
y = 380
radius = 15
vel_x = 10
vel_y = 10
jump = False

screen = pygame.display.set_mode(size)
screen.fill(wite)
pygame.display.set_caption("Pixel Game")

done = False    
clock = pygame.time.Clock()    
while not done:
    win.fill((wite))
    clock.tick(10)

    # Player
    pygame.draw.circle(win, (black), (int(x), int(y)), radius)
    # graund     
    pygame.draw.rect(screen, black, [0, 400, 500, 400])
    # opstakel     
    pygame.draw.rect(screen, black, [200, 349, 50, 50])


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