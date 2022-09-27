from time import sleep
import pygame
pygame.init()



windowSize = [1366, 768]
screen = pygame.display.set_mode(windowSize)
backcolour = pygame.color.Color('#010520')

#sets the window size
gameDisplay = pygame.display.set_mode((1366, 768))
pygame.display.set_caption('Menu')

#loads in your pics to use later
Titlep = pygame.image.load('Title PYCADE.png')


#DISPLAY BACKGROUND
pygame.display.update()
# sleep(1)


finished = False
while not finished:
    screen.fill(backcolour)
    gameDisplay.blit(Titlep, (265,40))
    pygame.display.flip()
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        finished = True 


#DISPLAY YOU ARE HERE

#GAME WILL NOW EXIT UNLESS YOU LOOP IT OR ADD AN input

   
pygame.quit()
quit()
