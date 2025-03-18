import pygame
from .constant import *
from .plant import Plant
from .tool import Tool

pygame.font.init()
font = pygame.font.Font('resource/ShortStack-Regular.ttf', 25)

class Game:
    def __init__(self):
        self.pArray = []
        self.fruitNum = 0
        for j in range(0, 4):
            for i in range(0, 4):
                self.pArray.append(Plant(180 + i*65, 140 + j*60))
        self.tool = [Tool(500,100,1), Tool(500,300,2)]

    def draw(self):
        for p in self.pArray:
            p.draw()
        for t in self.tool:
            t.draw()
        WIN.blit(pygame.image.load('img/Fruit.png').convert_alpha(), (S_X, S_Y))
        WIN.blit(font.render(str(self.fruitNum), True, BLACK),(S_X, S_Y + 40))
    
    def resetSelected(self):
        for p in self.pArray:
            p.selected = False

    def select_p(self, pos):
        self.resetSelected()
        for num, p in enumerate(self.pArray):
            if p.rect.collidepoint(pos):
                p.selected = True

    def select(self, pos):
        for i, t in enumerate(self.tool):
            if t.rect.collidepoint(pos):
                return i
        return 99

    def water(self, pos):
        for num, p in enumerate(self.pArray):
            if p.rect.collidepoint(pos):
                p.selected = True
    
    def collect(self, pos):
        for num, p in enumerate(self.pArray):
            if p.rect.collidepoint(pos):
                if p.phase >= 6:
                    p.phase = 0
                    if not p.collect:
                        self.fruitNum += 1
                        p.collect = True
                    
        