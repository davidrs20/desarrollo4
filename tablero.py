'''
tablero.py: dibuje el tablero del juego de el gato
'''
import random

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero de juego del gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
''')

def ia(simbolos:dict):
    ''' Juega la maquina '''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''Juega el usuario'''
    ocupado = True
    while ocupado is True:
        x = input('Ingresa el numero de la casilla: ')
        if x in numeros:
            if simbolos[x] not in ['X', 'O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else: 
            print ('Numero incorrecto')

def juego(simbolos:dict):
    '''Juego del Gato'''
    lista_combinaciones = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Horizontales
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Verticales
        ['1', '5', '9'], ['3', '5', '7']  # Diagonales
    ]
    en_juego = True
    ganador = ""
    movimientos = 0
    dibuja_tablero(simbolos)
    while en_juego:
        if movimientos < 9:
            usuario(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is True:
                en_juego = False
                ganador = 'Usuario/a'
            ia(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is True:
                en_juego = False
                ganador = 'Computadora'
        else :
            en 


def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay un ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos [c[0]]
    return None

if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    #x = random.choice(numeros)
    #numeros.remove(x)
    #simbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    #o = random.choice(numeros)
    #numeros.remove(o)
    #simbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    #print(numeros)