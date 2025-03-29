import pygame
import constantes
from personaje import Personaje

pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")

# Cargar múltiples imágenes para la animación
animaciones = []
for i in range(1, 5):  # Suponiendo que tienes 4 imágenes "player_1.png", "player_2.png", etc.
    img = pygame.image.load(f"assets/player_{i}.jpg")
    img = pygame.transform.scale(img, (int(img.get_width() * constantes.SCALA_PERSONAJE), 
                                       int(img.get_height() * constantes.SCALA_PERSONAJE)))
    animaciones.append(img)

# Crear el personaje con la lista de animaciones
player = Personaje(50, 50, animaciones)

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
     
    if mover_derecha:
        delta_x = constantes.VELOCIDAD

    if mover_izquierda:
        delta_x = -constantes.VELOCIDAD

    if mover_arriba:
        delta_y = -constantes.VELOCIDAD

    if mover_abajo:
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

