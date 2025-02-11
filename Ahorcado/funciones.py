'''
funciones auxiliares del juego Ahorcado
'''

def carga_archivos_texto(archivo:str)-> list:
    '''
    Carga un archivo de un texto y develve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones
 
def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(5):
        plantillas[i] = carga_archivos_texto(f'./Plantilla/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel <=5:
        plantilla = diccionario[nivel]
        for renglon in plantilla:
            print(renglon)


if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla, 0)
    lista_oraciones = carga_archivos_texto('./Datos/pg15532.txt')
    print(lista_oraciones[100:115])
 