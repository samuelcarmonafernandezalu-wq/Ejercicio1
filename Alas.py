import Arma
import pygame

class Alas(Arma.Arma):
    def __init__(self):
        self.__alasOn=pygame.image.load('./AlasOn.png')

    def enciende(self,screen):
        screen.blit(self.__alasOn,(0,0))
        pygame.display.flip()
    
    def grito(self):
        print('¡¡¡¡¡A volar!!!!')