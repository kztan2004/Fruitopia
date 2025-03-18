import pygame
from farm.constant import *
from farm.game import Game

pygame.init()

pygame.display.set_caption("Farm")

def main():
    t_num = 99
    clock = pygame.time.Clock()
    run = True
    game = Game()
    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)
        game.draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    t_num = game.select(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    t_num = 99
            
            if event.type == pygame.MOUSEMOTION:
                if t_num != 99:
                    game.tool[t_num].rect.move_ip(event.rel)
                    if t_num == 0:
                        game.water(event.pos)
                    elif t_num == 1:
                        game.collect(event.pos)
                    
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
main()