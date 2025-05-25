import pygame
import constantes
import math
class Arma():
    def __init__(self,image,imagen_bala):
        #size = (15,15)
        self.imagen_bala = imagen_bala
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original,self.angulo)
        self.forma = self.imagen.get_rect()
        self.disparar = False
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self,personaje):
        #self.angulo = 0
        disparo_cooldown = constantes.COOLDOWN_BALAS
        bala = None
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma.center = personaje.forma.center

        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/3
            self.rotar_arma(False)
        else:
            self.forma.x = self.forma.x - personaje.forma.width/3
            self.rotar_arma(True)
        
        #Pistola  + Mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = - mouse_pos[1] - self.forma.centery
        self.angulo = math.degrees(math.atan2(distancia_y,  distancia_x))
        print(self.angulo)

        if pygame.mouse.get_pressed()[0] and self.disparar == False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_cooldown):
           bala = Bala(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
           self.disparar = True
        if pygame.mouse.get_pressed() == False:
            self.disparar = False
        return bala


        #self.forma.x  =  self.forma.x + personaje.forma.width/3
        self.forma.y = self.forma.y + 23

    def rotar_arma(self, rotar):
        if rotar == True:
           imagen_flip = pygame.transform.flip(self.image_original, True, False)
           self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.image_original, False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self,interfaz):
        interfaz.blit(self.imagen,self.forma)

class Bala(pygame.sprite.Sprite):
    def __init__(self,image, X, Y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (X,Y)
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
        self.delta_y = -math.sin(math.radians(self.angulo))*constantes.VELOCIDAD_BALA

    def update(self):
        self.rect.x = self.rect.x + self.delta_x
        self.rect.y = self.rect.y + self.delta_y

        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VENTANA:
           self.kill()

    def dibujar(self,interfaz):
        interfaz.blit(self.image, (self.rect.centerx,
                                  self.rect.centery - int(self.image.get_height()/2)))