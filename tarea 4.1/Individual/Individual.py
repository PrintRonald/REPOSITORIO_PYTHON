
import random

usuarios = []
edad = []
print('--------------------------------')
print('BIENVENIDO A REGITRO DE USUARIOS') #SE DA LA BUENVENIDA AL USUARIO
print('--------------------------------')
# SE CREA UN MENU DE OPCIONES PARA INSERTAR, ELIMINAR Y MOSTRAR USUARIOS ALEATORIAMENTE
while True: 
    print('--------------------------------')
    print('1. Ingresar un usuario')
    print('2. Eliminar a un usuario')
    print('3. mostrar todos los usuarios registrados')
    print('4. mostrar 5 usuarios aleatorios')
    print('5. salir del programa')
    print('---------SELECCIONE UNA OPCION-------------')
    n = input('Seleccione una opcion---> ') # SE CREA UNA VARIABLE DONDE EL USUARIO PUEDE ESCOGER LA OPCION QUE ESTIME MEJOR
    print('--------------------------------')

# SE CONDICIONA SEGUN LAS OPCIONES QUE ESTAN DISPONIBLES EN EL MENU
    if n == '1': 
        nombre_usuario = input('Ingrese el nombre del usuairo: ').capitalize() #SE INGRESA EL USUARIO POR CONSOLA
        print('--------------------------------')
        edad_usuario = input('Ingrese la edad del usuario: ') #SE INGRESA LA EDAD DEL USUARIO POR CONSOLA
        print('--------------------------------')
        usuarios.append(nombre_usuario) #SE AGREGA EL USUARIO A LA LISTA USUARIOS
        edad.append(edad_usuario) #SE AGREGA LA EDAD A LA LISTA EDAD
    elif n == '2':
        eliminar_usuario = input('Ingrese el usuario a eliminar: ').capitalize() #POR CONSOLA SE BUSCA EL USUARIO QUE QUIERE ELIMINAR
        if eliminar_usuario not in usuarios: #SI EL USUARIO NO ESTA EN LA LISTA ME ENTREGA UN MENSAJE D ALERTA
            print('--------------------------------')
            print('Este usuario no esta en la lista')
            print('--------------------------------')
        else: #DE CASO CONTRARIO LO ELIMINA DE LA LISTA
            usuarios.remove(eliminar_usuario)
    elif n == '3':
        print('----------LISTA DE USUARIOS--------------')
        for i in usuarios: #SE RECORRE LA LISTA USUARIOS PARA MOSTRARLOS SI EL USUARIO LO DESEA
            print(f'- {i}')
        print('--------------------------------')
    elif n == '4':
        if len(usuarios) < 5: # SE CONDICIONA LA LISTA USUARIOS PARA QUE ME PUEDA MOSTRAR 5 USUARIOS
            print('--------------------------------')
            print('No hay sufucientes usuarios para mostrar')
            print('--------------------------------')
        else: # DE CASO CONTRARIO ESCOGE 5 USUARIOS ALEATORIOS PARA MOSTRARLOS EN PANTALLA
            mostrar = random.sample(usuarios,5)
            print('-----------USUARIOS ALEATORIOS-------------')
            for j in mostrar:
                print(f'- {j}')
            print('--------------------------------')
    elif n == '5': #FINALEMNTE SE DA LA OPCION DE SALIR DEL PROGRAMA A TRAVES DEL COMANDO BREAK
        break
    else: # SI NO SE SELECCIONA UNA OPCION CORRECTA DEL MENU, SE ENTREGA UNA ALERTA 
        print('--------------------------------')
        print('ingrese una opcion correcta: ')
        print('--------------------------------')



    



