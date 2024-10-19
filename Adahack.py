import time
import random
import pygame
import sys

from pygame.locals import *

def generate_mathQ():
    answer = 0
    Wanswers = []
    li_op = ["+", "-", "*", "/"]
    first = random.randint(-157,852)
    second = random.randint(-71,295)
    li_index = random.randint(0,3)
    string = str(first) + " " + str(li_op[li_index]) + " " + str(second)
    if li_index == 0:
        answer = first + second
    if li_index == 1:
        answer = first - second
    if li_index == 2:
        answer = first * second
    if li_index == 3:
        quo = first // second 
        rem = first % second
        answer = [quo, rem]
    
    if li_index <= 2:
        for i in range(3):
            deviation = abs (answer // 8)
            Wanswer = answer + random.randint(-1 * deviation, deviation)
            if Wanswer != answer:
                Wanswers.append(Wanswer)
            else:
                i -= 1
    else:
        for i in range(3):
            deviation_quo = abs(quo // 3)
            deviation_rem = abs(rem // 5)
            Wanswer = [quo + random.randint(-1 * deviation_quo, deviation_quo), rem + random.randint(-1 * deviation_rem, deviation_rem)]
            if Wanswer != answer:
                Wanswers.append(Wanswer)
            else:
                i -= 1
    return string,li_index,answer,Wanswers


for i in range(10):
    print(generate_mathQ())

pygame.init()
mainClock = pygame.time.Clock()

screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Hungry Hopper')

font = pygame.font.SysFont(None, 30)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((255,255,255))
        draw_text('Main Menu', font, (0,0,0), screen, 545, 250)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(500, 300, 200, 50)
        button_2 = pygame.Rect(500, 400, 200, 50)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                scoreboard()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), screen, 575, 315)
        draw_text('SCOREBOARD', font, (255,255,255), screen, 530, 415)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
 
        pygame.display.update()
        mainClock.tick(60)


def game():

    happy = pygame.image.load('/Users/user/Downloads/happy.webp')
    happy = pygame.transform.scale(happy, (300, 300))

    sad = pygame.image.load('/Users/user/Downloads/sad.webp')
    sad = pygame.transform.scale(sad, (300, 300))

    tired = pygame.image.load('/Users/user/Downloads/tired.webp')
    tired = pygame.transform.scale(tired, (300, 300))

    dead = pygame.image.load('/Users/user/Downloads/dead.png')
    dead = pygame.transform.scale(dead, (300, 300))

    running = True
    while running:
        screen.fill((0,0,0))
        counter, text = 30, '30'.rjust(3)

        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)
        question = generate_mathQ()
        run = True
        while run:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else "Hopper's Dead"

                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        running = False

            screen.fill((255, 255, 255))
            screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))

            answerss = [question[1]]
            for i in range(2):
                answerss.append(question[3][i])
            random.shuffle(answerss)

            if counter > 0:
                screen.blit(font.render(f'A. {question[0]}', True, (0, 0, 0)), (32, 200))
                screen.blit(font.render(f'B. {answerss[0]}', True, (0, 0, 0)), (50, 250))
                screen.blit(font.render(f'C. {answerss[1]}', True, (0, 0, 0)), (50, 300))
                screen.blit(font.render(f'D. {answerss[2]}', True, (0, 0, 0)), (50, 350))
            
                

        
            if counter >= 21:
                screen.blit(happy, (600,300))
            if 11 <= counter <= 20:
                screen.blit(tired, (600,300))
            if 1 <= counter <= 10:
                screen.blit(sad, (600,300))
            if counter <= 0:
                screen.blit(dead, (600,300))


            pygame.display.flip()
            mainClock.tick(60)


def scoreboard():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('SCOERBOARD', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
#countdown

def countdown(input):
    elapsed = input
    while elapsed > 0:
        print(input-elapsed)
        time.sleep(0.05)
        elapsed -= 0.05
    return "T!mesUp" 

# countdown(int(input("time u wan: ")))




scoreboard = {}

def addteam():
    ggroup = input()






