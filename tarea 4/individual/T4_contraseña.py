
usuario = input('Ingrese su nombre: ')
clave = str(input('Ingrese su clave: '))
lista_general =[]
while usuario != '':
    validar = False # valida que se cumplan los requisitos
    largo = len(clave) # calcula el largo de la clave
    espacio = False #variable para identificar espacios
    mayuscula = False #variable para identificar mayusculas
    minuscula = False #variable para identificar minuscula
    numeros = False #variable para identificar numeros
    alfanumerico = clave.isalnum() # si es alfanumerico devuelve True
    correcto = True #devuelve que hayan, mayusculas, minuscula, numeros y no alfanumericos

    for caracter in clave:
        if caracter.isspace()==True:
            espacio = True
        if caracter.isupper()==True:
            mayuscula = True
        if caracter.islower()==True:
            minuscula = True
        if caracter.isdigit()==True:
            numeros = True
    if espacio == True:
        print('---------------ALERTA---------------------')
        print('La contraseña no puede contener espacios en blanco')
        print('---------------ALERTA---------------------')
    else:
        validar=True
    if largo < 8 and validar==True:
        print('---------------ALERTA---------------------')
        print('La contraseña debe tener como minimo 8 caracteres')
        print('---------------ALERTA---------------------')
        validar = False
    if mayuscula == True and minuscula == True and numeros== True and alfanumerico== False and validar == True:
        validar =True
    else:
        correcto=False
    if validar == True and correcto==False:
        print('---------------ALERTA---------------------')
        print('La contraseña elegida no es segura: debe contener minuscula, mayuscula, numeros y al menos un caracter alfanumerico')
        print('---------------ALERTA---------------------')
    if validar == True and correcto== True:
        print('---------------CONTRASEÑA CORRECTA---------------------')
        print('La clave ha sido introducida correctamente')
        print('---------------CONTRASEÑA CORRECTA---------------------')
        clave_usuario = []
        clave_usuario.append(usuario)
        clave_usuario.append(clave)
        lista_general.append(clave_usuario)  
        usuario = input('Ingrese su nombre: ')
        clave = str(input('Ingrese su clave: '))       
print(lista_general)
diccionario = dict(lista_general)
print(diccionario)
for i,j in diccionario.items():
    print(f'{i} tiene la clave {j}')








    

    

