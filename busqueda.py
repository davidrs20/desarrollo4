import os
import csv
import argparse


#Función para leer el archivo csv y devolver una lista de frases
def leer_csv(archivo):
    '''Lee un archivo CSV y devuelve una lista de frases'''
    frases = []
    with open(archivo 'r', encoding='0utf-8') as f:
        lector =csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
    return frases

# Funcion para buscar plabras de las frases 
def buscar_palabras(frases, palabras):
    ''' Busca una lista de palabras en una lista de frases'''
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break
    return frases_encontradas

# Función para mostar las frases encontradas
def mostrar_frases(frases):
    '''Muestra las frases encontradas'''
    for frase in frases:
        print(frase)

# Función principal
def main(archivo, lista_palabras): 
    '''Función principal'''
    #leer el archivo CSV
    frases = leer_csv(archivo)
    #buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)
    #mostrar las frases encontradas
    mostrar_frases(frases_encontradas)

if __name__ == '__main__':
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description='Buscar palabras en un archivo CSV.')
    # Añadir los argumentos
    parser.add_argument('archivo', type=str, help='Ruta del archivo CSV')
    parser.add_argument('palabras', type=str, nargs='+', help='Lista de palabras a buscar')
    # Parsear los argumentos
    args = parser.parse_args()
    # Llamar a la función principal
    main(args.archivo, args.palabras)