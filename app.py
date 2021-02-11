import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        pass


def redrawWindow():
    win.fill((64, 64, 64))
    golfBall.draw(win)
    pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    pygame.display.update()


golfBall = ball(300, 494, 5, (255, 255, 255))


run = True
while run:
    pos = pygame.mouse.get_pos()
    line = [(golfBall.x, golfBall.y), pos]
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
