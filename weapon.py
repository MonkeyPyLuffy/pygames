import pygame
import constantes
class arma():
    def __init__(self,image):
        tamaño = (15,15)
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original,self.angulo)
        self.forma = self.imagen.get_rect()
        

    def update(self,personaje):
        self.angulo = 180
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma.center = personaje.shape.center
        self.forma.x = self.forma.x + personaje.shape.width/2



    def dibujar(self,interfaz):
        interfaz.blit(self.imagen,self.forma)    