'''
Este archivo es el punto de entrada a la aplicación. Aquí se importan las funciones de tablero.py y se ejecutan en un ciclo while.
'''
import tablero

def main():
    ''' Función principal '''
    nombre_usuario = input('Ingrese su nombre (presione Enter para "Usuario"): ').strip()
    if not nombre_usuario:
        nombre_usuario = "Usuario"
    
    score = {
        nombre_usuario: {"G": 0, "P": 0, "E": 0},
        "IA": {"G": 0, "P": 0, "E": 0}
    }

    numeros =[str(i) for i in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score, g, nombre_usuario)
        tablero.despliega_tablero(score, nombre_usuario)

        seguir = input('¿Quieres seguir? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    main()