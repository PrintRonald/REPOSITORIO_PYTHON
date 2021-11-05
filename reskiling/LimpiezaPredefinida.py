# ACCIONES DE LIMPIEZA PREDEFINIDA


try:   
    archivo = open('miarchivo.txt', 'w')
    archivo.write('Hola soy un archivo nuevo2....')
except:
    print('Error con el archivo no se cerro correctamente')  
finally:
    archivo.close()


