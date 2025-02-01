import pygame
import constantes
from personaje import Personaje

player = Personaje(50, 50)

pygame.init()
screen =  pygame.display.set_mode((constantes.ALTO_VENTANA,
                                   constantes.ANCHO_VENTANA ))
pygame.display.set_caption("mi primer juego")

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

running = True
while running:

      reloj.tick(constantes.FPS)


      screen.fill(constantes.COLOR_BG)

      delta_x = 0
      delta_y = 0
     
      if mover_derecha == True:
        delta_x = constantes.VELOCIDAD

      if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD

      if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD

      if mover_abajo == True:
        delta_y = constantes.VELOCIDAD          

      player.movimiento(delta_x, delta_y)


player.drawer(screen)
for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
              mover_izquierda = True

           if event.key == pygame.K_d:
             mover_derecha = True

           if event.key == pygame.K_w:
            mover_arriba = True

           if event.key == pygame.K_s:
            mover_abajo = True



           if event.type == pygame.KEYUP: 
              if event.key == pygame.K_a:
                 mover_izquierda = False

           if event.key == pygame.K_d:
             mover_derecha = False

           if event.key == pygame.K_w:
            mover_arriba = False

           if event.key == pygame.K_s:
            mover_abajo = False














pygame.display.update()



pygame.quit()