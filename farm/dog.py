import pygame
from .constant import *

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image

    def get_frame(self,frame,width,height,scale):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0),((frame*width), 0, width,height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(BLACK)
        
        return image

class Dog:
    def __init__(self):
        self.sheet = pygame.image.load('img/dog.png').convert_alpha()
        self.frame = 0

    