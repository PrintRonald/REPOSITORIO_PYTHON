# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QC6qXLgSiq3NgNOUaN2jDlO_9Os3Ozfj
"""

# CREACION DE CLASES
class Perro:
     def __init__(self, nombre, edad):
         self.nombre = nombre
         self. edad = edad

     def ladrar(self):
         print(f'{self.nombre} dice "GUAU GUAU!!!!!"')
    
     def comer(self, comida):
         print(f'{self.nombre} ha comido {comida} platos')
    
# INSTANCIANDO UNA CLASE
perro1 = Perro('Cachupin',7)
perro2 = Perro('Boby',2)
perro1.nombre
perro1.edad
perro2.nombre
perro2.edad
# INVOCANDO EL METODO LADRAR
perro1.ladrar()
perro2.ladrar()
# INVOCANDO EL METODO COMER
perro1.comer(3)
perro2.comer(6)

from abc import ABC, abstractmethod
class Pago(ABC):
    def imprimir(self, monto):
        print('Monto de compra- ', monto)
    @abstractmethod
    def pago(self, monto):
        pass
class PagoTarjetaCredito(Pago):
    def pago(self, monto):
        print('Pago de tarjeta de credito por- ', monto)
class PagoBilleteraMovil(Pago):
    def pago(self, monto):
        print('Pago de billetera movil por- ', monto)

# LA MAGIA ESTA EN GUARDAR EN UNA VARIABLE (INSTANCIAR) EL METODO 
obj = PagoTarjetaCredito()
# LUEGO SE INVOCA CON EL METODO QUE ESTA A LA VISTA
obj.pago(100)
obj.imprimir(100)
isinstance(obj, Pago)
obj = PagoBilleteraMovil()
obj.pago(200)
obj.imprimir(200)
isinstance(obj, Pago)

# ENCAPSULAMIENTO
class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 456
      self.__c = 789
      self.__version = 3.0  


#FORMA CORRECTA DE OBTENER UN DATO ENCAPSULADO 
   def getVersion(self):
       return self.__version

   def setVersion(self, a):
        self.__version = a

robot1 = Robot()
#objeto._Clase__atributo
robot1._Robot__c
#FORMA CORRECTA DE OBTENER UN DATO ENCAPSULADO 
robot1.getVersion()
#FORMA CORRECTA DE MODIFICAR UNA DATO ENCAPSULADO
robot1.setVersion(3.1)
robot1.getVersion()

