'''
    Programa principal del juego del ahorcado. 
'''
import funciones as fn
from random import choice
import string

def main():
    '''
    Programa principal del juego del ahorcado
    '''
    # cargamos las plantillas del juego
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = carga_archivo_texto('./Datos/pg15532.txt')
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 # oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 1:
        fn.despliega_plantilla(plantillas)
