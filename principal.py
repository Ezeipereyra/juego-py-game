#! /usr/bin/env python
from funcionesVACIAS import *
import os

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
from nuestrasFunciones import*

# importar el menu de pygame
import pygameMenu
from pygameMenu.locals import *


# Init pygame
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

# ventana
surface = pygame.display.set_mode(TAMANO_PANTALLA)
pygame.display.set_caption("MATRIX GAME")
clock = pygame.time.Clock()
dt = 1 / FPS

pygame.mixer.music.load("musica.menu.mp3")  # Musica del menu
pygame.mixer.music.play(10)


def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    # tiempo en el que el usuario estuvo en el menu
    tiempoMenu = pygame.time.get_ticks()
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("MATRIX Game")
    screen = pygame.display.set_mode((ANCHO, ALTO))  # setea las medidas

    # Inserto la imagen de fondo
    imagen = pygame.image.load("Imagen_fondo_juego.jpg")

    # Ejecuta la musica del juego
    pygame.mixer.music.load("musica.juego.mp3")
    pygame.mixer.music.play()  # ejecuta la musica
    soundWin = pygame.mixer.Sound("sound.mario.mp3")
    soundFail = pygame.mixer.Sound("windows.error.mp3")

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0

    puntaje = 0   # Almacena el puntaje anterior antes de que la variable puntos sea incrementada
    puntaje2 = 0  # Verifica si el puntaje obtenido fue positivo o negativo
    correctos = 0  # verifica la cantidad de palabras correctas
    fallos = 0  # verifica la cantidad de
    candidata = ""  # palabra que ingresa el usuario
    listaIzq = []
    listaMedio = []
    listaDer = []
    posicionesIzq = []  # son posiciones x,y ---ejemplo--- [46,60]
    posicionesMedio = []
    posicionesDer = []
    lista = []

    archivo = open("lemario_nuevo.txt", "r")  # abre el archivo
    for linea in archivo.readlines():
        lista.append(linea[0:-1])

    cargarListas(lista, listaIzq, listaMedio, listaDer,
                 posicionesIzq, posicionesMedio, posicionesDer)
    dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq,
            posicionesMedio, posicionesDer, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 5

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata)-1]
                if e.key == K_ESCAPE:  # tecla agregada para volver atras estando dentro del juego. Esto da la posibilidad de comenzar de vuelta el juego si el usuario quiere. TECLA ESCAPE regresa al menu
                    pygame.display.set_mode(TAMANO_PANTALLA)
                    pygame.mixer.music.pause()
                    pygame.mixer.music.load(
                        "musica.menu.mp3")  # Musica del menu
                    pygame.mixer.music.play()

                    return  # el return finaliza todo
                if e.key == K_RETURN:

                    puntaje = puntos
                    puntos += procesar(lista, candidata,
                                       listaIzq, listaMedio, listaDer)
                    puntaje2 = puntos-puntaje
                    # segun si hay error o acierto, suena la musica correspondiente
                    if puntaje2 > 0:
                        # Reinicio puntaje 2, para verificar nuevamente en la proxima ronda.
                        puntaje2 = 0
                        fallos = 0
                        # Sumo uno a correctos, el cual si llega a tres aciertos
                        correctos += 1
                        if correctos == 1:  # se reproduce el sonido de mario
                            soundWin.play()
                            correctos = 0
                    else:
                        puntaje2 = 0
                        correctos = 0
                        fallos += 1  # Se le incrementa uno a los fallos del usuario
                        if fallos == 1:  # Si el usuario obtiene 3 fallos.
                            soundFail.play()  # se reproduce el sonido de error de windows
                            fallos = 0
                    candidata = ""

        # LE SUMAMOS EL TIEMPO QUE ESTA EN EL MENU, para que no comience a correr el tiempo una vez entrado en el menu # actualizando el tiempo
        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + tiempoMenu/1000 + 1

        # Limpiar pantalla anterior pero con la imagen puesta
        screen.blit(imagen, (0, 0))
        # Dibujar de nuevo todo
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer,
                posicionesIzq, posicionesMedio, posicionesDer, puntos, segundos)

        pygame.display.flip()

        actualizar(lista, listaIzq, listaMedio, listaDer,
                   posicionesIzq, posicionesMedio, posicionesDer)

    # while 1:
    #     # Esperar el QUIT del usuario
    #     for e in pygame.event.get():
    #         if e.type == QUIT:
    #             pygame.quit()
    #             return

    archivo.close()  # cierra automaticamente el juego
    pygame.mixer.music.pause()  # detiene la musica
    # pygame.mixer.music.load("musica.menu.mp3")  # carga la musica del menu
    # pygame.mixer.music.play(10)  # vuelve a inicializar la musica del menu
    if puntos <= 25:  # si tuviste menos de 25 puntos perdiste
        # Musica de la pantalla puntaje
        pygame.mixer.music.load("sad.song.meme.mp3")
        pygame.mixer.music.play(3)

    else:  # si tenes mas de 25 puntos ganaste
        pygame.mixer.music.load("song.happy.mp3")
        pygame.mixer.music.play(3)
    ventanaPuntaje(puntos)  # Imprime el puntaje obtenido en la pantalla final
    pygame.quit()
    exit()

#-----------------------------------------------------------------------#


def menu_principal():  # funcion MENU EN PANTALLA

    surface.fill(COLOR1)


play_menu = pygameMenu.Menu(surface,  # titulo seccion
                            bgfun=menu_principal,
                            color_selected=COLOR_BLANCO,
                            font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                            font_color=COLOR_LETRAS_MENU,
                            font_size=45,
                            menu_alpha=100,
                            menu_color=COLOR_NEGRO_JUEGO,
                            menu_height=int(TAMANO_PANTALLA[1] * 0.9),
                            menu_width=int(TAMANO_PANTALLA[0] * 0.9),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title="JUGAR",
                            window_height=TAMANO_PANTALLA[1],
                            window_width=TAMANO_PANTALLA[0]
                            )

play_menu.add_option("NUEVA PARTIDA", main)
play_menu.add_option("REGRESAR AL MENU", PYGAME_MENU_BACK)

#--------------------------------------------------------------------------------------------#
# INTERNAUTA DESTINADO A SER EL ELEGIDO PARA MANIPULAR LAS REDES INFORMATICAS
# INFORMACION DEL MENU

COMO_JUGAR = ["El juego consiste en armar palabras utilizando las letras que van", "descendiendo en pantalla. Usted solo puede ingresar palabras", "que existan en el diccionario de lengua española. Si usa letras de la", "segunda columna ya no podra usar de la primera, y asi sucede con la", "tercera columna.", "Cuanto mas palabras aciertes, mayor puntaje recibiras.", "Para ganar debes obtener un puntaje MAYOR a 25 puntos", "Cada vez que aciertes una palabra, ésta se eliminara del diccionario", "LEER APARTADO 'SISTEMA DE PUNTUACION'", "Esperamos que disfrutes el juego.", "BUENA SUERTE!",
              "", "Si superas el juego, te convertiras en el internauta destinado a ser", "elegido para manipular las redes informaticas, al igual que NEO", "(Personaje principal de Matrix (La pelicula)). "]

about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=menu_principal,
                                 color_selected=COLOR_BLANCO,
                                 font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                                 font_color=COLOR_LETRAS_MENU,
                                 font_size=45,
                                 menu_alpha=100,
                                 menu_color=COLOR_NEGRO_JUEGO,
                                 menu_height=int(TAMANO_PANTALLA[1] * 0.9),
                                 menu_width=int(TAMANO_PANTALLA[0] * 0.9),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 # titulo de la seccion reglas del juego
                                 title="REGLAS",
                                 window_height=TAMANO_PANTALLA[1],
                                 window_width=TAMANO_PANTALLA[0]
                                 )

for reglas in COMO_JUGAR:
    about_menu.add_line(reglas)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option("REGRESAR AL MENU", PYGAME_MENU_BACK)


#--------------------------------------------------------------------------------------------#

# PARA LOS AGRADECIMIENTOS

AGRADECIMIENTOS = ["CONTACTO", "KEILA ORIANA LOPEZ : keiorilo2013@gmail.com ", "EZEQUIEL PEREYRA : ezeipereyra14@gmail.com  ", "MELANY ROBALO :  melirobalo@gmail.com ", "TOMAS VILLALBA : totovillalba.tv@gmail.com ",

                   "", "Podes realizar donaciones a nuestro equipo de desarrollo",
                   'CVU : 0000003100035931095409', "ALIAS : GROUP.IP.14", "", "", "2021 MATRIX Game. Todos los derechos reservados. 2021"]

agradecimientos_menu = pygameMenu.TextMenu(surface,
                                           bgfun=menu_principal,
                                           color_selected=COLOR_BLANCO,
                                           font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                                           font_color=COLOR_LETRAS_MENU,
                                           font_size=45,
                                           menu_alpha=100,
                                           menu_color=COLOR_NEGRO_JUEGO,
                                           menu_height=int(
                                               TAMANO_PANTALLA[1] * 0.9),
                                           menu_width=int(
                                               TAMANO_PANTALLA[0] * 0.9),
                                           onclose=PYGAME_MENU_DISABLE_CLOSE,
                                           option_shadow=False,
                                           title="CREDITOS",
                                           window_height=TAMANO_PANTALLA[1],
                                           window_width=TAMANO_PANTALLA[0]
                                           )

for agradecimiento in AGRADECIMIENTOS:
    agradecimientos_menu.add_line(agradecimiento)
agradecimientos_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
agradecimientos_menu.add_option("REGRESAR AL MENU", PYGAME_MENU_BACK)

#--------------------------------------------------------------------------------------------#

# PARA LA INFO DE LA MATRIX

INFO_MATRIX = ["¿Porque MATRIX?", "Al ver la base del juego, nos sentimos inspirados y nos recordo",  "a la saga de peliculas MATRIX.",
               "",
               "Acerca de la saga de peliculas MATRIX (1999) (2003) (2003) (2021).",
               "La pelicula plantea que en el futuro, tras una dura guerra, casi todos",
               "los seres humanos han sido esclavizados por las maquinas y las",
               "inteligencias artificiales creadas. Estas los tienen en suspension y", "con sus mentes conectadas a una realidad virtual llamada 'Matrix'", "que representa el final del siglo XX.", "", "Desde nuestro punto de vista como espectadores", "RECOMENDAMOS QUE LAS VEAN"]

#--------------------------------------------------------------------------------------------#

infoMatrix_menu = pygameMenu.TextMenu(surface,
                                      bgfun=menu_principal,
                                      color_selected=COLOR_BLANCO,
                                      font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                                      font_color=COLOR_LETRAS_MENU,
                                      font_size=45,
                                      menu_alpha=100,
                                      menu_color=COLOR_NEGRO_JUEGO,
                                      menu_height=int(
                                          TAMANO_PANTALLA[1] * 0.9),
                                      menu_width=int(TAMANO_PANTALLA[0] * 0.9),
                                      onclose=PYGAME_MENU_DISABLE_CLOSE,
                                      option_shadow=False,
                                      title="ACERCA DE LA MATRIX",
                                      window_height=TAMANO_PANTALLA[1],
                                      window_width=TAMANO_PANTALLA[0]
                                      )
for info in INFO_MATRIX:
    infoMatrix_menu.add_line(info)
infoMatrix_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
infoMatrix_menu.add_option("REGRESAR AL MENU", PYGAME_MENU_BACK)

#----------------------------------------------------------------#
# PARA EL SISTEMA DE PUNTACION

SIS_PUNTACION = ["IMPORTANTE", "Para sumar puntos, la palabra debe contener mas de 3 letras", "", "SISTEMA DE PUNTOS : Si la palabra ingresada es valida, se calculara",
                 "de la siguiente manera :", "", "VOCALES = 1 Punto", "CONSONANTES COMUNES : b-c-d-f-g-h-l-m-n-p-r-s-t-v = 2 Puntos", "CONSONANTES DIFICILES : j-k-q-w-x-y-z = 3 Puntos ", "", "Si la palabra ingresada es incorrecta o no se encuentra en el diccionario,", "se te restaran 5 puntos."]


puntuacion_menu = pygameMenu.TextMenu(surface,
                                      bgfun=menu_principal,
                                      color_selected=COLOR_BLANCO,
                                      font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                                      font_color=COLOR_LETRAS_MENU,
                                      font_size=45,
                                      menu_alpha=100,
                                      menu_color=COLOR_NEGRO_JUEGO,
                                      menu_height=int(
                                          TAMANO_PANTALLA[1] * 0.9),
                                      menu_width=int(TAMANO_PANTALLA[0] * 0.9),
                                      onclose=PYGAME_MENU_DISABLE_CLOSE,
                                      option_shadow=False,
                                      title="SISTEMA DE PUNTUACION",
                                      window_height=TAMANO_PANTALLA[1],
                                      window_width=TAMANO_PANTALLA[0]
                                      )
for punto in SIS_PUNTACION:  # aca hago la pestaña para la el sistema de puntacion
    puntuacion_menu.add_line(punto)
puntuacion_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
puntuacion_menu.add_option("REGRESAR AL MENU", PYGAME_MENU_BACK)
#----------------------------------------------------------------#
# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            bgfun=menu_principal,
                            color_selected=COLOR_BLANCO,
                            font=pygameMenu.fonts.FONT_ORBI_MEDIUM,
                            font_color=COLOR_LETRAS_MENU,
                            font_size=45,
                            menu_alpha=100,
                            menu_color=COLOR_NEGRO_JUEGO,  # color de ventana
                            menu_height=int(TAMANO_PANTALLA[1] * 0.9),
                            menu_width=int(TAMANO_PANTALLA[0] * 0.9),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title="MENU",
                            window_height=TAMANO_PANTALLA[1],
                            window_width=TAMANO_PANTALLA[0]
                            )

main_menu.add_option("MATRIX GAME", play_menu)
main_menu.add_option("COMO JUGAR", about_menu)
main_menu.add_option("SISTEMA DE PUNTUACION", puntuacion_menu)
main_menu.add_option("QUE ES MATRIX?", infoMatrix_menu)
main_menu.add_option("CREDITOS", agradecimientos_menu)
main_menu.add_option("SALIR AL ESCRITORIO", PYGAME_MENU_EXIT)
# -----------------------------------------------------------------------------#
# Aca es donde llamo a la funcion para poner el menu en pantalla
while True:

    clock.tick(60)

    # Eventos
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()

    # Main menu: lo de abajo ejecuta el menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

# # Programa Principal ejecuta Main
# if __name__ == "__main__":
#     main()
"""no es necesario ejecutarlo porque ya lo hice"""
