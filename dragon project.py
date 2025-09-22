# the code below imports pygame libery
import pygame
from pygame import draw, display

# Set up pygame window by inisializing pygame, setting up the screen
# with display.setmode,set caption for the caption and fill for the backround colour
pygame.init()
window = display.set_mode((600, 500))
display.set_caption("A Very big Dragon")
window.fill("cyan")

# set up objects with the pygame.rects method
#the values in the bracket represent the x and y cordinate,the width and height 

background = pygame.Rect(0, 220, 600, 400)
tail  = pygame.Rect(140, 200, 100, 30)
leg  = pygame.Rect(250, 200, 40, 150)
body = pygame.Rect(300, 200, 40, 100)
hand = pygame.Rect(350, 200, 40, 150)
neck = pygame.Rect(400, 190, 46, 46)
face = pygame.Rect(450, 170, 60, 60)
mouth = pygame.Rect(495, 190, 50, 40)
eye1 = pygame.Rect(490, 180, 10, 10)
eye2 = pygame.Rect(460, 180, 10, 10)

# this is the code that was use to make the sun 
pygame.draw.circle(window, "yellow", (50,50), 50)

#draw house objects with the draw . rect method
#the value in the bracket represent the screen the colour and the diffrent parts that are drawn
draw.rect(window, "red", background)
draw.rect(window, "green", tail)
draw.rect(window, "green", leg)
draw.rect(window, "green", body)
draw.rect(window, "green", hand)
draw.rect(window, "green", neck)
draw.rect(window, "green", face)
draw.rect(window, "green", mouth)
draw.rect(window, "grey", eye1)
draw.rect(window, "grey", eye2)
display.flip()
# the code below keeps the window open until u close it 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ✅ handles close button
            running = False

pygame.quit()