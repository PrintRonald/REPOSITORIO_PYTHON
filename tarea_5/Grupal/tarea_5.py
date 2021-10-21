texto ="""
  Guarde en una variable la siguiente información:
● Información de clientes: nombre, edad, identificador único.
● Información de productos: nombre, precio, identificador único y color.
● Información de la compra de cada cliente. 
Debe crear 10 clientes y 5 productos
La forma en que se organiza la información es a criterio del equipo. Es decir, ustedes definen el número
de variables y tipo de datos.

Sin definir funciones, utilice métodos necesarios para:
● Agregar Cliente.
● Agregar Producto
● Mostrar Clientes: Muestra el listado de clientes.
● Mostrar Producto: Muestra el listado de productos.
● Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
● Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?

En el caso que la información se esté guardando en un diccionario.
- Imprima todas las claves con un delay de 2 segundos.
- Luego imprima los valores con un delay de 3 segundos.

El código siempre debe estar debidamente comentado. Esto les ayudará a comprenderlo en el futuro y
ayudará a otras personas a comprender su código.

¿Lo lograron?
Imprima en pantalla un listado que contenga los ID de los usuarios.
Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
Imprima en pantalla los nuevos ID.
Elimine los últimos cuatro ID_clientes en el listado.
"""
# SE CREA EL DICICONARIO CLIENTES CON CLAVE Y VALOR, ADEMAS UN SUBDICCIONARIO CON CLAVE Y VALOR
clientes = {
    1234 :{'nombre_cliente' : 'Juan' ,'edad' : 25 },
    4563 :{'nombre_cliente' : 'Pedro' ,'edad' : 25},
    8757 :{'nombre_cliente' : 'Carlos' ,'edad' : 25, },
    6124 :{'nombre_cliente' : 'Esteban' ,'edad' : 25  },
    8993 :{'nombre_cliente' : 'Marcos' ,'edad' : 25},
    3461 :{'nombre_cliente' : 'Neifer' ,'edad' : 25 },
    5476 :{'nombre_cliente' : 'Ronald' ,'edad' : 25},
    9809 :{'nombre_cliente' : 'Joan' ,'edad' : 25},
    2354 :{'nombre_cliente' : 'Pablo' ,'edad' : 25},
    2434 :{'nombre_cliente' : 'Contanza' ,'edad' : 25}
}
# SE CREA EL DICICONARIO PRODUCTOS CON CLAVE Y VALOR, ADEMAS UN SUBDICCIONARIO CON CLAVE Y VALOR
productos = {
    1111 :{'nombre_producto': 'zapatillas','precio' : 5000,'color' : 'rojo'},
    2222 :{'nombre_producto': 'zapatillas','precio' : 5000,'color' : 'rojo'},
    3333 :{'nombre_producto': 'zapatillas','precio' : 5000,'color' : 'rojo'},
    4444 :{'nombre_producto': 'zapatillas','precio' : 5000,'color' : 'rojo'},
    5555 :{'nombre_producto': 'zapatillas','precio' : 5000,'color' : 'rojo'}
}
compras = {
}
# SE CREA UN CICLO WHILE PARA CONDICIONAR LA ENTRADA Y SALIDA DEL PROGRAMA
while True :
    print('----OPCIONES-------') # SE CREAN LAS OPCIONES QUE EL USUARIO TENDRA PARA REALIZAR UNA ACCION
    print('1. agregar cliente')
    print('2. agregar producto')
    print('3. mostrar clientes')
    print('4. mostrar productos')
    print('5. elimine cliente')
    print('6. elimine productos')
    print('7. salir del programa')
    n = int(input('Escoger una opcion --> ')) # OPCION PARA DEFINIR QUE ACCION REALIZARA EL USUARIO
    if n == 1: # AGREGAR CLIENTE
        IDcliente = int(input('Ingrese el ID del cliente: ')) 
        nombre_cliente = str(input('Ingrese el nombre del nuevo cliente: ')).capitalize()
        edad = int(input('Ingresa la edad: '))
        clientes[IDcliente]= {'nombre_cliente': nombre_cliente, 'edad': edad}
        print(clientes) # AL DICCIONARIO CLIENTE SE ASIGNA UN SUBDICCIONARIO CON EL NOMBRE Y LA EDAD DEL CLIENTE
    elif n == 2: # AGREGAR PRODUCTO
        IDproductos = int(input('Ingrese el ID del producto: '))
        nombre_producto = str(input('Ingrese el nombre del producto: '))
        precio = float(input('Ingrese precio del producto: '))
        color = str(input('Ingrese el color del producto: '))
        productos[IDproductos] = {'nombre_producto': nombre_producto, 'precio': precio, 'color' : color}
        print(productos) # AL DICCIONARIO PRODUCTO SE ASIGNA UN SUBDICCIONARIO CON EL NOMBRE Y LA EDAD DEL CLIENTE
    elif n == 3: # MOSTRAR CLIENTES
        for clave1, valor1 in clientes.items():# SE RECORRE EL DICCIONARIO CLIENTE PARA OBTENER LOS VALORES
            for clave,valor in valor1.items(): # SE RECORRE EL SUBDICCIONARIO CLIENTE PARA OBTENER LA CLAVE
                if clave == 'nombre_cliente': # SE CONDICIONA PARA QUE LA CLAVE DEL SUBDICCIONARIO SE CORRESPONDA A LA CLAVE DEL MISMO
                    print(f'{clave1} corresponde a {valor}') # SE IMPRIME EL RESULTADO DE LA BUSQUEDA
    elif n == 4: # MOSTRAR PRODUCTOS
        for clave1, valor1 in productos.items(): # SE RECORRE EL DICCIONARIO PRODUCTOS PARA OBTENER LOS VALORES
            for clave, valor in valor1.items(): # SE RECORRE EL SUBDICCIONARIO PRODUCTOS PARA OBTENER LA CLAVE
                if clave == 'nombre_producto':# SE CONDICIONA PARA QUE LA CLAVE DEL SUBDICCIONARIO SE CORRESPONDA A LA CLAVE DEL MISMO
                    print(f'{clave1} corresponde al producto {valor}')# SE IMPRIME EL RESULTADO DE LA BUSQUEDA
    elif n == 5: # ELIMINAR CLIENTE
        IDcliente = int(input('Ingrese el ID del cliente a eliminar:')) # SE INGRESA EL CLIENTE A ELIMINAR
        del clientes[IDcliente] # CON LA FUNCION DEL ELIMINAMOS EL CLIENTE QUE DESEAMOS
        print(clientes)
    elif n == 6: # ELIMINAR PRODUCTO
        IDproductos = int(input('Ingrese el ID del producto a eliminar:')) # SE INGRESA EL PRODUCTO A ELIMINAR
        del productos[IDproductos] # CON LA FUNCION DEL ELIMINAMOS EL PRODUCTO QUE DESEAMOS
        print(productos)
    elif n == 7: # FINALMENTE DAMOS LA OPCION DE SALIR DEL PROGRAMA CON EL COMNADO BREAK
        break
    else:
        print('Ingrese una opcion correcta: ') # MENSAJE DE ALERTA POR SI EL USUARIO INSERTA UNA OPCION INCORRECTA




        















