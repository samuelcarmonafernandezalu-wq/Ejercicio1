import Arma
import pygame

class VientosHuracanados(Arma.Arma):
    def __init__(self):
        self.__vientosOn=pygame.image.load('./VientosOn.png')

    def enciende(self,screen):
        screen.blit(self.__vientosOn,(0,0))
        pygame.display.flip()

    def grito(self):
        print('¡¡¡¡¡Vientos Huracanados!!!!')