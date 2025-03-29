import pygame
import constantes

import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones  # Lista de imágenes
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones[self.frame_index]
        self.shape = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True      
        if delta_x > 0:
            self.flip = False 

        self.shape.x += delta_x
        self.shape.y += delta_y

        # Si hay movimiento, actualizar animación
        if delta_x != 0 or delta_y != 0:
            self.update()

    def update(self):
        """Actualizar el frame de la animación."""
        cooldown_animacion = 100  # Milisegundos entre cada frame
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - self.update_time >= cooldown_animacion:
            self.update_time = tiempo_actual
            self.frame_index += 1

            # Volver al primer frame si llegamos al final
            if self.frame_index >= len(self.animaciones):
                self.frame_index = 0

            self.image = self.animaciones[self.frame_index]

    def drawer(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.shape.topleft)
