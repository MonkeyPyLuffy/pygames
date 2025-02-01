import pygame

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0,0,20,20)
        self.shape.center = (x,y)
    
    def movimiento(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y



    def drawer(self, interfaz):
        pygame.draw.rect(interfaz, (253,253,34), self.shape )