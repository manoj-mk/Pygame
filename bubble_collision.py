print("WELCOME TO BUBBLE GAME".center(50,"*"))
print(">ENTER SPACE TO CREATE A BUBBLE".rjust(40,"="))
print(">ENTER UP TO DELETE A BUBBLE".rjust(40,"="))

import pygame
import random
from random import randint
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
surface = pygame.Surface((100, 100))
done = False
class Bubble(object):
    WIDTH = 800
    HEIGHT = 600
    def __init__(self,size,speed,screen,x=0,y=0):
        self.size = size
        self.speed = speed
        self.xSpeed = speed
        self.ySpeed = speed
        self.screen = screen
        self.color = (randint(1,255), randint(1,255), randint(1,255))
        self.x = x
        self.y = y
    def set_color(self,color):
        self.color = color
    def run_bubble(self):
        if(self.x<=self.size):
            self.xSpeed = self.speed
        if(self.y<=self.size):
            self.ySpeed = self.speed
        if(self.x>=WIDTH-self.size):
            self.xSpeed = -self.speed
        if(self.y>=HEIGHT-self.size):
            self.ySpeed = -self.speed
        self.x+=self.xSpeed
        self.y+=self.ySpeed
        # pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.size)
bubble_stack = []
N = 3
for i in range(N):
    b = Bubble(randint(10,100),randint(1,4),screen,randint(0,WIDTH),randint(0,HEIGHT))
    bubble_stack.append(b)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    t = Bubble(randint(10,50),randint(1,4),screen,randint(0,WIDTH),randint(0,HEIGHT))
                    bubble_stack.append(t)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    bubble_stack.pop()

        screen.fill((0, 0, 1))
        for b in bubble_stack:
            b.run_bubble()
        pygame.display.flip()
        clock.tick(60)