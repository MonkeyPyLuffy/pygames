import pygame
import constantes



class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.shape = pygame.Rect(1,1,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)
        self.shape.center = (x,y)

def update(self):
    cooldown_animacion = 100
    self.image = self.animaciones[self.frame_index]
    if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
       self.frame_index = self.frame_index + 1
       self.update.time = pygame.time.get_ticks()
    if self.frame_index >= len(self.animaciones):
        self.frame_index = 0


    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True      
        if delta_x > 0:
            self.flip = False 
            
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y



    def drawer(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image,self.flip,False)
        interfaz.blit(imagen_flip, self.shape)
        #pygame.draw.rect(interfaz, (253,253,34), self.shape )