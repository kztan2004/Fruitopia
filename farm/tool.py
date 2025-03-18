import pygame
from .constant import *

toolImg = [pygame.image.load('img/tool.png').convert_alpha(), pygame.image.load('img/Scythe.png').convert_alpha()]

class Tool:
    def __init__(self, x, y, tNum):
        self.x = x
        self.y = y
        self.tNum = tNum - 1
        self.rect = pygame.Rect(x, y, toolImg[self.tNum].get_height(), toolImg[self.tNum].get_width())

    def draw(self):
        WIN.blit(toolImg[self.tNum], (self.rect[0], self.rect[1]))