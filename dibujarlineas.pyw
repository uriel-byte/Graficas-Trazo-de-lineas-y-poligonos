#########################################
#
# Script sencillo para dibujar líneas negras
# con un ratón en un lienzo blanco
#
#########################################

# paquetes
from tkinter import Canvas
import cv2
import numpy as np
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from graphics import *


# init un lienzo
canvas = np.zeros((600, 800, 1), np.uint8)

# hacer de lienzo blanco
canvas.fill(255)

# coordenadas globales y de estado de dibujo
x = 0
y = 0
dibujo = False

# mouse función de devolución de llamada
def dibujar(event, current_x, current_y, flags, params):
    # gancho de variables globales
    global x, y, dibujo
    
    # manejar el mouse con el evento
    if event == cv2.EVENT_LBUTTONDOWN:
        # actualización de coordenadas
        x = current_x
        y = current_y
        
        # activa el dibujo de la bandera
        dibujo = True
    
    # manejar el mouse mover evento
    elif event == cv2.EVENT_MOUSEMOVE:
        # sorteo sólo si el ratón está abajo
        if dibujo:
            # dibujar la línea
            cv2.line(canvas, (current_x, current_y), (x, y), 0, thickness=3)
            
            # actualización de coordenadas
            x, y = current_x, current_y
    
    # manejar el mouse hasta el evento
    elif event == cv2.EVENT_LBUTTONUP:
        # deshabilitar el dibujo de la bandera
        dibujo = False
    

# mostrar el lienzo en una ventana
cv2.imshow('Dibujar', canvas)

# enlazar los eventos de ratón
cv2.setMouseCallback('Dibujar', dibujar)

# infinito bucle de dibujo
while True:
    # actualización de lona
    cv2.imshow('Dibujar', canvas)
    
    # salir de un programa de 'Esc' botón de golpe
    if cv2.waitKey (1) & 0xFF == 27: break
     

 # limpieza de windows
cv2.destroyAllWindows()
