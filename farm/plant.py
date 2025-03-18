import pygame
from .constant import *
from .fruit import Fruit

pImg = []
for i in range(1,8):
    pImg.append(pygame.image.load("img/Stage_%d.png" %(i)).convert_alpha())

class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, P_WIDTH, P_HEIGHT)
        self.prect = pygame.Rect(x + P_WIDTH/4, y - P_HEIGHT/4 - 15, pImg[0].get_width(), pImg[0].get_height())
        self.selected = False
        self.phase = 0
        self.timer = 0
        self.fruit = Fruit(x + P_WIDTH/2, y + P_WIDTH/4)
        self.collect = False

    def draw(self):
        if self.selected:
            pygame.draw.rect(WIN, DARK_BROWN, self.rect, 0, 20)
            self.timer += 1
            if self.timer > 100:
                self.phase += 1
                self.selected = False
                self.timer = 0
            if self.phase >= 7:
                self.phase = 6
        else:
            pygame.draw.rect(WIN, BROWN, self.rect, 0, 20)

        if self.collect:
            self.collect = self.fruit.move()
        else:
            self.fruit = Fruit(self.x + P_WIDTH/2, self.y + P_WIDTH/4)

        WIN.blit(pImg[self.phase], (self.prect[0], self.prect[1]))
        