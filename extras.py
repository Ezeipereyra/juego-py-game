import pygame
from pygame.locals import *
from configuracion import *
import time


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
        return(" ")
    else:
        return("")


def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)


def dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq,
            posicionesMedio, posicionesDer, puntos, segundos):

    defaultFont = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA)

    font_time_points = pygame.font.Font(
        "RetroGaming.ttf", TAMANNO_LETRA_COUNT)  # fuente agregada por nosotros
    font_candidata = pygame.font.Font("RetroGaming.ttf", TAMANNO_CANDIDATA)
    # Linea del piso
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO-72),
                     (ANCHO, ALTO-72), 5)  # color blanco

    # linea vertical
    pygame.draw.line(screen, (255, 255, 255),
                     (ANCHO//3, ALTO-70), (ANCHO//3, 0), 5)

    # linea vertical
    pygame.draw.line(screen, (255, 255, 255),
                     (2*ANCHO//3, ALTO-70), (2*ANCHO//3, 0), 5)

    # candidata es la palabra que escribe el usuario
    ren1 = font_candidata.render(
        candidata.upper(), 1, COLOR_TEXTO)  # candidata
    ren2 = font_time_points.render(
        "PUNTOS: " + str(puntos), 1, COLOR_TEXTO)  # puntos
    if(segundos < 15):
        ren3 = font_time_points.render(
            "TIEMPO: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)  # tiempo
    else:
        ren3 = font_time_points.render(
            "TIEMPO: " + str(int(segundos)), 1, COLOR_TEXTO)  # tiempo

    for i in range(len(listaIzq)):
        # es como un print
        screen.blit(defaultFont.render(
            listaIzq[i], 1, COLOR_LETRAS), posicionesIzq[i])
    for i in range(len(listaMedio)):
        screen.blit(defaultFont.render(
            listaMedio[i], 1, COLOR_LETRAS), posicionesMedio[i])
    for i in range(len(listaDer)):
        screen.blit(defaultFont.render(
            listaDer[i], 1, COLOR_LETRAS), posicionesDer[i])

    screen.blit(ren1, (ANCHO-822, ALTO-48))
    """estos valores tambien fueron modificados para poder poner la posicion de la candidata donde quisieramos"""
    screen.blit(ren2, (ANCHO-200, 10))
    """tambien fue modificado para posicionar correctamente la solapa 'puntos'"""
    screen.blit(ren3, (10, 10))
