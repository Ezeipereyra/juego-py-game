# from principal import *
from typing import List
from configuracion import *
from nuestrasFunciones import*
import random
import math
import time


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    # elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente
    # Tengo que hacer que se separen las palabras en 3 partes y mande cada una de esas partes
    # a cada columna,
    # no hace falta que devuelva nada,

    palabra = random.choice(lista)
    ingreso = dividirPalabra(palabra)  # separa en 3 partes y
    ubicacion_Y = -10
    # Agregamos las letras segun corresponda
    # ListaIzquierda

    # crea una lista de posiciones en X Los parametros son el ancho de la columna izquierda
    listaizq_X = ubicacionesEnX(5, ANCHO//3-20)
    for elemento in ingreso[0]:
        listaIzq.append(elemento)  # agregamos dentro de una listas las letras
        # asigna una ubicacion en x con random
        ubicacion_X = random.choice(listaizq_X)
        ubicacion = [ubicacion_X, ubicacion_Y]
        # agrega a la lista posiciones, ubicacion x e y
        posicionesIzq.append(ubicacion)
        # elimina de la lista de posiciones de x, la posicion agregada a la lista posiciones asi no hay ubicaciones iguales
        listaizq_X.remove(ubicacion_X)

    # Lista del Medio

    # Los parametros son el ancho de la columna del medio
    listaMed_X = ubicacionesEnX(ANCHO//3+10, 2*ANCHO//3-15)
    for elemento in ingreso[1]:
        listaMedio.append(elemento)
        # elige una ubicacion en x al azar
        ubicacion_X = random.choice(listaMed_X)
        ubicacion = [ubicacion_X, ubicacion_Y]
        posicionesMedio.append(ubicacion)
        listaMed_X.remove(ubicacion_X)

    # Lista de la derecha

    # Los parametros son el ancho de la columna derecha
    listaDer_X = ubicacionesEnX(2*ANCHO//3+10, ANCHO-10)
    for elemento in ingreso[2]:
        listaDer.append(elemento)
        ubicacion_X = random.choice(listaDer_X)
        ubicacion = [ubicacion_X, ubicacion_Y]
        posicionesDer.append(ubicacion)
        listaDer_X.remove(ubicacion_X)


def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    for posicion in posiciones:  # creo que es aca donde debe ver si hay dos posiciones iguales, si lo son deberia cambiar la posicion de lugar
        velocidad = 20  # asigna una velocidad para que vaya incrementando
        y = posicion[1]  # la posicion en Y, esta como una sub lista
        if posicion[1] < ALTO-90:
            y += velocidad
            posicion[1] = y
        else:
            if y == (ALTO-90):
                lista.pop(0)
                posiciones.pop(0)


def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    # llama a otras funciones para bajar  las letras, eliminar las que tocan el piso y
    # cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    bajar(listaIzq, posicionesIzq)
    bajar(listaMedio, posicionesMedio)
    bajar(listaDer, posicionesDer)
    cargarListas(lista, listaIzq, listaMedio, listaDer,
                 posicionesIzq, posicionesMedio, posicionesDer)


def Puntos(palabra):

    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h",
                   "l", "m", "n", "p", "r", "s", "t", "v"]
    consonantesdificiles = ["j", "k", "q", "w", "x", "y", "z"]
    puntajes = 0
    for i in palabra:
        if i in vocales:  # por aca entran las vocales
            puntajes += 1

        if i in consonantes:  # por acá entran las consonantes
            puntajes += 2

        if i in consonantesdificiles:  # por aca entran las consonantes dificiles
            puntajes += 5

    return puntajes


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    if esta(candidata, lista):
        contador_1 = 0  # por cada lista agregamos un contador
        contador_2 = 0
        nueva1 = ""  # en estas string vacias guardamos la palabra valida
        nueva2 = ""
        nueva3 = ""
        for letra in candidata:  # recorremos la palabra
            if letra in listaIzq and letra not in nueva1 and contador_1== 0 and contador_2 == 0:
                # si la letra se encuentra en la lista se agrega a una nueva donde se almacena
                nueva1 += letra
            elif letra in listaMedio and letra not in nueva2 and contador_2== 0:
                nueva2 += letra
                contador_1 += 1
            elif letra in listaDerecha and letra not in nueva3:
                contador_2 += 1
                nueva3 += letra
        # asignamos una variable "nueva" para sumar las 3 cadenas
        nueva = nueva1+nueva2+nueva3
        if nueva == candidata:  # si nueva es igual a candidata la damos por valida
            lista.remove(candidata) #eliminamos la palabra del lemario si el usuario ya la ingreso, por lo tanto no se puede elegir dos veces la misma palabra
            return True
    else:
        return False  # si no es valida la toma como error, o si ya fue elegida


# devuelve True si candidata cumple con los requisitos


def procesar(lista, candidata, listaIzq, listaMedio, listaDer):
    if len(candidata) < 4:  # para evitar palabras con len menor a 4
        return 0
    if esValida(lista, candidata, listaIzq, listaMedio, listaDer):
        return Puntos(candidata)
    else:
        return -5

    # chequea que candidata sea correcta en  cuyo caso devuelve el puntajes y 0 si no es correcta
