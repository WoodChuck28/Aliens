import pygame
import time
import random

pygame.init()


green = (0, 125, 0)
blue = (0, 0, 200)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

displayW = 800
displayH = 600

fps = 15
block = 10

gameDisplay = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption('Chuck\'s Snake')


font = pygame.font.SysFont(None, 25)
def game_message(txt, color):
    text_on_screen = font.render(txt, True, color)
    gameDisplay.blit(text_on_screen, [displayW/2, displayH/2])

def snake(block, snakelist):
    for x_and_y in snakelist:
        pygame.draw.rect(gameDisplay, red, [x_and_y[0], x_and_y[1], block, block])


def gameLoop():
    gameExit = False
    gameOver = False

    snakelist = []
    snakeLength = 1

    lead_x =displayW/2
    lead_y = displayH/2

    xaxis_move = 0
    yaxis_move = 0

    randAppleX = round(random.randrange(0, displayW - block)/10.0) * 10
    randAppleY = round(random.randrange(0, displayH - block)/10.0) * 10

    while not gameExit:

        gameDisplay.fill(white)



        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSeg in snakelist [:-1]:
            if eachSeg == snakeHead:
                gameOver = True

        snake(block, snakelist)
        pygame.draw.rect(gameDisplay, blue, [randAppleX, randAppleY, block, block])

        pygame.display.update()
        lead_x += xaxis_move
        lead_y += yaxis_move
        clock.tick(fps)
        if lead_x >= displayW or lead_x < 0 or lead_y >= displayH or lead_y < 0:
            gameOver = True

        while gameOver == True:
            gameDisplay.fill(white)
            game_message("Game Over, press z to play again or Q to quit", red)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        gameLoop()
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xaxis_move = -block
                    yaxis_move = 0
                elif event.key == pygame.K_RIGHT:
                    xaxis_move = block
                    yaxis_move = 0
                elif event.key == pygame.K_UP:
                    yaxis_move = -block
                    xaxis_move = 0
                elif event.key == pygame.K_DOWN:
                    yaxis_move = block
                    xaxis_move = 0
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, displayW - block)/10.0) * 10
            randAppleY = round(random.randrange(0, displayH - block)/10.0) * 10
            snakeLength += 1


    pygame.quit()
    quit()

gameLoop()
