
from operator import index
import pygame


from configuracion import COLOR_BLANCO


def esta(elem, lista):  # funcion para identificar si un elemento esta dentro de una lista
    for i in lista:
        if elem == i:
            return True
    else:
        return False


def dividirPalabra(palabra):
    cantLetras = len(palabra)
    if cantLetras % 3 != 0 and cantLetras != 4:
        divisor = (cantLetras//3)+1  # ej 3+1
        s1 = palabra[:divisor]  # sintaxis de ":" secuencia [start:end:step]
        # inicia en divisor y finaliza en uno menos, asi no toma una letra de más
        s2 = palabra[divisor:divisor*2-1]
        s3 = palabra[-divisor:]  # inicia de atras para adelante
        # print ("divisor",divisor)
    elif cantLetras == 4:
        divisor = (cantLetras//3)
        s1 = palabra[:divisor]  # sintaxis de ":" seq[start:end:step]
        s2 = palabra[divisor:divisor*2+1]
        s3 = palabra[-divisor:]  # inicia de atras para adelante
        # print ("divisor",divisor)
    else:
        divisor = (cantLetras//3)
        s1 = palabra[:divisor]  # sintaxis de ":" seq[start:end:step]
        s2 = palabra[divisor:divisor*2]
        s3 = palabra[-divisor:]  # inicia de atras para adelante
        # print ("divisor",divisor)
    primeras = list(s1)
    segundas = list(s2)
    terceras = list(s3)
    # print ("1",s1)
    # print ("2",s2)
    # print ("3",s3)
    palabraDividida = [primeras, segundas, terceras]
    return palabraDividida


# def estaCerca(elem, lista):  # ubicacion en Y y la lista de posiciones
#     for sublista in lista:
#         if elem==sublista:
#             return True
#           # retorna cerca segun corresponda


def ubicacionesEnX(inicio, fin):
    ubicacionX = []
    for i in range(inicio, fin, 3):
        ubicacionX.append(i)
    return ubicacionX


def ventanaPuntaje(puntuacion):  # funcion para crear la ventana de puntuacion
    pygame.init()
    resolucion = (1280, 800)
    ventana = pygame.display.set_mode(resolucion)  # seteo la ventana
    imagen_puntos = pygame.image.load("matrix_code.jpg").convert() #cargo la imagen
    pygame.display.set_caption("Gamer Over") #nombre de la ventana

    font = pygame.font.Font("RetroGaming.ttf", 50)  # titulo para la ventana

    # fuente de la letra y color
    texto = font.render("GRACIAS POR JUGAR", 0, (COLOR_BLANCO))

    textoPUNTOS = font.render(
        "TU PUNTAJE FUE DE: " + str(puntuacion), 0, (COLOR_BLANCO))

    run = True  # hago un true para que se ejecute el programa
    if puntuacion <= 25:  # si la puntuacion es menor a 25, hago la siguiente ventana
        while run:
            # abro la ventana con la imagen
            ventana.blit(imagen_puntos, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            ventana.blit(texto, (100, 150))  # cargo la pantalla con el texto
            # cargo la pantalla con el texto
            ventana.blit(textoPUNTOS, (100, 200))
            pygame.display.update()
    else:  # si la puntuacion es igual o mayor a 25
        while run:
            ventana.blit(imagen_puntos, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            ventana.blit(texto, (100, 150))  # cargo la pantalla con el texto
            ventana.blit(textoPUNTOS, (100, 200))
            # cargo la pantalla con el texto
            pygame.display.update()
