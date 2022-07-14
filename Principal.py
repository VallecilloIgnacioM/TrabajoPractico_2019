from Modulos.registro import *
from Modulos.archivos import *
import os
from datetime import date


# Creamos la funcion inicio para cargar los articulos y los guardamos en un archivo "Articulo.dat"
# para agilizar el testing
def inicio():
    if not os.path.exists("Articulos.dat"):
        print('Ingrese la cantidad de articulos que desea crear. Por favor, mayor que 0: ')
        n = validar_dato(0)
        print('\033[4;m' + '\nLista Completa de Articulos' + '\033[;m')

        # Carga del vector con los articulos
        lista_articulos = carga(n)

        # Ordenamiento del vector por codigo de articulo
        shell_sort(lista_articulos, 1)

        # Guardar en un archivo la lista de articulos.
        grabar(lista_articulos, A_Articulos)
    else:
        lista_articulos = leer(A_Articulos)
    # Print en pantalla
    mostrar_todo(lista_articulos)
    return lista_articulos


def generar_ticket(compra):
    # Estructura del ticket
    dato = "-----------------------------------------------\n" \
           "Compra #{0} - {1}\n" \
           "Resumen de compra\n" \
           "Producto       ${2} ({3} x ${4})\n" \
           "Cargo de envio ${5}\n" \
           "Tu pago        ${6}\n" \
           "-----------------------------------------------\n"
    # Se abre el archivo en modo append texto
    archivo = open("Ticket.txt", "at")
    semitotal = (compra.cantidad * compra.precio)
    envio = round(compra.total - semitotal)
    # Se da formato el ticket
    dato = dato.format(compra.codigo, compra.fecha, semitotal, compra.cantidad, compra.precio,
                       envio, compra.total)
    # Se guarda el ticket en el archivo.
    archivo.write(dato)


def opcion_1(lista_articulos):
    print("\033[4;30m" + '\nBIENVENIDO AL SISTEMA DE COMPRA' + '\033[;m')
    op = "s"
    lista_compras = leer(A_Compra)
    # Repetir compra si desea el cliente.
    while op in ("s", "S"):
        # Se ingresa el codigo de publicacion.
        print("Ingrese el codigo de la publicacion a comprar:")
        codigo_compra = validar_dato(0)

        # Se busca el articulo.
        i = buscar(lista_articulos, codigo_compra)

        # Se verifica si el articulo existe y si tiene cantidad mayor a 0.
        if i is not False and lista_articulos[i].cantidad > 0:

            # Se imprime el articulo buscado.
            print("Articulo encontrado:\n", to_string(lista_articulos[i]))
            print("Ingrese la cantidad de articulos a comprar:")

            # se verifica que la cantidad ingresada sea menor a la cantidad disponible.
            cantidad = validar_dato(1, lista_articulos[i].cantidad)

            # Se resta la cantidad comprada a la disponible.
            lista_articulos[i].cantidad -= cantidad
            print("Desea envio a domicilio(costo 10% de la compra)?(s/n)")
            x = input()

            # Se calcula el precio total
            total = cantidad * lista_articulos[i].precio

            # Si es envio a domicilio se agrega 10% al total.
            if x in ("S", "s"):
                total += round(total * 0.1, 2)
                envio = 1
            else:
                envio = 0

            # Se genera un registo Compra con los datos ingresados.
            compra = Compra(lista_articulos[i].codigo, cantidad, lista_articulos[i].precio, envio, total)
            # Se guarda el registro compra al archivo "miscompras.dat"
            insertar_ordenado(lista_compras, compra, 2)
            print("Compra realizada con exito!")
            # Se genera el ticket
            generar_ticket(compra)
            print("Su ticket fue generado con exito! Disfrute su compra.")

        else:
            # Si el articulo no existe o el parametro cantidad es igual a 0, se avisa por mensaje
            print("El articulo no existe ó no tiene cantidad suficiente para realizar la compra.")

        # Se permite volver a comprar
        print("Desea realizar otra compra?(s/n)")
        op = input()
    grabar(lista_compras, A_Compra)


def opcion_2():
    print('\n\033[4;30m' + 'LISTADO DE COMPRAS POR FECHA' + '\033[;m')

    # Se lee el archivo "miscompras.dat"
    v = leer(A_Compra)
    if len(v) > 0:

        # Se pide el rango de fechas a buscar.
        print('Ingrese las fechas con formato aaaa-mm-dd')

        # Se valida que la fecha ingresada sea el formato correcto y anterior a la fecha actual.
        print('Desde: ')
        desde = validar_fecha()
        print('Hasta: ')
        hasta = validar_fecha()

        # En el caso de que se ingrese fechas invertidas posterior/anterior, se invierten las fechas.
        # Anti-troll.
        if desde > hasta:
            desde, hasta = hasta, desde

        print('\n\033[4;30m' + 'Compras realizadas desde ' + str(desde) + ' hasta ' + str(hasta) + ':\033[;m')

        # Bandera control para emitir mensaje de NO haber coincidencia con el rango de fechas.
        bandera = True
        for i in range(len(v)):

            # Si existen articulos comprados dentro del rango de fechas se muestra por pantalla.
            if desde <= v[i].fecha <= hasta:
                print(to_string_compra(v[i]))
                bandera = False
        if bandera:
            print('No se han registrado compras con el intervalo de fechas ingresado.')

    else:
        # Si el vector esta vacio se informa por mensaje
        print("No has comprado articulos todavia!")


def opcion_3(lista_articulos):
    # Ordenamos previamente la lista de articulos por precio
    v = lista_articulos[:]
    shell_sort(v, 3)

    # Asignamos a var menor_precio el primero de la lista y a var mayor_precio el ultimo de la lista
    menor_precio = v[0]
    mayor_precio = v[-1]

    # Mostramos en pantalla los mismos.
    print('\n\033[4;30m' + 'FILTRO POR PRECIOS' + '\033[;m')
    print('El valor del articulo de menor precio es: $' + str(menor_precio.precio))
    print('El valor del articulo de mayor precio es: $' + str(mayor_precio.precio) + '\n')

    # Permitimos que el usuario ajuste la busqueda basado en el monto que desea gastar.
    print('Cual es el monto MINIMO que desea gastar?')
    minimo = validar_dato(menor_precio.precio)
    print('Cual es el monto MAXIMO que desea gastar?')
    maximo = validar_dato(minimo, mayor_precio.precio)

    # Se buscan y se muestran cuales son los articulos que estan dentro de dicho rango.
    print('\nFiltro de precio aplicado:')
    for i in range(len(v)):
        if minimo <= v[i].precio <= maximo:
            print(to_string(v[i]))

    # Damos la opcion si desea comprar alguno de los articulos y se lo redirecciona a la opcion de Compras(opc 1)
    x = input('\n Desea realizar una compra?(s/n)')
    if x in ('S', 's'):
        opcion_1(lista_articulos)


def opcion_4(lista_art, list_fav):
    print('\n\033[4;30m' + 'FAVORITOS ' + '\033[;m')
    print('Ingrese el codigo del articulo que desea agregar a Favoritos: ')
    cod = validar_dato(0)

    # Se busca el articulo dentro de la lista original de articulos.
    # Si existe coincidencia, se asigna a la var "i" la posicion del articulo dentro del vector "lista_art"
    i = buscar(lista_art, cod)

    if i is not False:
        # verifica que el articulo no esté agregado ya.
        if buscar(list_fav, lista_art[i].codigo) is not False:
            print('\n\033[1;30m' + 'El articulo ya existe en la lista de favoritos!' + '\033[;m')
        else:
            # Se agrega el articulos si no esta en la lista de favoritos.
            insertar_ordenado(list_fav, lista_art[i])

        # Muestra la lista completa de articulos favoritos.
        print('\n\033[4;30m' + 'Lista de Favoritos:' + '\033[;m')
        mostrar_todo(list_fav)
        return list_fav

    else:
        # Si el articulo no esta dentro de la lista de articulos, se avisa por mensaje.
        print('El codigo del articulo buscado no coincide con ninguno existente. ')


def opcion_5(lista_fav):
    print('\n\033[4;30m' + 'ACTUALIZAR FAVORITOS' + '\033[;m')
    # Si la lista de favoritos esta vacia, se avisa por mensaje.
    if len(lista_fav) == 0:
        print('\n\033[1;31m' + 'No exiten articulos favoritos' + '\033[;m')
        return

    # Se verifica si existe el Archivo "favoritos.dat"
    if os.path.exists(A_Favorito):

        # Se lee el archivo, se compara cada Art de la nueva lista de favoritos con los del vector recuperado.
        archivo_fav = leer(A_Favorito)
        for i in range(len(archivo_fav)):
            if buscar(lista_fav, archivo_fav[i].codigo) is False:
                # Si hay algun favorito nuevo, lo agrega al ultimo.
                insertar_ordenado(lista_fav, archivo_fav[i])

    print('\n\033[4;30m' + 'Lista de Favoritos:' + '\033[;m')
    # Se muestra por pantalla la lista de favoritos completa

    mostrar_todo(lista_fav)
    # Si el archivo existe, se actualiza con la nueva lista. Si no existe, se crea el archivo "favoritos.dat"
    grabar(lista_fav, A_Favorito)


# Funcion para eliminar archivos de forma permantente.
def borrar_archivo(archivo):
    print('\n\033[1;31m' + 'ATENCION!' + '\033[;m' + " Se eliminará definitivamente el archivo", archivo, "\nDesea continuar?(s/n)")
    x = input()
    if x in ("S", "s"):
        if os.path.exists(archivo):
            os.remove(archivo)
            print("Se ha eliminado exitosamente el archivo.")
        else:
            print("El archivo no existe.")


def eliminar_archivos():
    print('\n\033[4;30m' + 'MENU DE GESTION DE ARCHIVOS' + '\033[;m')
    op = -1
    while op != 5:
        print("1) Eliminar archivo 'Articulos.dat'")
        print("2) Eliminar archivo 'miscompras.dat'")
        print("3) Eliminar archivo 'Ticket.txt'")
        print("4) Eliminar archivo 'favoritos.dat'")
        print("5) Volver atras")
        op = validar_dato(0, 5)

        # Elimina el archivo "Articulos.dat"
        if op == 1:
            borrar_archivo(A_Articulos)
            print("A Continuacion se volvera a generar la lista de articulos")
            menu()
            break

        # Elimina el archivo "miscompras.dat"
        elif op == 2:
            borrar_archivo(A_Compra)

        # Elimina el archivo "Ticket.txt"
        elif op == 3:
            borrar_archivo("Ticket.txt")

        # Elimina el archivo "favoritos.dat"
        elif op == 4:
            borrar_archivo(A_Favorito)


# Menu de opciones
def menu():
    # Llama la funcion la inicio() para cargar la lista de articulos ya sea desde archivo o generar uno nuevo
    lista_articulos = inicio()
    lista_favoritos = []
    opc = 0
    print('\n\033[1;32m' + "BIENVENIDO AL KWIK-E-MART" + '\033[;m' + '\033[1;31m' + ' ONLINE(V2.0)' +
          '\033[;m' + '\033[1;m' + ' ahora con mas bugs que antes' + '\033[;m')
    while opc != 7:

        opc = validar_menu(7)

        if opc == 1:
            opcion_1(lista_articulos)
        elif opc == 2:
            opcion_2()
        elif opc == 3:
            opcion_3(lista_articulos)
        elif opc == 4:
            opcion_4(lista_articulos, lista_favoritos)
        elif opc == 5:
            if comprobar_vector(lista_favoritos):
                print('\n\033[1;31m' + 'No exiten articulos en la lista favoritos' + '\033[;m')
            else:
                opcion_5(lista_favoritos)
        elif opc == 6:
            eliminar_archivos()
        elif opc == 7:
            print('---Gracias por su compra---')
            print('\n\033[1;32m' + 'MUCHAS GRACIAS VUELVAS PRONTOS' + '\033[;m')


if __name__ == '__main__':
    menu()
