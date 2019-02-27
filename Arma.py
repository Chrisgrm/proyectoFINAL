import pygame

class proyectil(object):
    def __init__(self, x,y, radio, color, lado ):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.lado = lado
        self.vel = 8 * lado

    def draw(win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)
