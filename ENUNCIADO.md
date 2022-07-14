Mercado Libre es una aplicación muy conocida para permitir la compra/venta en línea de todo tipo de artículos en forma directa por cualquier usuario.

A partir de la información generada en el TP3….

Se solicita simular los resultados de una búsqueda en Mercado Libre de un artículo x. Para ello, se requiere la realización de al menos tres módulos independientes (registro, archivos y principal).


Cargar automáticamente los resultados de la búsqueda en un vector de n registros (n se ingresa por teclado). Por cada registro se debe indicar:


código de publicación



precio



ubicación geográfica (1-23 identificando cada provincia de la Argentina)



estado (nuevo/usado)



cantidad disponible



puntuación del vendedor ( 1-5 identificando 5 como Excelente y 1 Mala).


El vector debe quedar ordenado por código de publicación.

Mostrar el vector generado.


Se solicita un nuevo menú con las siguientes opciones...


Comprar: buscar una publicación cuyo código se ingresa por teclado. Si no existe, informar con un mensaje. Si existe, preguntar al usuario qué cantidad de artículos desea comprar, validar que la cantidad disponible sea suficiente, y confirmar/rechazar la compra según corresponda. 


Si la compra pudo confirmarse, realizar las siguientes acciones:


Restar en la publicación la cantidad comprada por el usuario



Consultar al usuario si desea envío a domicilio (costo 10% de la compra) o retira en sucursal



Calcular el monto de acuerdo a la cantidad de articulos comprados y a la forma de envío elegida



Agregar el registro de la compra en el archivo binario miscompras.dat, con el siguiente formato:



código de publicación



cantidad comprada



precio



tipo de envío



monto total abonado (incluyendo envío si corresponde)



fecha de la compra en formato aaaammdd (investigar cómo tomar fecha actual en Python)



Generar un archivo de texto para enviar al usuario el detalle de la operación realizada. Suponiendo que el usuario compra la publicación #1234, el archivo debe verse así:


-----------------------------------------------

Compra #1234 - 29/09/2019

Resumen de compra

Producto     $1000 (2 x $500)

Cargo de envio     $ 100

Tu pago        $1100

-----------------------------------------------


Mis compras: mostrar el contenido del archivo miscompras.dat, para un intervalo de fechas que se ingresa por teclado



Rango de precios: informar el menor y mayor precio encontrado en la búsqueda. Permitir que el usuario ajuste el mínimo y máximo que desea gastar, usando como topes mínimo y máximo los valores encontrados. Mostrar las publicaciones que se encuentren en ese rango de precios.



Agregar favorito: Buscar una publicación cuyo código se ingresa por teclado. Si no existe, informar con un mensaje. Si existe, agregarla a un vector de favoritos (evitar repeticiones en el mismo). El vector de favoritos debe quedar ordenado por código de publicación aplicando la inserción ordenada.  Mostrar el listado de favoritos. 



Actualizar Favoritos: Actualizar el archivo binario de favoritos con el vector y mostrar el archivo resultante. Teniendo en cuenta lo siguiente:



Si existe el archivo favoritos.dat, verificar que todos los registros que están en el vector de favoritos estén en el archivo sin repetirse. 



Si no existe, generar un nuevo archivo binario llamado favoritos.dat.

