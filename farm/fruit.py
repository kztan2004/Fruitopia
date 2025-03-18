import pygame
from .constant import *
fImg = pygame.image.load('img/Fruit.png').convert_alpha()
fImg = pygame.transform.scale(fImg,(int(fImg.get_width() * 0.75), int(fImg.get_height() * 0.75)))

class Fruit:
    def __init__(self, x, y):
        self.rect = fImg.get_rect()
        self.rect.center = (x,y)
        self.dX = abs(self.rect.x - S_X)
        self.dY = abs(self.rect.y - S_Y)
        self.stpScale = 3
        self.stpX = 1
        self.stpY = 1
        self.errX = 0
        self.errY = 0
        self.count = 0
        if self.dX > self.dY:
            self.stpX = self.dX/self.dY
            self.errX = round(self.dX/(self.dX % self.dY))
        elif self.dX < self.dY:
            self.stpY = self.dY/self.dX
            self.errY = round(self.dY/(self.dY % self.dX))

    def draw(self):
        WIN.blit(fImg, (self.rect.x, self.rect.y))

    def move(self):
        if not (self.rect.x >= S_X - 10 and self.rect.y <= S_Y + 10):
            count = 0
            if self.rect.x >= S_X - 10:
                self.stpX = 0
            if self.rect.y <= S_Y + 10:
                self.stpY = 0

            if self.errX > 0:
                if self.count >= self.errX:
                    self.rect.x += 1
                    self.count = 0
            elif self.errY > 0:
                if self.count >= self.errY:
                    self.rect.y -= 1
                    self.count = 0

            self.count += self.stpScale + 1
            self.rect.x += self.stpX * self.stpScale
            self.rect.y -= self.stpY * self.stpScale
            WIN.blit(fImg, (self.rect.x, self.rect.y))
            return True
        return False