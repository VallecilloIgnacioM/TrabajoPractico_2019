import pickle
import os.path
from Principal import inicio, validar_dato

# Se asignan variables con los nombres de los archivos necesarios


A_Compra = 'miscompras.dat'
A_Favorito = 'favoritos.dat'
A_Articulos = 'Articulos.dat'


def grabar(dato, nombre_archivo):
    # Se abre como archivo binario en modo append, si el archivo existe se agregan los datos.
    # Si NO existe, se crea el archivo.
    archivo = open(nombre_archivo, "wb")
    pickle.dump(dato, archivo)
    archivo.close()
    return


def leer(nombre_archivo):
    # Vector a cargar
    data = []
    # Se verifica si el archivo existe
    if os.path.exists(nombre_archivo):

        # Se abre el archivo binario en modo lectura
        archive = open(nombre_archivo, "rb")

        # Se lee secuencialmente el archivo
        while archive.tell() < os.path.getsize(nombre_archivo):
            # Se carga el vector con todos los datos
            data = pickle.load(archive)
        archive.close()

        # Se retorna el vector cargado
    return data



