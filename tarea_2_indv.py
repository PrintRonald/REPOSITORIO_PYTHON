
print('Bienvenido a la aplicacion "preparemos tu primer año de U"')


lista_completa = []
while len(lista_completa) <= 6:
    nombre = input('Para comenzar, dime tu nombre completo')
    print('Hola', nombre, 'bienvenido a "preparemos tu primer año de U"')
    print('A continuacion, prepararemos tu perfil')
    edad = input('¿Que edad tienes?')
    f_Nacimiento = input('¿Cual es tu fecha de nacimiento?')
    ciudad = input('¿Donde vives?')
    lista_usuarios = []
    if len(lista_usuarios) <= 6:
        lista_usuarios.append(nombre)
        lista_usuarios.append(edad)
        lista_usuarios.append(f_Nacimiento)
        lista_usuarios.append(ciudad)
        lista_completa.append(lista_usuarios)
    print(lista_usuarios)
print(lista_completa)
print(lista_completa[0])
print(lista_completa[2])
print(lista_completa[5])

buscar_usuario = str(input('Desea buscar un usuario de la lista entre (0 y 6)? (Si/No)'))
if buscar_usuario == 'Si':
    usuario = int(input('Ingrese el usuario que desea buscar:'))
    print(lista_completa[usuario])
else:
    print('El usuario no esta dentro de la lista')
    

lista_saludo = []
while len(lista_saludo) <= 6:
    nombre = input('Para comenzar, dime tu nombre para saludarte')
    lista_saludo.append(nombre)
    print(lista_saludo)
print('Usuarios registrados')
print(lista_saludo)
print('La cantidad de usuarios son:', len(lista_saludo))
for i in lista_saludo:
    print('BIENVENIDO A TU SESION', i)
    i =+ 1





 

