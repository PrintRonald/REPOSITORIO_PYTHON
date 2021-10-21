

print('----BIENBENIDO A LA APLICACION----') # SE DA LA BIENVENIDA AL PROGRAMA
info_usuarios = {} # SE CREA EL DICCIONARIO CON LOS USUARIOS A INGRESAR
while True: # SE CONDICIONA PARA QUE MIENTRAS SEA TRUE CADA OPCION SE EJECUTEN LAS INTRUCCIONES
    print('--OPCIONES--') # SE IMPRIMEN LAS DISTINTAS OPCIONES
    print("""
    [1] Agregar usuario
    [2] Eliminar usuario
    [3] Mostrar informacion de cada usuarios
    [4] Mostrar la fecha de incorporacion de cada usuario
    [5] Salir del programa
    """)
    n =(input('Ingrese una opcion: ')) # EL USUARIO INGRESA LA OPCION QUE DESEA EJECUTAR
    if n == '1': # SE AGREGAN USUARIOS AL DICCIONARIO
        IDusuario = int(input('Ingrese el ID del usuario: ')) # SE PIDE EL NOMBRE DEL USUARIO A INGRESAR
        info_usuarios[IDusuario] = {} # SE CREA UN SUBDICCIONARIO PARA INGRESAR LOS ATRIBUTOS DE CADA USUARIO
        nombre = input('Ingrese el nombre de usuario: ') # SE PIDE EL ATRIBUTO NOMBRE
        info_usuarios[IDusuario]['Nombre'] = nombre # SE INGRESA AL SUBDICCIONARIO CON LA CLAVE 'NOMBRE'
        edad = int(input('Edad del usuario: ')) # SE PIDE EL ATRIBUTO EDAD
        info_usuarios[IDusuario]['Edad'] = edad # SE INGRESA AL SUBDICCIONARIO CON LA CLAVE 'EDAD'
        genero = input('Ingrese le genero del usuario: (M O F)') # SE PIDE EL ATRIBUTO GENERO
        info_usuarios[IDusuario]['genero'] = genero # SE INGRESA AL SUBDICCIONARIO CON LA CLAVE 'GENERO'
        antiguedad = input('ingrese el año de ingreso del usuario') # SE PIDE EL ATRIBUTO ANTIGUEDAD
        info_usuarios[IDusuario]['Antiguedad'] = antiguedad # SE INGRESA AL SUBDICCIONARIO CON LA CLAVE 'ANTIGUEDAD'
        print(info_usuarios) # SE IMPRIME EL DICCIONARIO 
    elif n== '2': # SE ELIMINAN USUARIOS SEGUN EL ID
        IDusuario = int(input('Ingrese el ID de usuario: '))# SE PIDE EL ID DEL USUARIO A ELIMINAR
        del info_usuarios[IDusuario] # CON LA FUNCION DEL SE ELIMINA EL USUARIO DEL DICCIONARIO
        print(info_usuarios) # SE IMPRIMER EL DICCIONARIO
    elif n == '3': # MOSTRAR EL ID DEL USUARIO
        for clave, valor in info_usuarios.items(): # SE RECORRE EL DICCIONARIO PARA MOSTRAR CADA ID Y SUBDICCIONARIO DE CADA USUARIO 
            for clave1, valor1 in valor.items(): # SE RECORRE EL SUBDICCIONARIO PARA MOSTRAR EL ATRIBUTO CORRESPONDIENTE A CADA USUARIO
                if clave1 == 'Nombre': # CONDICIONAMOS PARA QUE CONTRASTE LA CLAVE1 CON LA CLAVE 'NOMBRE' DE DICHO DICCIONARIO
                    print(f'El usuario {valor1} corresponde al ID: {clave}') # SE IMPRIME LA INFORMACION 
    elif n == '4': # MOSTRAR LA FECHA DE INCORPORACION DE CADA USUARIO
        for clave, valor in info_usuarios.items():# SE RECORRE EL DICCIONARIO PARA MOSTRAR CADA USUARIO
            for clave1, valor1 in valor.items():# SE RECORRE EL SUBDICCIONARIO PARA MOSTRAR LOS ATRIBUTOS DE CADA USUARIOS
                if clave1 == 'Nombre': # CONDICIONAMOS PARA QUE CONTRASTE LA CLAVE1 CON LA CLAVE 'NOMBRE' DE DICHO DICCIONARIO
                    print(f'El usuario {valor1}') # IMPRIMO EL VALOR ENCONTRADO
                if clave1 == 'Antiguedad': # CONDICIONAMOE PARA QUE CONTRASTE LA CLAVE1 CON LA CLAVE 'ANTIGUEDAD' DE DICHO DICCIONARIO
                    print(f'Se inscribio el {valor1}') # IMPRIMO EL VALOR ENCONTRADO  
    elif n == '5':
        break # CREAMOS LA OPCION DE SALIDA DEL PROGRAMA
    else:
        print('Ingrese una opcion correcta: ') # FINALMENTE CREAMOS UNA CONDICION POR SI EL USUARIO INGRESA UNA OPCION INCORRECTA


