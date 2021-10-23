import time
"""
- Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’.
"""

#FUNCIONES
def diccionario():
    global diccionario
    diccionario= {}
    return diccionario

def ingresar_usuario(diccionario):
    nombre = input('Ingrese su nombre: ')
    contrasena = input('Ingrese su contraseña: ')
    edad = int(input('Ingrese su edad: '))
    diccionario[nombre] = {}
    diccionario[nombre]['contraseña'] = contrasena
    diccionario[nombre]['edad'] = edad
    return diccionario


def mostrarUsuarios ():
    print ('-------Listado de Usuarios--------')
    print ('')

    for usuario,valores in diccionario.items():
        print (f'Usuario: {usuario}  Datos: {valores}') 
        time.sleep(5)

#INICIO
diccionarioTotal = diccionario()
while True:
    print('---OPCIONES---')
    print("""
    [1] Ingresar a aplicacion
    [2] Mostrar usuarios registrados
    [3] Salir del programa
    """)
    n = int(input('Ingrese una opción --> '))

    if n == 1:
        usuario = ingresar_usuario(diccionario)
        print('A ingresado a la aplicación')
        print("Bienvenido a ... ")
        print("""              _                  __
           ____ ___  (_)  ________  ____/ /
          / __ `__ \/ /  / ___/ _ \/ __  /
         / / / / / / /  / /  /  __/ /_/ /
        /_/ /_/ /_/_/  /_/   \___/\__,_/
        
        """)
    elif n == 2:
        print(mostrarUsuarios())
    elif n == 3:
        break
    else:
        print('Ingrese una opción correcta: ')
#FIN

