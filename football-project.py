import pygame
from pygame import display, font, event
from pygame.locals import *

# Setup display
pygame.init()
screen = display.set_mode()
display.set_caption("football is life 2")
myFont = font.SysFont('arial', 20)  # Choose a font to use in game

# Directions displayed throughout game
directions = "Please press the 'Y' key for yes and the 'N' key for no."

# Counts how many questions have been asked
currentQuestion = 0

# Determines which question to ask
def story(answer, count):
    screen.fill("white")
    if count == 0:
        question1(answer)
    elif count == 1:
        question2(answer)
    elif count == 2:
        question3(answer)
    elif count == 3:
        end(answer)

# Displays the first part of the story
def intro():
    # Break up the string into multiple variables because there isn't text wrapping in Pygame
    intro1 = "Once opon a time there was a 12 year old boy that loved football his name was Nathan."
    intro2 = "he wanted to be a footballer but then he got a really bad injury ."
    intro3 = "but he had a really important game to play a cup final ."
    q1 = "Should he go play the cup game ? Yes or no?"

    screen.fill("white")
    textSurface = myFont.render(intro1, True, "black")
    screen.blit(textSurface, (10, 10))
    textSurface = myFont.render(intro2, True, "black")
    screen.blit(textSurface, (10, 40))
    textSurface = myFont.render(intro3, True, "black")
    screen.blit(textSurface, (10, 70))
    textSurface = myFont.render(q1, True, "black")
    screen.blit(textSurface, (10, 100))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 130))

    # First question
def question1(answer):
    if answer == K_y:
        yes1 = "he goes on to play the cup game and win it he."
        yes2 = "liftes the trophy as his parents watch in proudnes!"
        q2 = "should he be known as the team captain because of his bravery  ? Yes or no?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10,40))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 100))

    elif answer == K_n:
        no1 = "he decided not to play the cup game and his team lost the cup and all the fans were angry at him"
        no2 = "his injury heals ."
        no3 = "he knows he will have to train really hard to get back into the sqaud"
        no4 = "he is so good"
        q2 = "should the coach him bring him back tnto the team early? Yes or no?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))

# Second question
def question2(answer):
    if answer == K_y:
        yes1 = "they are so proud of their son who just won the cup final ."
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))

    elif answer == K_n:
        no1 = "they are so disappointed in him."
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))

    story2 = "He started working hard."
    story3 = "He was focused on training."
    story4 = "Real Madrid comes calling to sign him."
    q3 = "should he sign for Real Madrid, Yes or No?"

    textSurface = myFont.render(story2, True, "black")
    screen.blit(textSurface, (10, 40))
    textSurface = myFont.render(story3, True, "black")
    screen.blit(textSurface, (10, 70))
    textSurface = myFont.render(story4, True, "black")
    screen.blit(textSurface, (10, 100))
    textSurface = myFont.render(q3, True, "black")
    screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 160))

# Third question
def question3(answer):
    if answer == K_y:
        yes1 = "Yes he decided to join Real Madrid,"
        yes2 = "He took the number 38."
        yes3 = "saying it gave him luck"
        yes4 = "His first game for Real Madrid was agianst his boyhood club."
        q4 = "Should he play the game knowing he is gonna get targeted or should he skip the game?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(yes3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(yes4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))

    elif answer == K_n:
        no1 = "he said no that this is the team that brought him up."
        no2 = "But Real Madrid wasn't having it" 
        no3 = "So they gave him an offer that to good to refuse."
        no4 = "And the offer is 250,000 a week the team will cover everything like his plane tickets his cars and houses."
        q4 = "Should he accept the offer? Yes or No?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))

# Ending
def end(answer):
    if answer == K_y:
        yes1 = "He decided to play the full 90 minutes ."
        end1 = "all through the 90 minutes he kept getting slide tackled!"
        end2 = "His boyhood teams fans were shouting insult at him."
        end3 = "And then when he was threw on goal one of there defenders fouled him so hard he broke his ankle."
        end4 = "He nhad the choice of playing or get taken to the hosipital he decided to play"
        end5 = "And at full time the scores were 4:0 to Real Madrid with Nathan scorig all four goals to shush his old teams fans"
        end6 = "The end!"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(end5, True, "black")
        screen.blit(textSurface, (10, 160))
        textSurface = myFont.render(end6, True, "black")
        screen.blit(textSurface, (10, 190))

    elif answer == K_n:
        no1 = "He decided to reject the offer he said he will not chose money over his team."
        end1 = "The next day when he went to his locker he found papers of Real Madrid supporters threatening him"
        end2 = "He took it serious and in the next match they were playing Real Madrid perfect time to show the fans who is boss he said."
        end3 = "The fans were saying stuff about nathans parents nathan replied by scoring 3 goals to win the game for his team."
        end4 = "The end!"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 130))

# Game loop
running = True
while running:
    # Check for events
    for currentEvent in pygame.event.get():
        if currentEvent.type == QUIT:
            running = False
        elif currentEvent.type == KEYDOWN:
            if currentQuestion == 0:
            
                story(currentEvent.key, currentQuestion)
                currentQuestion += 1
            elif currentQuestion < 4:
                
                story(currentEvent.key, currentQuestion)
                currentQuestion += 1
            elif currentQuestion == 4 and currentEvent.key == K_r:
                # Restart the game
                currentQuestion = 0
                intro()

    # Show intro screen at the start
    if currentQuestion == 0:
        intro()

    # Update the display every frame
    pygame.display.update()

pygame.quit()
