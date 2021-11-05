# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QC6qXLgSiq3NgNOUaN2jDlO_9Os3Ozfj
"""

# PROGRAMACION ORIENTADA A OBJETOS

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def  sentarse(self):
        print(f'{self.nombre.title()} esta sentado!!!!')

    def dar_vuelta(self, vueltas):
        print(f'{self.nombre.title()} se da {vueltas} vuelta!!!!')

perro1 = Perro('Chooolooo', 4)
perro2 = Perro('Cachuloooooo', 10)
perro1.edad
print(f'El nombre de mi perro es {perro2.nombre.title()} y tiene {perro2.edad} años')

perro2.sentarse()
perro1.dar_vuelta(5)

# SOBRECARGA DE METODOS
class WebScraper:
    def __init__(self,version):
        self.version = version 
#*ARGS podemos agregar la cantidad de parametros que queramos al metodo   
    def capturar_enlace(self, *enlace):
        for enlaces in enlace:
            print('Capturando enlace >>>',enlaces)
#**KWARGS
    def capturar_etiqueta(self, **etiquetas):
        for key, value in etiquetas.items():
            print(key, ':', value)



prototipo = WebScraper(1.0)
prototipo.capturar_enlace(3,'texto',4,5,6)
prototipo.capturar_etiqueta(etiqueta = {'atributos','contenedores','footer'},
                            imagenes = {'banner','logo','carrusel'},
                            enlaces = {'htttps//','google','com'})


