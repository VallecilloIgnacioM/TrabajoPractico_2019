import time
from random import randint
from datetime import datetime, timedelta, date

# Variables Globales.
ESTADO = ("Nuevo", "Usado")
PUNTUACION = ("1.Mala", "2.Regular", "3.Buena", "4.Muy Buena", "5.Excelente")
PROVINCIAS = ('Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Cordoba', 'Corrientes', 'Entre Rios',
              'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquen',
              'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe',
              'Santiago del Estero', 'Tierra del Fuego', 'Tucuman')
ENVIO = ("A Domicilio", "Retiro en sucursal")


# Definicion de la Clase Articulo.
class Articulo:
    def __init__(self, codigo, precio, ubicacion, estado, cantidad, puntuacion):
        self.codigo = codigo
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cantidad = cantidad
        self.puntuacion = puntuacion


# Definicion de la clase Compra, en el parametro fecha se generan fechas aleatorias del año 2000 al dia de hoy.
class Compra:
    def __init__(self, codigo, cantidad, precio, tipo_envio, total):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio
        self.tipo_envio = tipo_envio
        self.total = total
        self.fecha = date.today() + timedelta(days=randint(-7000, 0))


# Funcion que permite crear y cargar de manera automatica el vector con los articulos.
def carga(n):
    v = [None] * n
    for i in range(n):
        v[i] = Articulo(randint(1, 9999), randint(100, 5000), randint(1, 23),
                        randint(1, 2), randint(0, 50), randint(1, 5))
    return v


# To string nos permite darle formato a cada articulo en una sola linea horizontal
def to_string(articulo):
    r = ''
    r += '{:<15}'.format('Codigo: ' + str(articulo.codigo))
    r += '{:<16}'.format('Precio: $' + str(articulo.precio))
    r += '{:<36}'.format('Ubicacion: ' + PROVINCIAS[articulo.ubicacion - 1])
    r += '{:<18}'.format('Estado: ' + ESTADO[articulo.estado - 1])
    r += '{:<26}'.format('Cantidad disponible: ' + str(articulo.cantidad))
    r += '{:<20}'.format('Puntuacion del vendedor: ' + PUNTUACION[articulo.puntuacion - 1])
    return r


def to_string_compra(compra):
    r = ''
    r += '{:<15}'.format('Codigo: ' + str(compra.codigo))
    r += '{:<23}'.format('Cantidad comprada: ' + str(compra.cantidad))
    r += '{:<16}'.format('Precio: $' + str(compra.precio))
    r += '{:<28}'.format('Envio: ' + ENVIO[compra.tipo_envio - 1])
    r += '{:<18}'.format('Total: ' + str(compra.total))
    r += '{:<20}'.format('Fecha: ' + str(compra.fecha))
    return r


# Ordenamiento de Shell con modificacion que permite optar que ordenar
def shell_sort(v, opcion):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            if opcion == 1:
                while k >= 0 and y.codigo < v[k].codigo:
                    v[k + h] = v[k]
                    k -= h

            elif opcion == 2:
                while k >= 0 and y.fecha < v[k].fecha:
                    v[k + h] = v[k]
                    k -= h
            else:
                while k >= 0 and y.precio < v[k].precio:
                    v[k + h] = v[k]
                    k -= h
            v[k + h] = y
        h //= 3


# Permite hacer un print de un vector con el formato dado por la funcion to_string.
def mostrar_todo(v):
    for i in range(len(v)):
        print(to_string(v[i]))


# Validador generico de numeros
def validar_dato(menor=None, mayor=None):
    x = int(input('Ingrese el numero:'))
    while ((menor is not None) and x < menor) or ((mayor is not None) and x > mayor):
        dato_incorrecto = ('\033[1;31m' + 'Numero Incorrecto!' + '\033[0;m' + ' Vuelva a ingresar')
        if menor is not None:
            dato_incorrecto += ('\033[1;m' + ' - Mayor que ' + str(menor) + '\033[0;m')
        if mayor is not None:
            dato_incorrecto += ('\033[1;m' + ' - Menor que ' + str(mayor) + '\033[0;m')
        print(dato_incorrecto)
        x = int(input('Ingrese el numero:'))
    return x


# Validador para el menu, restringe la eleccion a la cantidad de opciones.
def validar_menu(menor_a):
    print('\033[4;30m' + "\nMENU DE OPCIONES" + '\033[;m')
    print('1) Comprar')
    print('2) Mostrar compras')
    print('3) Rango de precios')
    print('4) Favoritos')
    print('5) Actualizar Favoritos ')
    print('6) Eliminar archivos')
    print('7) Salir')
    print()
    x = int(input('\033[1;34m' + 'Su opcion:' + '\033[;m'))
    while x < 1 or x > menor_a:
        print('\033[1;31m' + 'Error!' + '\033[0;m' + ' Debe ingresar un numero entre 1 y ' + str(menor_a))
        x = int(input('\033[1;34m' + 'Su opcion:' + '\033[;m'))
    return x


# Buscador binario de un elemento(x) en un vector.
def buscar(vector, x):
    izq = 0
    der = len(vector) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if vector[medio].codigo == x:
            return medio

        elif vector[medio].codigo > x:
            der = medio - 1

        else:
            izq = medio + 1

    return False


# Se retorna True si el vector esta vacio.
def comprobar_vector(vector):
    return len(vector) == 0


# Se valida que la fecha ingresada sea de formato aaaa-mm-dd y que sea anterior a la fecha actual.
def validar_fecha():
    correcto = False
    x = i = None
    while not correcto:
        x = input()
        if len(x) == 10:

            for i in range(10):
                if not (es_numero(x[i]) or ((i == 4 or i == 7) and (x[i] == '-'))):
                    i = 0
                    break

            if i == 9:
                x = date.fromisoformat(x)
                if x <= date.today():
                    correcto = True

        if not correcto:
            print('\033[1;30m' + 'Se ha ingresado mal la fecha ó una fecha posterior al dia de hoy.'
                  ' Por favor, vuelva a ingresar con formato aaaa-mm-dd' + ':\033[;m')

    return x


# Retorna True si es un numero.
def es_numero(x):
    return x in '0123456789'


# Se insertan elementos a un vector por insercion ordenada.
def insertar_ordenado(v, publicacion, opcion=1):
    n = len(v)
    izq = 0
    der = n - 1
    pos = n
    if opcion == 1:
        while izq <= der:
            c = (izq + der) // 2
            if v[c].codigo == publicacion.codigo:
                pos = c
                break
            elif publicacion.codigo > v[c].codigo:
                izq = c + 1
            else:
                der = c - 1
    else:
        while izq <= der:
            c = (izq + der) // 2
            if v[c].fecha == publicacion.fecha:
                pos = c
                break
            elif publicacion.fecha > v[c].fecha:
                izq = c + 1
            else:
                der = c - 1

    if izq > der:
        pos = izq

    v[pos:pos] = [publicacion]


def test():
    pass


if __name__ == '__main__':
    test()
