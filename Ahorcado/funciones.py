def carga_archivo_texto(archivo:str)->str:
    """
    Carga un archivo de texto y devuelve su una lista con las oraciones del archivo
    """
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == "__main__":
    print(carga_archivo_texto("oraciones.txt"))