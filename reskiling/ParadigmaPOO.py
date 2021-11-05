

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

























